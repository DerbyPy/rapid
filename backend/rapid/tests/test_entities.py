from rapid.libs.testing import ModelBase
import rapid.model.entities as ents


class TestUser(ModelBase):
    orm_cls = ents.User
    constraint_tests = [
        ('name_first', False, True),
        ('name_last', False, True),
        ('dependents', False, True),
        ('birth_date', False, True),
        ('phone_number', False, False),
    ]
