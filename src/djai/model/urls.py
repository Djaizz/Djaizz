"""DjAI Model URLs."""


from functools import partial
import sys

from django.urls.conf import path
from django.urls.resolvers import URLPattern

from djai.model.views import model_ui

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('urlpatterns',)


urlpatterns: Sequence[URLPattern] = (
    path(route='<str:model_class_or_instance_name_or_uuid>/dash/',
         view=partial(model_ui, ui_type='dash'),
         kwargs=None, name=None),

    path(route='<str:model_class_or_instance_name_or_uuid>/gradio/',
         view=partial(model_ui, ui_type='gradio'),
         kwargs=None, name=None),
)
