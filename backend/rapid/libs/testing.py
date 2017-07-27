from keg_elements.db.mixins import DefaultColsMixin
import sqlalchemy as sa


class ModelBase(object):
    orm_cls = None
    # expects tuples of (key, is_fk, is_required)
    constraint_tests = tuple()
    # expects tuples of (key, scale)
    scale_tests = tuple()

    def setup(self):
        if hasattr(self.orm_cls, 'delete_cascaded'):
            self.orm_cls.delete_cascaded()
        else:
            self.orm_cls.delete_all()

    def make_test_object(self):
        """Allow children to override how to create test objects of this class.
        """
        return self.orm_cls.testing_create()

    def test_add(self):
        assert self.orm_cls.query.count() == 0
        o = self.make_test_object()
        assert self.orm_cls.query.count() == 1
        if hasattr(self.orm_cls, 'id'):
            assert o.id

    def check_nullable_column(self, cname, is_nullable):
        column = getattr(self.orm_cls.__table__.c, cname)
        assert column.nullable is is_nullable, 'Column "{}" has unexpected nullability'\
            .format(cname)

    def check_fk_column(self, cname, is_fk):
        column = getattr(self.orm_cls.__table__.c, cname)
        assert bool(len(column.foreign_keys)) is is_fk

    def check_rel_cascade(self, column):
        types = (
            'delete',
            'expunge',
            'merge',
            'refresh-expire',
            'save-update',
        )

        for cascade_type in types:
            message = 'Missing `{}` in cascade for field {}'.format(cascade_type, column.key)
            assert cascade_type in column.property._cascade, message

        assert 'delete-orphan' in column.property._cascade, 'Missing `delete-orphan` in cascade ' \
                                                            'for field {}.'.format(column.key)

        for relationship in column.property.remote_side:
            for foreign_key in relationship.foreign_keys:
                assert foreign_key.ondelete == 'cascade', \
                    'You must set `ondelete` on the ForeignKey object of the child entity. ' \
                    'Failed on field {}.{}.'.format(
                        foreign_key.parent.table.name,
                        foreign_key.parent.name
                    )

    def test_all_columns_are_constraint_tested(self):
        expected_columns = [col.name for col in self.orm_cls.__table__.columns]
        constraint_columns = [col[0] for col in self.constraint_tests]
        inherited_columns = []

        if isinstance(self.orm_cls(), DefaultColsMixin):
            # Include columns from common import base classes
            for field in vars(DefaultColsMixin):

                # Ignore the usual __class__, __dict__, blah, blah blah
                if field.startswith('__'):
                    continue

                col = getattr(DefaultColsMixin, field)

                # Only consider SQLAlchemy columns
                if isinstance(col, sa.sql.schema.Column):
                    inherited_columns.append(field)

        if len(constraint_columns + inherited_columns) != len(expected_columns):
            expected = set(expected_columns)
            constraint = set(constraint_columns + inherited_columns)

            missing = expected - constraint

            message = ('Missing columns in constraint tests: {}').format('\n- '.join(missing))

            raise AssertionError(message)

    def test_column_constraints(self):
        for cname, is_fk, is_not_nullable in self.constraint_tests:
            self.check_fk_column(cname, bool(is_fk))
            self.check_nullable_column(cname, not is_not_nullable)

    def test_scale(self):
        def check_scale(cname, scale):
            column = getattr(self.orm_cls.__table__.c, cname)
            assert column.type.scale == scale

        for cname, scale in self.scale_tests:
            yield check_scale, cname, scale

    def check_unique_constraint(self, data_first, data_second=None, is_unique=True):
        if data_second is None:
            data_second = data_first

        # add record with data_first
        o = self.orm_cls.add(**data_first)

        # adding with data_second should produce error
        try:
            o2 = self.orm_cls.add(**data_second)
            assert not is_unique, 'Expected %sunique' % ('' if is_unique else 'not ')
            self.orm_cls.delete(o2.id)
        except Exception as e:
            if 'IntegrityError' not in str(e) and 'validation error' not in str(e):
                raise

        self.orm_cls.delete(o.id)

    def test_repr(self):
        assert repr(self.make_test_object())
