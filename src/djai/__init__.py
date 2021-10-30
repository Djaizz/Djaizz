"""DjAI package."""


import sys
if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence

from importlib.metadata import version


__all__: Sequence[str] = ('__version__',)


__version__ = version(distribution_name='DjAI')
