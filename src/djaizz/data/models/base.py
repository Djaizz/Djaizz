"""Djaizz base DataSchema & DataSet classes."""


from abc import abstractmethod
from json.decoder import JSONDecoder   # pylint: disable=import-error
from sys import version_info
from typing import Any, Optional

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.deletion import SET_NULL
from django.db.models.fields import BooleanField, CharField
from django.db.models.fields.json import JSONField
from django.db.models.fields.related import ForeignKey

from polymorphic.models import PolymorphicModel

from djutil.models import _ModelWithUUIDPKAndOptionalUniqueNameAndTimestampsABC

from djaizz.data.apps import DjaizzDataModuleConfig
from djaizz.util import PGSQL_IDENTIFIER_MAX_LEN, dir_path_with_end_slash

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence   # pylint: disable=ungrouped-imports


__all__: Sequence[str] = 'DataSchema', 'DataSet', '_FileDataSetABC'


class DataSchema(PolymorphicModel,
                 _ModelWithUUIDPKAndOptionalUniqueNameAndTimestampsABC):
    """Djaizz DataSchema class."""

    specs = \
        JSONField(
            verbose_name='Data Schema Specifications',
            help_text='Data Schema Specifications',

            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,

            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=False,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages={},
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta(_ModelWithUUIDPKAndOptionalUniqueNameAndTimestampsABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        verbose_name: str = 'Data Schema'
        verbose_name_plural: str = 'Data Schemas'

        db_table: str = (f'{DjaizzDataModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'data_schemas'


class DataSet(PolymorphicModel,
              _ModelWithUUIDPKAndOptionalUniqueNameAndTimestampsABC):
    """Djaizz base DataSet class."""

    RELATED_NAME: str = 'data_sets'
    RELATED_QUERY_NAME: str = 'data_set'

    # pylint: disable=line-too-long
    schema: ForeignKey = \
        ForeignKey(
            verbose_name='Data Set Schema',
            help_text='Data Set Schema',

            # docs.djangoproject.com/en/dev/ref/models/fields/#arguments
            to=DataSchema,

            # docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.on_delete
            on_delete=SET_NULL,

            # docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.limit_choices_to
            limit_choices_to={},

            # docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.related_name
            related_name=RELATED_NAME,

            # docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.related_query_name
            related_query_name=RELATED_QUERY_NAME,

            # docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.to_field
            # to_field=...,

            # docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.db_constraint
            db_constraint=True,

            # docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.swappable
            swappable=True,

            null=True,
            blank=True,
            choices=None,
            db_column=None,
            db_index=True,   # implied
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages={},
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta(_ModelWithUUIDPKAndOptionalUniqueNameAndTimestampsABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        verbose_name: str = 'Data Set'
        verbose_name_plural: str = 'Data Sets'

        db_table: str = (f'{DjaizzDataModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'data_sets'


class _FileDataSetABC(DataSet):
    global_url: CharField = \
        CharField(
            verbose_name='Data Set Global URL',
            help_text='Data Set Global URL',

            max_length=255,

            null=True,
            blank=True,
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

    local_path: CharField = \
        CharField(
            verbose_name='Data Set Local Path',
            help_text='Data Set Local Path',

            max_length=255,

            null=True,
            blank=True,
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

    path_is_dir: BooleanField = \
        BooleanField(
            verbose_name='Data Set Path/URL is Directory?',
            help_text='Data Set Path/URL is Directory?',

            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=False,
            editable=True,
            # error_messages={},
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    native_obj: Optional[Any] = None

    class Meta(DataSet.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True

    @property
    def _path_repr(self) -> str:
        global_url_repr = ((dir_path_with_end_slash(self.global_url)
                            if self.path_is_dir
                            else self.global_url)
                           if self.global_url
                           else None)

        local_path_repr = ((dir_path_with_end_slash(self.local_path)
                            if self.path_is_dir
                            else self.local_path)
                           if self.local_path
                           else None)

        return ((f' @ {global_url_repr} (local: {local_path_repr})'
                 if local_path_repr
                 else f' @ {global_url_repr}')
                if global_url_repr
                else (f' @ {local_path_repr}'
                      if local_path_repr
                      else ''))

    def __str__(self) -> str:
        return f'{type(self).__name__} #{self.uuid}{self._path_repr}'

    @abstractmethod
    def load(self) -> None:
        """Load native data object from file artifact(s)."""
        raise NotImplementedError

    def unload(self) -> None:
        """Unload native data object to free up memory."""
        self.native_obj = None
