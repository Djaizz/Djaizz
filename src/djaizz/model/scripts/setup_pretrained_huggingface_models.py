"""Set up pre-trained Hugging Face models."""


from transformers.pipelines import pipeline

from djaizz.model.models.ml.hugging_face import (
    PreTrainedHuggingFaceAudioClassifier,
    PreTrainedHuggingFaceImageClassifier,
    PreTrainedHuggingFaceMaskFiller,
    PreTrainedHuggingFaceObjectDetector,
    PreTrainedHuggingFaceQuestionAnswerer,
    PreTrainedHuggingFaceSpeechRecognizer,
    PreTrainedHuggingFaceTableQuestionAnswerer,
    PreTrainedHuggingFaceTextClassifier,
    PreTrainedHuggingFaceTextGenerator,
    PreTrainedHuggingFaceText2TextGenerator,
    PreTrainedHuggingFaceTextSummarizer,
    PreTrainedHuggingFaceTokenClassifier,
    PreTrainedHuggingFaceTranslator,
    PreTrainedHuggingFaceZeroShotClassifier,
)
from djaizz.util import full_qual_name


def run():   # noqa: MC0001
    """Run this script."""
    try:
        print(
            PreTrainedHuggingFaceAudioClassifier.objects.update_or_create(
                name='PreTrained-HuggingFace-Audio-Classifier',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='audio-classification',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceAudioClassifier.__name__} model '
              f'not set up: {err}')

    try:
        print(
            PreTrainedHuggingFaceImageClassifier.objects.update_or_create(
                name='PreTrained-HuggingFace-Image-Classifier',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='image-classification',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceImageClassifier.__name__} model '
              f'not set up: {err}')

    try:
        print(
            PreTrainedHuggingFaceMaskFiller.objects.update_or_create(
                name='PreTrained-HuggingFace-Mask-Filler',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='fill-mask',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceMaskFiller.__name__} model '
              f'not set up: {err}')

    try:
        print(
            PreTrainedHuggingFaceObjectDetector.objects.update_or_create(
                name='PreTrained-HuggingFace-Object-Detector',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='object-detection',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceObjectDetector.__name__} model '
              f'not set up: {err}')

    try:
        print(
            PreTrainedHuggingFaceQuestionAnswerer.objects.update_or_create(
                name='PreTrained-HuggingFace-Question-Answerer',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='question-answering',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceQuestionAnswerer.__name__} model '
              f'not set up: {err}')

    try:
        print(
            PreTrainedHuggingFaceSpeechRecognizer.objects.update_or_create(
                name='PreTrained-HuggingFace-Speech-Recognizer',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task=('automatic-'
                                                    'speech-recognition'),
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceSpeechRecognizer.__name__} model '
              f'not set up: {err}')

    try:
        print(
            PreTrainedHuggingFaceTableQuestionAnswerer.objects.update_or_create(   # noqa: E501
                name='PreTrained-HuggingFace-Table-Question-Answerer',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='table-question-answering',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceTableQuestionAnswerer.__name__} model '
              f'not set up: {err}')

    try:
        print(
            PreTrainedHuggingFaceTextClassifier.objects.update_or_create(
                name='PreTrained-HuggingFace-Text-Classifier',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='text-classification',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
        print(
            PreTrainedHuggingFaceTextClassifier.objects.update_or_create(
                name='PreTrained-HuggingFace-Sentiment-Analyzer',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='sentiment-analysis',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceTextClassifier.__name__} model '
              f'not set up: {err}')

    try:
        print(
            PreTrainedHuggingFaceTextGenerator.objects.update_or_create(
                name='PreTrained-HuggingFace-Text-Generator',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='text-generation',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceTextGenerator.__name__} model '
              f'not set up: {err}')

    try:
        print(
            PreTrainedHuggingFaceText2TextGenerator.objects.update_or_create(
                name='PreTrained-HuggingFace-Text2Text-Generator',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='text2text-generation',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceText2TextGenerator.__name__} model '
              f'not set up: {err}')

    try:
        print(
            PreTrainedHuggingFaceTextSummarizer.objects.update_or_create(
                name='PreTrained-HuggingFace-Text-Summarizer',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='summarization',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceTextSummarizer.__name__} model '
              f'not set up: {err}')

    try:
        print(
            PreTrainedHuggingFaceTokenClassifier.objects.update_or_create(
                name='PreTrained-HuggingFace-Token-Classifier',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='token-classification',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
        print(
            PreTrainedHuggingFaceTokenClassifier.objects.update_or_create(
                name='PreTrained-HuggingFace-Named-Entity-Recognizer',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='ner',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceTokenClassifier.__name__} model '
              f'not set up: {err}')

    for translation_model_name in ('facebook/m2m100_418M',
                                   'facebook/m2m100_1.2B',
                                   'facebook/mbart-large-50-one-to-many-mmt',
                                   'facebook/mbart-large-50-many-to-many-mmt'):
        try:
            print(
                PreTrainedHuggingFaceTranslator.objects.update_or_create(
                    name=('PreTrained-HuggingFace-Translator-' +
                          translation_model_name.replace('/', '-')),
                    defaults=dict(
                        loader_module_and_qualname=full_qual_name(pipeline),
                        artifact_global_url=None,
                        artifact_local_path=None,
                        params=dict(__init__=dict(task='translation',
                                                  model=translation_model_name,
                                                  config=None,
                                                  tokenizer=None,
                                                  feature_extractor=None,
                                                  framework=None,
                                                  revision=None,
                                                  use_fast=True,
                                                  use_auth_token=None,
                                                  model_kwargs={}))))[0])
        except Exception as err:   # pylint: disable=broad-except
            print(f'{PreTrainedHuggingFaceTranslator.__name__} model '
                  f'not set up: {err}')

    try:
        print(
            PreTrainedHuggingFaceZeroShotClassifier.objects.update_or_create(
                name='PreTrained-HuggingFace-Zero-Shot-Classifier',
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(pipeline),
                    artifact_global_url=None,
                    artifact_local_path=None,
                    params=dict(__init__=dict(task='zero-shot-classification',
                                              model=None,
                                              config=None,
                                              tokenizer=None,
                                              feature_extractor=None,
                                              framework=None,
                                              revision=None,
                                              use_fast=True,
                                              use_auth_token=None,
                                              model_kwargs={}))))[0])
    except Exception as err:   # pylint: disable=broad-except
        print(f'{PreTrainedHuggingFaceZeroShotClassifier.__name__} model '
              f'not set up: {err}')
