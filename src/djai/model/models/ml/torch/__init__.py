"""DjAI Torch Deep Learning Model classes."""


import sys
if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence

from .base import TorchModel


__all__: Sequence[str] = (
    'TorchModel',
)
