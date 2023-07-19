"""Set up Google Cloud AI Service models."""


from djaizz.model.models.cloud_ai_svc.google import (
    GoogleTranslate,
)


def run():
    """Run this script."""
    try:
        print(GoogleTranslate.objects
              .get_or_create(name='Google-Translate')[0])

    except Exception as err:   # pylint: disable=broad-except
        print(f'{GoogleTranslate.__name__} model not set up: {err}')
