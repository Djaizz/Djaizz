"""DjAI Torch Deep Learning Model classes."""


import sys

from .base import TorchModel

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'TorchModel',
)
