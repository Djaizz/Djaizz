"""DjAI Cloud AI Service model classes."""


import sys
if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence

from .base import CloudAIService

from .google import (
    GoogleTranslate,
)


__all__: Sequence[str] = (
    'CloudAIService',

    'GoogleTranslate',
)
