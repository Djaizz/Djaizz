"""DjAI Data URLs."""


import sys

from django.urls.resolvers import URLPattern

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('urlpatterns',)


urlpatterns: Sequence[URLPattern] = (
)
