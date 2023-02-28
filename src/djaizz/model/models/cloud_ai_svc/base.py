"""Djaizz Cloud AI Service base model class."""


from sys import version_info

from djaizz.model.apps import DjaizzModelModuleConfig
from djaizz.util import PGSQL_IDENTIFIER_MAX_LEN

from ..base import AIModel

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('CloudAIService',)


class CloudAIService(AIModel):   # pylint: disable=abstract-method
    """Djaizz Cloud AI Service model class."""

    class Meta(AIModel.Meta):   # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        verbose_name: str = 'Cloud AI Service'
        verbose_name_plural: str = 'Cloud AI Services'

        db_table: str = (f'{DjaizzModelModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name: str = 'cloud_ai_svcs'
