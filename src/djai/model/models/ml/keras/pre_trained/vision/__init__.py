"""DjAI Pre-Trained TensorFlow.Keras Vision Model classes."""


import sys

from .image_classification import PreTrainedKerasImageNetClassifier

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'PreTrainedKerasImageNetClassifier',
)
