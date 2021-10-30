"""DjAI Google Cloud AI Service model classes."""


import sys
if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence

from .translation import GoogleTranslate


__all__: Sequence[str] = (
    'GoogleTranslate',
)
