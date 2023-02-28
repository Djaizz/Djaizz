# pylint: disable=invalid-name


"""Djaizz PreTrainedHuggingFaceTransformer model classes."""


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Create Djaizz PreTrainedHuggingFaceTransformer model classes."""

    dependencies = (('AIModel', '0002_PreTrainedKerasImageNetClassifier'),)

    operations = (
        migrations.CreateModel(
            name='PreTrainedHuggingFaceTransformer',

            fields=(
                ('aimodel_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_hugging_face_transformers',
                    serialize=False, to='AIModel.aimodel')),

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
                                  '(module.dot.qualname)')))
            ),

            options={
                'verbose_name': 'Pre-Trained Hugging Face Transformer',
                'verbose_name_plural': 'Pre-Trained Hugging Face Transformers',
                'db_table': 'AIModel_PreTrainedHuggingFaceTransformer',
                'abstract': False,
                'default_related_name': 'pretrained_hugging_face_transformers',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.aimodel',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceAudioClassifier',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_hugging_face_audio_classifiers',
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name': 'Pre-Trained Hugging Face Audio Classifier',
                'verbose_name_plural':
                    'Pre-Trained Hugging Face Audio Classifiers',
                'db_table': 'AIModel_PreTrainedHuggingFaceAudioClassifier',
                'abstract': False,
                'default_related_name':
                    'pretrained_hugging_face_audio_classifiers',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceImageClassifier',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_hugging_face_image_classifiers',
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name': 'Pre-Trained Hugging Face Image Classifier',
                'verbose_name_plural':
                    'Pre-Trained Hugging Face Image Classifiers',
                'db_table': 'AIModel_PreTrainedHuggingFaceImageClassifier',
                'abstract': False,
                'default_related_name':
                    'pretrained_hugging_face_image_classifiers',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceMaskFiller',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_hugging_face_mask_fillers',
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name': 'Pre-Trained Hugging Face Mask Filler',
                'verbose_name_plural': 'Pre-Trained Hugging Face Mask Fillers',
                'db_table': 'AIModel_PreTrainedHuggingFaceMaskFiller',
                'abstract': False,
                'default_related_name': 'pretrained_hugging_face_mask_fillers',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceObjectDetector',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_hugging_face_object_detectors',
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name': 'Pre-Trained Hugging Face Object Detector',
                'verbose_name_plural':
                    'Pre-Trained Hugging Face Object Detectors',
                'db_table': 'AIModel_PreTrainedHuggingFaceObjectDetector',
                'abstract': False,
                'default_related_name':
                    'pretrained_hugging_face_object_detectors',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceQuestionAnswerer',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_hugging_face_question_answerers',
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name': 'Pre-Trained Hugging Face Question Answerer',
                'verbose_name_plural':
                    'Pre-Trained Hugging Face Question Answerers',
                'db_table': 'AIModel_PreTrainedHuggingFaceQuestionAnswerer',
                'abstract': False,
                'default_related_name':
                    'pretrained_hugging_face_question_answerers',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',),
        ),
        migrations.CreateModel(
            name='PreTrainedHuggingFaceSpeechRecognizer',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_hugging_face_speech_recognizers',
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name': 'Pre-Trained Hugging Face Speech Recognizer',
                'verbose_name_plural':
                    'Pre-Trained Hugging Face Speech Recognizers',
                'db_table': 'AIModel_PreTrainedHuggingFaceSpeechRecognizer',
                'abstract': False,
                'default_related_name':
                    'pretrained_hugging_face_speech_recognizers',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceTableQuestionAnswerer',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name=('pretrained_hugging_face_'
                                  'table_question_answerers'),
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name':
                    'Pre-Trained Hugging Face Table Question Answerer',
                'verbose_name_plural':
                    'Pre-Trained Hugging Face Table Question Answerers',
                'db_table':
                    'AIModel_PreTrainedHuggingFaceTableQuestionAnswerer',
                'abstract': False,
                'default_related_name':
                    'pretrained_hugging_face_table_question_answerers',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceText2TextGenerator',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name=('pretrained_hugging_face_'
                                  'text2text_generators'),
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name':
                    'Pre-Trained Hugging Face Text-to-Text Generator',
                'verbose_name_plural':
                    'Pre-Trained Hugging Face Text-to-Text Generators',
                'db_table': 'AIModel_PreTrainedHuggingFaceText2TextGenerator',
                'abstract': False,
                'default_related_name':
                    'pretrained_hugging_face_text2text_generators',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceTextClassifier',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_hugging_face_text_classifiers',
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name': 'Pre-Trained Hugging Face Text Classifier',
                'verbose_name_plural':
                    'Pre-Trained Hugging Face Text Classifiers',
                'db_table': 'AIModel_PreTrainedHuggingFaceTextClassifier',
                'abstract': False,
                'default_related_name':
                    'pretrained_hugging_face_text_classifiers',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceTextGenerator',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_hugging_face_text_generators',
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name': 'Pre-Trained Hugging Face Text Generator',
                'verbose_name_plural':
                    'Pre-Trained Hugging Face Text Generators',
                'db_table': 'AIModel_PreTrainedHuggingFaceTextGenerator',
                'abstract': False,
                'default_related_name':
                    'pretrained_hugging_face_text_generators',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceTextSummarizer',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_hugging_face_text_summarizers',
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name': 'Pre-Trained Hugging Face Text Summarizer',
                'verbose_name_plural':
                    'Pre-Trained Hugging Face Text Summarizers',
                'db_table': 'AIModel_PreTrainedHuggingFaceTextSummarizer',
                'abstract': False,
                'default_related_name':
                    'pretrained_hugging_face_text_summarizers',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceTokenClassifier',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_hugging_face_token_classifiers',
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name': 'Pre-Trained Hugging Face Token Classifier',
                'verbose_name_plural':
                    'Pre-Trained Hugging Face Token Classifiers',
                'db_table': 'AIModel_PreTrainedHuggingFaceTokenClassifier',
                'abstract': False,
                'default_related_name':
                    'pretrained_hugging_face_token_classifiers',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceTranslator',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='pretrained_hugging_face_translators',
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name': 'Pre-Trained Hugging Face Translator',
                'verbose_name_plural': 'Pre-Trained Hugging Face Translators',
                'db_table': 'AIModel_PreTrainedHuggingFaceTranslator',
                'abstract': False,
                'default_related_name': 'pretrained_hugging_face_translators',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        ),

        migrations.CreateModel(
            name='PreTrainedHuggingFaceZeroShotClassifier',

            fields=(
                ('pretrainedhuggingfacetransformer_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name=('pretrained_hugging_face_'
                                  'zero_shot_classifiers'),
                    serialize=False,
                    to='AIModel.pretrainedhuggingfacetransformer')),
            ),

            options={
                'verbose_name':
                    'Pre-Trained Hugging Face Zero-Shot Classifier',
                'verbose_name_plural':
                    'Pre-Trained Hugging Face Zero-Shot Classifiers',
                'db_table': 'AIModel_PreTrainedHuggingFaceZeroShotClassifier',
                'abstract': False,
                'default_related_name':
                    'pretrained_hugging_face_zero_shot_classifiers',
                'base_manager_name': 'objects'
            },

            bases=('AIModel.pretrainedhuggingfacetransformer',)
        )
    )
