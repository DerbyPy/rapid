import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, hashHistory } from 'react-router'

import './index.css';
import App from './App';
import Form1 from './components/form1'
import Form2 from './components/form2'
import registerServiceWorker from './registerServiceWorker';


ReactDOM.render((
  <Router history={hashHistory}>
    <Route path="/" component={App}/>
    <Route path="/form1" component={Form1}/>
    <Route path="/form2" component={Form2}/>
  </Router>
), document.getElementById('root'))


registerServiceWorker();
