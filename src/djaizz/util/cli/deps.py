"""Djaizz Dependencies."""


from importlib.metadata import version
from pprint import pprint
from typing import Sequence  # Py3.9+: use built-ins/collections.abc

import click


CAPPED_DEPS: Sequence[str] = ('Channels',
                              'Daphne',
                              'Dash-Bootstrap-Components',
                              'Django-CORS-Headers',
                              'Django-Plotly-Dash',
                              'H11',
                              'NumPy',
                              'Quart')


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
    pprint(object={dep_name: version(distribution_name=dep_name)
                   for dep_name in CAPPED_DEPS},
           indent=2, width=80, depth=None, compact=False, sort_dicts=False,
           underscore_numbers=True)
