# Rapid: SQLAlchemy to React form

A DRY method to turn SQLAlchemy entities (models) into React forms.

Proof of concept: [rapid on Github](https://github.com/DerbyPy/rapid/)

## Projects Needed

* [SQLAlchemy](http://sqlalchemy.org/): SQL Toolkit and Object Relational Mapper (ORM)
* [Marshmallow](https://marshmallow.readthedocs.io/en/latest/): (de)serialization and validation
* [Marshmallow-SQLAlchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/): auto-generates Marshmallow schemas from SQLAlchemy entities
* [JSON Schema](http://json-schema.org/): is a vocabulary that allows you to annotate and validate JSON documents.
* [marshmallow-jsonschema](https://github.com/fuhrysteve/marshmallow-jsonschema): translates marshmallow schemas into JSON Schema Draft v4 compliant jsonschema
* [react-jsonschema-form](https://github.com/mozilla-services/react-jsonschema-form) ([live playground](https://mozilla-services.github.io/react-jsonschema-form/)): builds HTML forms out of a JSON schema

## Customization / Bugs

1. [Required fields should not permit empty string](https://github.com/DerbyPy/rapid/blob/master/backend/rapid/model/schemas.py#L15)
2. marshmallow-jsonschema creates incompatible JSON schema for integers
    - [bug report](https://github.com/fuhrysteve/marshmallow-jsonschema/issues/40)
    - [quick fix](https://github.com/DerbyPy/rapid/blob/master/backend/rapid/views.py#L28)
3. Form field names aren't pretty, [use better titles](https://github.com/DerbyPy/rapid/blob/master/backend/rapid/views.py#L31).
