"""Djaizz URLs."""


from sys import version_info

from django.urls.conf import include, path
from django.urls.resolvers import URLPattern

from .data import urls as data_urls
from .model import urls as model_urls

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('urlpatterns',)


urlpatterns: Sequence[URLPattern] = (
    path(route='data/',
         view=include(data_urls), kwargs=None, name=None),
    path(route='data-mgmt/',
         view=include(data_urls), kwargs=None, name=None),

    path(route='model/',
         view=include(model_urls), kwargs=None, name=None),
    path(route='models/',
         view=include(model_urls), kwargs=None, name=None),
    path(route='modeling/',
         view=include(model_urls), kwargs=None, name=None),
)
