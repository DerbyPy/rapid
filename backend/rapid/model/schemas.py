import logging

from keg.db import db
from marshmallow import validate
import marshmallow_sqlalchemy as masa
from ..model import entities as ents

log = logging.getLogger(__name__)


class _ModelConverter(masa.ModelConverter):
    """ Customized so required fields do not accept an empty string. """
    def _add_column_kwargs(self, kwargs, column):
        super()._add_column_kwargs(kwargs, column)
        if kwargs['required'] and hasattr(column.type, 'length'):
            lenval = validate.Length(min=1, error='Empty string not valid for required field.')
            kwargs['validate'].append(lenval)


class _BaseOpts(masa.ModelSchemaOpts):
    """
        Cleanest method to automatically associate our SQLAlchemy session.
        See: https://marshmallow-sqlalchemy.readthedocs.io/en/latest/recipes.html#base-schema-ii
    """
    def __init__(self, meta):
        meta.sqla_session = db.session
        meta.model_converter = _ModelConverter
        super().__init__(meta)


class _ModelSchema(masa.ModelSchema):
    """ See note on _BaseOpts """
    OPTIONS_CLASS = _BaseOpts


class UserSchema(_ModelSchema):
    class Meta:
        model = ents.User


user = UserSchema()  # noqa
users = UserSchema(many=True)  # noqa
