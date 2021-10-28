"""DjAI Pre-Trained TensorFlow.Keras Vision Model classes."""


from collections.abc import Sequence

from .image_classification import PreTrainedKerasImageNetClassifier


__all__: Sequence[str] = (
    'PreTrainedKerasImageNetClassifier',
)
