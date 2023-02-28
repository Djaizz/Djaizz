# pylint: disable=invalid-name


"""Djaizz CloudAIService model class."""


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Create Djaizz CloudAIService model class."""

    dependencies = (('AIModel', '0003_PreTrainedHuggingFaceTransformers'),)

    operations = (
        migrations.CreateModel(
            name='CloudAIService',

            fields=(
                ('aimodel_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='cloud_ai_svcs',
                    serialize=False,
                    to='AIModel.aimodel')),
            ),

            options={
                'verbose_name': 'Cloud AI Service',
                'verbose_name_plural': 'Cloud AI Services',
                'db_table': 'AIModel_CloudAIService',
                'abstract': False,
                'default_related_name': 'cloud_ai_svcs',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.aimodel',)
        ),
    )
