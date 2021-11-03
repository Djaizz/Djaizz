"""DjAI Cloud AI Service model classes."""


import sys

from .base import CloudAIService

from .google import (
    GoogleTranslate,
)

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'CloudAIService',

    'GoogleTranslate',
)
