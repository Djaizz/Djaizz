"""DjAI Dependencies."""


from importlib.metadata import version
from pprint import pprint

import click
# import corsheaders
# TODO: import django_plotly_dash
import gradio
import h11
import numpy
import starlette


@click.command(name='capped-deps',
               cls=click.Command,
               context_settings=None,
               help=('DjAI Capped Dependencies CLI >>>'),
               epilog=('^^^ DjAI Capped Dependencies CLI'),
               short_help='DjAI Capped Dependencies',
               options_metavar='',
               add_help_option=True,
               hidden=False,
               deprecated=False)
def capped_deps():
    """List DjAI's Capped Dependencies' Versions."""
    pprint(object={
           'CLICK': click.__version__,
           # 'Django-Bootstrap-Components': ...,
           'Django-CORS-Headers': version(distribution_name='Django-CORS-Headers'),   # noqa: E501
           # TODO: 'Django-Plotly-Dash': django_plotly_dash.__version__,
           'Gradio': gradio.__version__,
           'H11': h11.__version__,
           'NumPy': numpy.__version__,
           'Starlette': starlette.__version__,
           },
           indent=2, width=80, depth=None, compact=False, sort_dicts=False,
           underscore_numbers=True)
