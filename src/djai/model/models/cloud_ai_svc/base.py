"""DjAI Cloud AI Service base model class."""


import sys

from djai.model.apps import DjAIModelModuleConfig
from djai.util import PGSQL_IDENTIFIER_MAX_LEN

from ..base import AIModel

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('CloudAIService',)


class CloudAIService(AIModel):   # pylint: disable=abstract-method
    """DjAI Cloud AI Service model class."""

    class Meta(AIModel.Meta):   # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        verbose_name: str = 'Cloud AI Service'
        verbose_name_plural: str = 'Cloud AI Services'

        db_table: str = (f'{DjAIModelModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name: str = 'cloud_ai_svcs'
