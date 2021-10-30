"""DjAI Model Public API."""


import sys
if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence

from djai.model.models import (
    AIModel,

    CloudAIService,

    GoogleTranslate,

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
