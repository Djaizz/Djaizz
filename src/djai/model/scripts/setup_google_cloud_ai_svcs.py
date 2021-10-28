"""Set up Google Cloud AI Service models."""


from djai.model.models.cloud_ai_svc.google import (
    GoogleTranslate,
)


def run():
    """Run this script."""
    print(GoogleTranslate.objects.get_or_create(name='Google-Translate')[0])
