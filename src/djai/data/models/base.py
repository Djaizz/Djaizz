"""DjAI base DataSchema & DataSet classes."""


from collections.abc import Sequence
from json.decoder import JSONDecoder   # pylint: disable=import-error

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.deletion import SET_NULL
from django.db.models.fields.json import JSONField
from django.db.models.fields.related import ForeignKey

from polymorphic.models import PolymorphicModel

from djai.data.apps import DjAIDataModuleConfig
from djai.util import PGSQL_IDENTIFIER_MAX_LEN
from djai.util.models import _ModelWithUUIDPKAndOptionalUniqueNameAndTimestampsABC   # noqa: E501


__all__: Sequence[str] = 'DataSchema', 'DataSet'


class DataSchema(PolymorphicModel,
                 _ModelWithUUIDPKAndOptionalUniqueNameAndTimestampsABC):
    """DjAI DataSchema class."""

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
            # error_messages=None,
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

        db_table: str = (f'{DjAIDataModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'data_schemas'


class DataSet(PolymorphicModel,
              _ModelWithUUIDPKAndOptionalUniqueNameAndTimestampsABC):
    """DjAI base DataSet class."""

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
            # error_messages=None,
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

        db_table: str = (f'{DjAIDataModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'data_sets'
