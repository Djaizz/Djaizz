"""Djaizz TensorFlow.Keras Deep Learning Model classes."""


from sys import version_info

from .base import KerasModel

from .pre_trained import (
    PreTrainedKerasImageNetClassifier,
)

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'KerasModel',
    'PreTrainedKerasImageNetClassifier',
)
