"""Djaizz Pre-Trained Hugging Face Model classes."""


from sys import version_info

from .base import PreTrainedHuggingFaceTransformer
from .audio_classification import PreTrainedHuggingFaceAudioClassifier
from .image_classification import PreTrainedHuggingFaceImageClassifier
from .mask_filling import PreTrainedHuggingFaceMaskFiller
from .object_detection import PreTrainedHuggingFaceObjectDetector
from .question_answering import PreTrainedHuggingFaceQuestionAnswerer
from .speech_recognition import PreTrainedHuggingFaceSpeechRecognizer
from .table_question_answering import (
    PreTrainedHuggingFaceTableQuestionAnswerer)
from .text_classification import PreTrainedHuggingFaceTextClassifier
from .text_generation import PreTrainedHuggingFaceTextGenerator
from .text2text_generation import PreTrainedHuggingFaceText2TextGenerator
from .text_summarization import PreTrainedHuggingFaceTextSummarizer
from .token_classification import PreTrainedHuggingFaceTokenClassifier
from .translation import PreTrainedHuggingFaceTranslator
from .zero_shot_classification import PreTrainedHuggingFaceZeroShotClassifier

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
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
