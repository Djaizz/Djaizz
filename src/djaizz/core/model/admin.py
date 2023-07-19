"""Djaizz AI Model Admin classes."""


from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import site

from silk.profiling.profiler import silk_profile

from djaizz.model.models import (
    GoogleTranslate,
    PreTrainedKerasImageNetClassifier,
    PreTrainedHuggingFaceTransformer,
)


@register(GoogleTranslate, site=site)
class GoogleTranslateAdmin(ModelAdmin):
    """GoogleTranslate model admin."""

    show_full_result_count = False

    @silk_profile(name=f'{__module__}: {GoogleTranslate._meta.verbose_name}')
    def changeform_view(self, *args, **kwargs):
        """Silk-profiled change-form view."""
        return super().changeform_view(*args, **kwargs)

    @silk_profile(name=(f'{__module__}: '
                        f'{GoogleTranslate._meta.verbose_name_plural}'))
    def changelist_view(self, *args, **kwargs):
        """Silk-profiled change-list view."""
        return super().changelist_view(*args, **kwargs)


@register(PreTrainedKerasImageNetClassifier, site=site)
class PreTrainedKerasImageNetClassifierAdmin(ModelAdmin):
    """PreTrainedKerasImageNetClassifier model admin."""

    show_full_result_count = False

    @silk_profile(
        name=(f'{__module__}: '
              f'{PreTrainedKerasImageNetClassifier._meta.verbose_name}'))
    def changeform_view(self, *args, **kwargs):
        """Silk-profiled change-form view."""
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=(f'{__module__}: '
              f'{PreTrainedKerasImageNetClassifier._meta.verbose_name_plural}')
    )
    def changelist_view(self, *args, **kwargs):
        """Silk-profiled change-list view."""
        return super().changelist_view(*args, **kwargs)


@register(PreTrainedHuggingFaceTransformer, site=site)
class PreTrainedHuggingFaceTransformerAdmin(ModelAdmin):
    """PreTrainedHuggingFaceTransformer model admin."""

    show_full_result_count = False

    @silk_profile(
        name=(f'{__module__}: '
              f'{PreTrainedHuggingFaceTransformer._meta.verbose_name}'))
    def changeform_view(self, *args, **kwargs):
        """Silk-profiled change-form view."""
        return super().changeform_view(*args, **kwargs)

    @silk_profile(
        name=(f'{__module__}: '
              f'{PreTrainedHuggingFaceTransformer._meta.verbose_name_plural}'))
    def changelist_view(self, *args, **kwargs):
        """Silk-profiled change-list view."""
        return super().changelist_view(*args, **kwargs)
