"""Djaizz Utilities."""


from importlib import import_module
from sys import version_info
from typing import Any

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence   # pylint: disable=ungrouped-imports


__all__: Sequence[str] = (
    'PGSQL_IDENTIFIER_MAX_LEN',
    'dir_path_with_end_slash',
    'full_qual_name',
    'import_obj',
)


PGSQL_IDENTIFIER_MAX_LEN: int = 63


def dir_path_with_end_slash(path: str) -> str:
    """Add an ending slash to a directory path if necessary."""
    return path if path.endswith('/') else f'{path}/'


def full_qual_name(obj: Any) -> str:
    """full.module.path.and.object.name to fully identify an object."""
    return f'{obj.__module__}.{obj.__qualname__}'


def import_obj(module_and_qualname: str) -> Any:
    """Import an objects by its full.module.path.and.object.name string."""
    module_name, qualname = module_and_qualname.rsplit(sep='.', maxsplit=1)
    return getattr(import_module(module_name), qualname)
