"""Djaizz Django views-related utilities."""


from sys import version_info
from typing import Union
from uuid import UUID

from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.http.response import Http404
from django.shortcuts import get_object_or_404

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence   # pylint: disable=ungrouped-imports


__all__: Sequence[str] = ('LookUpByUniqueNameOrUUIDMixin',)


# refs:
# - django-rest-framework.org/api-guide/generic-views/#creating-custom-mixins
# - stackoverflow.com/questions/38461366
class LookUpByUniqueNameOrUUIDMixin:
    # pylint: disable=too-few-public-methods
    """A mix-in to look up Django model object by UUID or Unique Name."""

    def get_object(self) -> Union[Model, Http404]:
        """Get Django model object by UUID or Unique Name."""
        # get base queryset
        queryset: QuerySet = self.get_queryset()

        # apply any filter backends
        queryset: QuerySet = self.filter_queryset(queryset)

        # get look-up value
        lookup_value: str = str(self.kwargs[self.lookup_field])

        try:   # try looking up object by UUID
            _uuid: UUID = UUID(hex=lookup_value, version=4)
            obj: Union[Model, Http404] = get_object_or_404(queryset,
                                                           uuid=_uuid)

        except ValueError:
            # else look up by Name
            obj: Union[Model, Http404] = get_object_or_404(queryset,
                                                           name=lookup_value)

        # check object permissions
        self.check_object_permissions(self.request, obj)

        return obj
