"""Djaizz Data URLs."""


from sys import version_info

from django.urls.resolvers import URLPattern

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('urlpatterns',)


urlpatterns: Sequence[URLPattern] = (
)
