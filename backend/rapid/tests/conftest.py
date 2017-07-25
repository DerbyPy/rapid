from __future__ import absolute_import
from __future__ import unicode_literals

# important to import from .cli so that the commands get attached
from rapid.cli import Rapid


def pytest_configure(config):
    Rapid.testing_prep()
