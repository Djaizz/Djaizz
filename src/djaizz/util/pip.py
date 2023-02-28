"""Djaizz PIP-related Utilities."""


from sys import version_info
from typing import Optional
from typing import Dict, List   # Py3.9+: use generic types

from pip._internal.operations.freeze import (   # pylint: disable=import-error
    freeze)

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence   # pylint: disable=ungrouped-imports


__all__: Sequence[str] = ('get_python_dependencies',)


def get_python_dependencies() -> Dict[str, Optional[str]]:
    """Get Python Dependencies."""
    deps_and_vers_dict: Dict[str, Optional[str]] = {}

    for dep_and_ver_str in freeze(requirement=None,
                                  local_only=False,
                                  user_only=False,
                                  paths=None,
                                  isolated=False,
                                  exclude_editable=False,
                                  skip=()):
        dep_and_ver_tuple: List[str] = dep_and_ver_str.split('==')

        if len(dep_and_ver_tuple) == 2:
            deps_and_vers_dict[dep_and_ver_tuple[0]] = dep_and_ver_tuple[1]

        else:
            assert len(dep_and_ver_tuple) == 1, f'*** {dep_and_ver_tuple} ***'
            deps_and_vers_dict[dep_and_ver_tuple[0]] = None

    return deps_and_vers_dict
