import datetime as dt

import rapid.model.entities as ents
import rapid.model.schemas as schemas


class TestUserSchema:
    def user_data(self, **kwargs):
        data = {'name_first': 'bob', 'name_last': 'smith', 'dependents': 1,
                'birth_date': '2000-01-09', 'phone_number': '5556667777'}
        data.update(kwargs)
        return data

    def test_dump(self):
        bob = ents.User.testing_create(
            name_first='bob',
            name_last='smith',
            dependents=1,
            birth_date=dt.date(2000, 1, 9),
            phone_number='5556667777',
        )

        data = schemas.user.dump(bob).data

        assert not data.errors

        assert data['name_first'] == 'bob'
        assert data['name_last'] == 'smith'
        assert data['dependents'] == 1
        assert data['birth_date'] == '2000-01-09'
        assert data['phone_number'] == '5556667777'

    def test_load_ok(self):
        data = self.user_data()

        result = schemas.user.load(data)
        assert not result.errors

        bob = result.data
        assert bob.id is None
        assert bob.name_first == 'bob'
        assert bob.name_last == 'smith'
        assert bob.dependents == 1
        assert bob.birth_date == dt.date(2000, 1, 9)
        assert bob.phone_number == '5556667777'

    def test_valid_name_length(self):
        long_string = 'f' * 60
        data = self.user_data(name_first=long_string, name_last=long_string)

        result = schemas.user.load(data)
        assert result.errors

        errors = result.errors
        assert errors['name_first'] == ['Longer than maximum length 50.']
        assert errors['name_last'] == ['Longer than maximum length 50.']

    def test_valid_required(self):
        data = self.user_data(name_first='', name_last=None)
        del data['dependents']
        del data['phone_number']

        result = schemas.user.load(data)
        assert len(result.errors) == 3

        errors = result.errors
        assert errors['name_first'] == ['Empty string not valid for required field.']
        assert errors['name_last'] == ['Field may not be null.']
        assert errors['dependents'] == ['Missing data for required field.']

        # import pdb; pdb.set_trace()
