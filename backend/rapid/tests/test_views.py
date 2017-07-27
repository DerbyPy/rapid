import flask
import flask.ext.webtest as webtest


from rapid.model import entities as ents


class ViewBase(object):

    @classmethod
    def setup_class(cls):
        # anonymous user
        cls.ta = webtest.TestApp(flask.current_app)


class TestPublic(ViewBase):

    def test_home(self):
        resp = self.ta.get('/')
        assert resp.text == 'Hello World from Rapid!'

    def test_ping(self):
        resp = self.ta.get('/ping')
        assert resp.text == 'rapid ok'


class TestAPI(ViewBase):
    def setup(self):
        ents.User.delete_cascaded()

    def test_users(self):
        ents.User.testing_create(name_first='foo')

        resp = self.ta.get('/api/users')
        users = resp.json['users']
        assert len(users) == 1
        assert users[0]['name_first'] == 'foo'

    def test_user_schema(self):
        resp = self.ta.get('/api/user/schema')
        schema = resp.json
        props = schema['properties']
        dependents = props['dependents']
        assert dependents['title'] == 'dependents'
        assert dependents['type'] == 'integer'
        assert 'format' not in dependents
