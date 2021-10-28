"""DjAI Cloud AI Service model classes."""


from collections.abc import Sequence


from .base import CloudAIService

from .google import (
    GoogleTranslate,
)


__all__: Sequence[str] = (
    'CloudAIService',

    'GoogleTranslate',
)
