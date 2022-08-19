"""DjAI CLI."""


import click

from .aws_eb import djai_aws_eb
from .deps import capped_deps


@click.group(name='djai',
             cls=click.Group,
             commands={'aws-eb': djai_aws_eb,
                       'capped-deps': capped_deps},
             invoke_without_command=False,
             no_args_is_help=True,
             subcommand_metavar='DJAI_SUB_COMMAND',
             chain=False,
             help='DjAI CLI >>>',
             epilog='^^^ DjAI CLI',
             short_help='DjAI CLI',
             options_metavar='[OPTIONS]',
             add_help_option=True,
             hidden=False,
             deprecated=False)
def djai():
    """Trigger DjAI from CLI."""
