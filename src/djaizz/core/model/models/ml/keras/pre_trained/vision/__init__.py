"""Djaizz Pre-Trained TensorFlow.Keras Vision Model classes."""


from sys import version_info

from .image_classification import PreTrainedKerasImageNetClassifier

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'PreTrainedKerasImageNetClassifier',
)
