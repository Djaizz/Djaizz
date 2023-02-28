"""Djaizz Pre-Trained Hugging Face Transformer Model class."""


from sys import version_info

from djaizz.util import PGSQL_IDENTIFIER_MAX_LEN
from djaizz.model.apps import DjaizzModelModuleConfig

from ..base import _PreTrainedMLModelABC

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('PreTrainedHuggingFaceTransformer',)


class PreTrainedHuggingFaceTransformer(_PreTrainedMLModelABC):
    # pylint: disable=abstract-method
    """Djaizz Pre-Trained Hugging Face Transformer Model class."""

    class Meta(_PreTrainedMLModelABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        verbose_name: str = 'Pre-Trained Hugging Face Transformer'
        verbose_name_plural: str = 'Pre-Trained Hugging Face Transformers'

        db_table: str = (f'{DjaizzModelModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name: str = 'pretrained_hugging_face_transformers'
