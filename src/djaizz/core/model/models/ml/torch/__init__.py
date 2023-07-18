"""Djaizz Torch Deep Learning Model classes."""


from sys import version_info

from .base import TorchModel

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'TorchModel',
)
