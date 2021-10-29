"""DjAI JSON DataSet classes."""


from collections.abc import Sequence
from json.decoder import JSONDecoder   # pylint: disable=import-error

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.json import JSONField

from djai.data.apps import DjAIDataModuleConfig
from djai.util import PGSQL_IDENTIFIER_MAX_LEN

from .base import DataSet


__all__: Sequence[str] = ('InDBJSONDataSet',)


class InDBJSONDataSet(DataSet):
    """DjAI In-Database JSON DataSet class."""

    in_db_json: JSONField = \
        JSONField(
            verbose_name='In-Database JSON Data Content',
            help_text='In-Database JSON Data Content',

            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,

            null=True,
            blank=True,
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

    class Meta(DataSet.Meta):   # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        verbose_name: str = 'In-Database JSON Data Set'
        verbose_name_plural: str = 'In-Database JSON Data Sets'

        db_table: str = (f'{DjAIDataModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'in_db_json_data_sets'
