import logging

from keg.db import db
import sqlalchemy as sa
# from sqlalchemy_utils import ArrowType

from .utils import EntityMixin

log = logging.getLogger(__name__)


class User(db.Model, EntityMixin):
    __tablename__ = 'users'

    name_first = sa.Column(sa.Unicode(50), nullable=False)
    name_last = sa.Column(sa.Unicode(50), nullable=False)
    dependents = sa.Column(sa.Integer, nullable=False)
    birth_date = sa.Column(sa.Date, nullable=False)
    phone_number = sa.Column(sa.String(10))
