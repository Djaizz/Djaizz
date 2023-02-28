# pylint: disable=invalid-name


"""Djaizz In-Database JSON DataSet class."""


import json.decoder

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Create Djaizz In-Database JSON DataSet class."""

    dependencies = (('AIData', '0001_DataSchema_DataSet'),)

    operations = (
        migrations.CreateModel(
            name='InDBJSONDataSet',

            fields=(
                ('dataset_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='in_db_json_data_sets',
                    serialize=False,
                    to='AIData.dataset')),

                ('in_db_json',
                 models.JSONField(
                    blank=True,
                    decoder=json.decoder.JSONDecoder,
                    default=None,
                    encoder=django.core.serializers.json.DjangoJSONEncoder,
                    help_text='In-Database JSON Data Content',
                    null=True,
                    verbose_name='In-Database JSON Data Content'))
            ),

            options={
                'verbose_name': 'In-Database JSON Data Set',
                'verbose_name_plural': 'In-Database JSON Data Sets',
                'db_table': 'AIData_InDBJSONDataSet',
                'abstract': False,
                'default_related_name': 'in_db_json_data_sets',
                'base_manager_name': 'objects'
            },

            bases=('AIData.dataset',)
        ),
    )
