"""Djaizz Machine Learning Model base classes."""


from sys import version_info
from typing import Dict   # Py3.9+: use generic types
from typing import Any

from django.db.models.fields import CharField

from djaizz.util import import_obj

from ..base import _AIModelWithArtifactFilesABC

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('_PreTrainedMLModelABC',)


class _PreTrainedMLModelABC(_AIModelWithArtifactFilesABC):
    # pylint: disable=abstract-method
    loader_module_and_qualname: CharField = \
        CharField(
            verbose_name='Pre-Trained ML Model Loader (module.dot.qualname)',
            help_text='Pre-Trained ML Model Loader (module.dot.qualname)',

            max_length=255,

            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages={},
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta(_AIModelWithArtifactFilesABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True

    @property
    def loader(self) -> callable:
        """Loader method to load the Model's native object."""
        return import_obj(self.loader_module_and_qualname)

    @property
    def init_params(self) -> Dict[str, Any]:
        """Extract initialization parameters from in-database params JSON."""
        return ({} if self.params is None else self.params).get('__init__', {})

    def load(self) -> None:
        if not self.native_obj:
            self.native_obj = self.loader(**self.init_params)
