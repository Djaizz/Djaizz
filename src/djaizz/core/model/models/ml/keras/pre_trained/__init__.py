"""Djaizz Pre-Trained TensorFlow.Keras Model classes."""


from sys import version_info

from .vision import PreTrainedKerasImageNetClassifier

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'PreTrainedKerasImageNetClassifier',
)
