"""DjAI base AIModel class & its subclasses."""


from collections.abc import Sequence

from .base import AIModel
from .ml import SKLModel


__all__: Sequence[str] = (
    'AIModel',
    'SKLModel',
)
