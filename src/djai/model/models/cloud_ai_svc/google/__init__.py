"""DjAI Google Cloud AI Service model classes."""


import sys

from .translation import GoogleTranslate

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'GoogleTranslate',
)
