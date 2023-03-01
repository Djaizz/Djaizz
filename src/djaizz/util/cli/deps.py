"""Djaizz Dependencies."""


from importlib.metadata import version
from pprint import pprint

import click
# import corsheaders
import django_plotly_dash
import numpy


@click.command(name='capped-deps',
               cls=click.Command,
               context_settings=None,
               help=('Djaizz Capped Dependencies CLI >>>'),
               epilog=('^^^ Djaizz Capped Dependencies CLI'),
               short_help='Djaizz Capped Dependencies',
               options_metavar='',
               add_help_option=True,
               hidden=False,
               deprecated=False)
def capped_deps():
    """List Djaizz's Capped Dependencies' Versions."""
    pprint(object={
           # 'Django-Bootstrap-Components': ...,
           'Django-CORS-Headers': version(distribution_name='Django-CORS-Headers'),  # noqa: E501
           'Django-Plotly-Dash': django_plotly_dash.__version__,
           'NumPy': numpy.__version__,
           },
           indent=2, width=80, depth=None, compact=False, sort_dicts=False,
           underscore_numbers=True)
