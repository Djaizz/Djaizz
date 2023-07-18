# pylint: disable=invalid-name


"""Djaizz base AIModel class."""


import json.decoder
import uuid

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

import model_utils.fields


class Migration(migrations.Migration):
    """Create Djaizz base AIModel class."""

    initial = True

    dependencies = (('contenttypes', '0002_remove_content_type_name'),)

    operations = (
        migrations.CreateModel(
            name='AIModel',

            fields=(
                ('polymorphic_ctype',
                 models.ForeignKey(
                    editable=False,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='polymorphic_aimodel.aimodel_set+',
                    to='contenttypes.contenttype')),

                ('uuid',
                 models.UUIDField(
                    db_index=True,
                    default=uuid.uuid4,
                    editable=False,
                    help_text='UUID',
                    primary_key=True,
                    serialize=False,
                    unique=True,
                    verbose_name='UUID')),

                ('name',
                 models.CharField(
                    blank=True,
                    db_index=True,
                    default=None,
                    help_text='(optional) Unique Name',
                    max_length=255,
                    null=True,
                    unique=True,
                    verbose_name='(optional) Unique Name')),

                ('params',
                 models.JSONField(
                    blank=True,
                    decoder=json.decoder.JSONDecoder,
                    default=None,
                    encoder=django.core.serializers.json.DjangoJSONEncoder,
                    help_text='Model Parameters',
                    null=True,
                    verbose_name='Model Parameters')),

                ('created',
                 model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='created')),

                ('modified',
                 model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now,
                    editable=False,
                    verbose_name='modified'))
            ),

            options={
                'verbose_name': 'AI Model',
                'verbose_name_plural': 'AI Models',
                'db_table': 'AIModel_AIModel',
                'ordering': ('name', '-modified'),
                'permissions': (),
                'get_latest_by': 'modified',
                'abstract': False,
                'managed': True,
                'proxy': False,
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'select_on_save': False,
                'default_related_name': 'ai_models',
                'required_db_features': (),
                'base_manager_name': 'objects',
                'default_manager_name': 'objects'
            }
        ),
    )
