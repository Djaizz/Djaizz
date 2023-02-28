# pylint: disable=invalid-name


"""Djaizz GoogleTranslate model class."""


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Create Djaizz GoogleTranslate model class."""

    dependencies = (('AIModel', '0004_CloudAIService'),)

    operations = (
        migrations.CreateModel(
            name='GoogleTranslate',

            fields=(
                ('cloudaiservice_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='google_translate',
                    serialize=False,
                    to='AIModel.cloudaiservice')),
            ),

            options={
                'verbose_name': 'Google Translate',
                'verbose_name_plural': 'Google Translate',
                'db_table': 'AIModel_GoogleTranslate',
                'abstract': False,
                'default_related_name': 'google_translate',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.cloudaiservice',)
        ),
    )
