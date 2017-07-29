import React, { Component } from 'react';

import Form from "react-jsonschema-form";

const log = (type) => console.log.bind(console, type);


class Form2 extends Component {
  constructor(props) {
    super(props);

    this.state = {schema: {}};
  }

  componentWillMount() {
    let that = this;

    console.log('component will mount')
    fetch('/api/user/schema')
    .then(function(response) {
      console.log()
      return response.json();
    }).then(function(json) {
      console.log(json)
      that.setState({ schema: json})
    }).catch(function(err) {
      console.log(err);
    });
  }

  render() {
    console.log('rendering');
    return (
      <Form schema={this.state.schema}
        onChange={log("changed")}
        onSubmit={log("submitted")}
        onError={log("errors")} />
    );
  }
}

export default Form2;
