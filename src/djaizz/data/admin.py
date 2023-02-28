"""Djaizz Data Admin."""


from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from silk.profiling.profiler import silk_profile

from djaizz.data.models import (
    DataSchema,
)


@register(DataSchema, site=site)
class DataSchemaAdmin(ModelAdmin):
    """DataSchema model admin."""

    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {DataSchema._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        """Silk-profiled change-form view."""
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=f'{__module__}: {DataSchema._meta.verbose_name_plural}')
    def changelist_view(self, *args, **kwargs):
        """Silk-profiled change-list view."""
        return super().changelist_view(*args, **kwargs)
