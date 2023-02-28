"""Djaizz package."""


from importlib.metadata import version
from sys import version_info

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('__version__',)


__version__: str = version(distribution_name='Djaizz')
