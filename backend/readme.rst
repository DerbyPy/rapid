.. default-role:: code

Rapid's Readme
######################################

.. image:: https://circleci.com/gh/DerbyPy/rapid.svg?&style=shield&circle-token=d794afcf40d755d518b577eca93970f04c123e54
    :target: https://circleci.com/gh/DerbyPy/rapid

.. image:: https://codecov.io/github/DerbyPy/rapid/coverage.svg?branch=master&token=
    :target: https://codecov.io/github/DerbyPy/rapid?branch=master

Project Setup Checklist
=======================

* `wheelhouse build`
* `tox`
* setup git hooks from /scripts
* create project on

    * GitHub
    * CodeCov: then add repo token to tox.ini
    * CircleCI
    * Appveyor?
    * Sentry

* Setup Slack integrations for

    * CircleCI
    * Appveyor
    * Sentry

* Git init, commit, push
* Verify

    ** CI builds pass
    ** Coverage is pushed
    ** Verify deliberate exception (/exception) shows up in Sentry
    ** Failed builds show up in Slack

* Update this readme


