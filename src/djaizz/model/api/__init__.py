"""Djaizz Model Public API."""


from sys import version_info

from djaizz.model.models import (
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

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


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
