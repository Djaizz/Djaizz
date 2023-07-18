"""Djaizz Cloud AI Service model classes."""


from sys import version_info

from .base import CloudAIService

from .google import (
    GoogleTranslate,
)

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'CloudAIService',

    'GoogleTranslate',
)
