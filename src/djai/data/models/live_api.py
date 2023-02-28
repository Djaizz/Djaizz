"""Djaizz Image DataSet class."""


from sys import version_info

from .base import DataSet

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('LiveAPIDataSource',)


class LiveAPIDataSource(DataSet):
    # pylint: disable=abstract-method,too-many-ancestors
    """Djaizz Image DataSet class."""

    class Meta(DataSet.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True
