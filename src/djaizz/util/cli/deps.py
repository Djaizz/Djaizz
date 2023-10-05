"""Djaizz Dependencies."""


from collections.abc import Sequence
from importlib.metadata import version
from pprint import pprint
from typing import LiteralString

import click


CAPPED_DEPS: Sequence[LiteralString] = ('Dash',
                                        'GUnicorn',
                                        'H11',
                                        'LangChain',
                                        'NumPy',
                                        'OpenAI',
                                        'Pandas',
                                        'Pillow',
                                        'Pydantic',
                                        'Starlette',
                                        'TensorFlow',
                                        'TensorFlow-Text',
                                        'Torch',
                                        'TorchAudio',
                                        'TorchText',
                                        'TorchVision')


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
