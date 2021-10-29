"""DjAI CLI."""


import click

from .aws_eb import djai_aws_eb


@click.group(name='djai',
             cls=click.Group,
             commands={'aws-eb': djai_aws_eb},
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
