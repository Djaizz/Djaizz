"""DjAI base AIModel class & its subclasses."""


from collections.abc import Sequence

from .base import AIModel

from .ml import (
    SKLModel,

    KerasModel,
    PreTrainedKerasImageNetClassifier,

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
    'AIModel',

    'SKLModel',

    'KerasModel',
    'PreTrainedKerasImageNetClassifier',

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
