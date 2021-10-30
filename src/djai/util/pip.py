"""DjAI PIP-related Utilities."""


import sys
if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence

from typing import Dict, List   # Py3.9+: use generic types

from typing import Optional

from pip._internal.operations.freeze import freeze


__all__: Sequence[str] = ('get_python_dependencies',)


def get_python_dependencies() -> Dict[str, Optional[str]]:
    """Get Python Dependencies."""
    d: Dict[str, Optional[str]] = {}

    for deps_and_vers in freeze(requirement=None,
                                local_only=False,
                                user_only=False,
                                paths=None,
                                isolated=False,
                                exclude_editable=False,
                                skip=()):
        ls: List[str] = deps_and_vers.split('==')

        if len(ls) == 2:
            d[ls[0]] = ls[1]

        else:
            assert len(ls) == 1, f'*** {ls} ***'
            d[ls[0]] = None

    return d
