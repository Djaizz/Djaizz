"""Djaizz Google Cloud AI Service model classes."""


from sys import version_info

from .translation import GoogleTranslate

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'GoogleTranslate',
)
