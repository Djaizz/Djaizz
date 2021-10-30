"""DjAI Model URLs."""


import sys
if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence

from django.urls.conf import path
from django.urls.resolvers import URLPattern

from djai.model.views import gradio_ui


__all__: Sequence[str] = ('urlpatterns',)


urlpatterns: Sequence[URLPattern] = (
    path(route='<str:model_class_or_instance_name_or_uuid>/gradio/',
         view=gradio_ui, kwargs=None, name=None),
)
