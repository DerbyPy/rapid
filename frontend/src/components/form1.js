import React, { Component } from 'react';

import Form from "react-jsonschema-form";

const schema = {
  "properties": {
    "name_last": {
      "maxLength": 50,
      "minLength": 1,
      "title": "name_last",
      "type": "string"
    },
    "name_first": {
      "maxLength": 50,
      "minLength": 1,
      "title": "name_first",
      "type": "string"
    },
  },
  "required": [
    "name_first",
    "name_last"
  ],
  "type": "object"
};

const log = (type) => console.log.bind(console, type);

class Form1 extends Component {

  render() {
    return (
      <Form schema={schema}
        onChange={log("changed")}
        onSubmit={log("submitted")}
        onError={log("errors")} />
    );
  }
}

export default Form1;
