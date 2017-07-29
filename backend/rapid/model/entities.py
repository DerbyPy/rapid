import enum
import logging


from keg.db import db
import sqlalchemy as sa
import sqlalchemy.orm as saorm
# from sqlalchemy_utils import ArrowType

from .utils import EntityMixin

log = logging.getLogger(__name__)

_rel_cascade = 'all, delete-orphan'


class AgeRange(enum.Enum):
    young = 1
    middle = 2
    old = 3


class User(db.Model, EntityMixin):
    __tablename__ = 'users'

    name_first = sa.Column(sa.Unicode(50), nullable=False)
    name_last = sa.Column(sa.Unicode(50), nullable=False)
    dependents = sa.Column(sa.Integer, nullable=False)
    birth_date = sa.Column(sa.Date, nullable=False)
    phone_number = sa.Column(sa.String(10))
    #age_range = sa.Column(sa.Enum(AgeRange))

    #wagers = saorm.relationship('UserEmail', lazy='subquery', cascade=_rel_cascade,
                                #passive_deletes=True)


class UserEmail(db.Model, EntityMixin):
    __tablename__ = 'user_emails'

    user_id = sa.Column(sa.ForeignKey(User.id, ondelete='cascade'), nullable=False)
    email = sa.Column(sa.Unicode(50), nullable=False)
