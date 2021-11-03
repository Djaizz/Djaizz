"""DjAI TensorFlow.Keras Deep Learning Model classes."""


import sys

from .base import KerasModel

from .pre_trained import (
    PreTrainedKerasImageNetClassifier,
)

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'KerasModel',
    'PreTrainedKerasImageNetClassifier',
)
