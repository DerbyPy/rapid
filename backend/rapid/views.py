import logging

import flask
from marshmallow_jsonschema import JSONSchema
from blazeutils.strings import case_us2cw

from .model import entities as ents
from .model import schemas

public = flask.Blueprint('public', __name__,)
log = logging.getLogger(__name__)


@public.route('/')
def home():
    return 'Hello World from Rapid!'


@public.route('/api/users')
def users():
    result = schemas.users.dump(ents.User.query)
    return flask.jsonify({'users': result.data})


class _JSONSchema(JSONSchema):
    @classmethod
    def _from_python_type(cls, field, pytype):
        json_schema = JSONSchema._from_python_type(field, pytype)
        if pytype is int:
            json_schema['type'] = 'integer'
            del json_schema['format']
        title = json_schema['title']
        if 'name' in title:
            parts = title.split('_')
            parts.reverse()
            title = ' '.join(parts).title()
        else:
            title = title.replace('_', ' ').title()
        json_schema['title'] = title
        return json_schema


@public.route('/api/user/schema')
def user_schema():
    return flask.jsonify(_JSONSchema().dump(schemas.user).data)
