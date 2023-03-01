"""Djaizz CLI."""


import click

from .aws_eb import djaizz_aws_eb
from .deps import capped_deps


@click.group(name='djaizz',
             cls=click.Group,
             commands={'aws-eb': djaizz_aws_eb,
                       'capped-deps': capped_deps
                       },
             invoke_without_command=False,
             no_args_is_help=True,
             subcommand_metavar='DJAI_SUB_COMMAND',
             chain=False,
             help='Djaizz CLI >>>',
             epilog='^^^ Djaizz CLI',
             short_help='Djaizz CLI',
             options_metavar='[OPTIONS]',
             add_help_option=True,
             hidden=False,
             deprecated=False)
def djaizz():
    """Trigger Djaizz from CLI."""
