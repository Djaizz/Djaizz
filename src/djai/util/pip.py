"""DjAI PIP-related Utilities."""


from collections.abc import Sequence
from typing import Optional

from pip._internal.operations.freeze import freeze


__all__: Sequence[str] = ('get_python_dependencies',)


def get_python_dependencies() -> dict[str, Optional[str]]:
    """Get Python Dependencies."""
    d: dict[str, Optional[str]] = {}

    for deps_and_vers in freeze():
        ls: list[str] = deps_and_vers.split('==')

        if len(ls) == 2:
            d[ls[0]] = ls[1]

        else:
            assert len(ls) == 1, f'*** {ls} ***'
            d[ls[0]] = None

    return d
