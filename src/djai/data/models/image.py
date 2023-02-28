"""Djaizz Image DataSet class."""


from sys import version_info

from .base import _FileDataSetABC

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('ImageDataSet',)


class ImageDataSet(_FileDataSetABC):
    # pylint: disable=abstract-method,too-many-ancestors
    """Djaizz Image DataSet class."""

    class Meta(_FileDataSetABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True
