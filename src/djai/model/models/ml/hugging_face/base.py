"""DjAI Pre-Trained Hugging Face Transformer Model class."""


from collections.abc import Sequence

from .....util import PGSQL_IDENTIFIER_MAX_LEN
from ....apps import DjAIModelModuleConfig
from ..base import _PreTrainedMLModelABC


__all__: Sequence[str] = ('PreTrainedHuggingFaceTransformer',)


class PreTrainedHuggingFaceTransformer(_PreTrainedMLModelABC):
    """DjAI Pre-Trained Hugging Face Transformer Model class."""

    class Meta(_PreTrainedMLModelABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        verbose_name: str = 'Pre-Trained Hugging Face Transformer'
        verbose_name_plural: str = 'Pre-Trained Hugging Face Transformers'

        db_table: str = (f'{DjAIModelModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name: str = 'pretrained_hugging_face_transformers'
