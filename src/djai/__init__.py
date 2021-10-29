"""DjAI package."""


from collections.abc import Sequence
from importlib.metadata import version


__all__: Sequence[str] = ('__version__',)


__version__ = version(distribution_name='DjAI')
