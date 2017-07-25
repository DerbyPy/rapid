from __future__ import absolute_import
from __future__ import print_function

import logging

import click

from rapid.app import Rapid

log = logging.getLogger(__name__)


def cli_entry():
    Rapid.cli_run()


@Rapid.command('hello', short_help='Example command: say hello.')
@click.option('--name', default='World', help='The person to greet.')
def hello_world(name):
    click.echo('Hello {} from Rapid!'.format(name))


@Rapid.command('log', short_help='log some messages')
def logcmd():
    log.info('info log message')
    log.warning('warning log message')
    log.error('error log message')


if __name__ == '__main__':
    cli_entry()
