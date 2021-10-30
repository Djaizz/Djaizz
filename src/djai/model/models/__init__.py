"""DjAI base AIModel class & its subclasses."""


import sys
if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence

from .base import AIModel

from .cloud_ai_svc import (
    CloudAIService,

    GoogleTranslate,
)

from .ml import (
    SKLModel,

    KerasModel,
    PreTrainedKerasImageNetClassifier,

    TorchModel,

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

    'CloudAIService',

    'GoogleTranslate',

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
