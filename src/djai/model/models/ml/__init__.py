"""DjAI Machine Learning Model classes."""


from collections.abc import Sequence

from .skl import SKLModel

from .keras import (
    KerasModel,

    PreTrainedKerasImageNetClassifier,
)

from .torch import (
    TorchModel,
)

from .hugging_face import (
    PreTrainedHuggingFaceTransformer,

    PreTrainedHuggingFaceAudioClassifier,
    PreTrainedHuggingFaceImageClassifier,
    PreTrainedHuggingFaceMaskFiller,
    PreTrainedHuggingFaceObjectDetector,
    PreTrainedHuggingFaceQuestionAnswerer,
    PreTrainedHuggingFaceSpeechRecognizer,
    PreTrainedHuggingFaceTableQuestionAnswerer,
    PreTrainedHuggingFaceTextClassifier,
    PreTrainedHuggingFaceTextGenerator,
    PreTrainedHuggingFaceText2TextGenerator,
    PreTrainedHuggingFaceTextSummarizer,
    PreTrainedHuggingFaceTokenClassifier,
    PreTrainedHuggingFaceTranslator,
    PreTrainedHuggingFaceZeroShotClassifier,
)


__all__: Sequence[str] = (
    'SKLModel',

    'KerasModel',
    'PreTrainedKerasImageNetClassifier',

    'TorchModel',

    'PreTrainedHuggingFaceTransformer',
    'PreTrainedHuggingFaceAudioClassifier',
    'PreTrainedHuggingFaceImageClassifier',
    'PreTrainedHuggingFaceMaskFiller',
    'PreTrainedHuggingFaceObjectDetector',
    'PreTrainedHuggingFaceQuestionAnswerer',
    'PreTrainedHuggingFaceSpeechRecognizer',
    'PreTrainedHuggingFaceTableQuestionAnswerer',
    'PreTrainedHuggingFaceTextClassifier',
    'PreTrainedHuggingFaceTextGenerator',
    'PreTrainedHuggingFaceText2TextGenerator',
    'PreTrainedHuggingFaceTextSummarizer',
    'PreTrainedHuggingFaceTokenClassifier',
    'PreTrainedHuggingFaceTranslator',
    'PreTrainedHuggingFaceZeroShotClassifier',
)
