# pylint: disable=invalid-name


"""Djaizz PreTrainedKerasImageNetClassifier model class."""


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Create Djaizz PreTrainedKerasImageNetClassifier model class."""

    dependencies = (('AIModel', '0001_AIModel'),)

    operations = (
        migrations.CreateModel(
            name='PreTrainedKerasImageNetClassifier',

            fields=(
                ('aimodel_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_keras_imagenet_classifiers',
                    serialize=False,
                    to='AIModel.aimodel')),

                ('artifact_global_url',
                 models.CharField(
                    blank=True,
                    db_index=True,
                    default=None,
                    help_text='Model Artifact Global URL',
                    max_length=255,
                    null=True,
                    unique=True,
                    verbose_name='Model Artifact Global URL')),

                ('artifact_local_path',
                 models.CharField(
                    blank=True,
                    db_index=True,
                    default=None,
                    help_text='Model Artifact Local Path',
                    max_length=255,
                    null=True,
                    verbose_name='Model Artifact Local Path')),

                ('loader_module_and_qualname',
                 models.CharField(
                    db_index=True,
                    default=None,
                    help_text=('Pre-Trained ML Model Loader '
                               '(module.dot.qualname)'),
                    max_length=255,
                    verbose_name=('Pre-Trained ML Model Loader '
                                  '(module.dot.qualname)'))),

                ('preprocessor_module_and_qualname',
                 models.CharField(
                    db_index=True,
                    default=None,
                    help_text='Preprocessor (module.dot.qualname)',
                    max_length=255,
                    verbose_name='Preprocessor (module.dot.qualname)'))
            ),

            options={
                'verbose_name': 'Pre-Trained Keras ImageNet Classifier',
                'verbose_name_plural':
                    'Pre-Trained Keras ImageNet Classifiers',
                'db_table': 'AIModel_PreTrainedKerasImageNetClassifier',
                'abstract': False,
                'default_related_name':
                    'pretrained_keras_imagenet_classifiers',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.aimodel',)
        ),
    )
