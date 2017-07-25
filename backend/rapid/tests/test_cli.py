from __future__ import absolute_import
from __future__ import unicode_literals

from keg.testing import CLIBase

from rapid.app import Rapid


class TestCLI(CLIBase):
    app_cls = Rapid
    cmd_name = 'hello'

    def test_hello(self):
        result = self.invoke()
        assert 'Hello World from Rapid!\n' == result.output

        result = self.invoke('--name', 'Foo')
        assert 'Hello Foo from Rapid!\n' == result.output
