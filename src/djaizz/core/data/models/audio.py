"""Djaizz Audio DataSet class."""


from sys import version_info

from .base import _FileDataSetABC

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('AudioDataSet',)


class AudioDataSet(_FileDataSetABC):
    # pylint: disable=abstract-method,too-many-ancestors
    """Djaizz Audio DataSet class."""

    class Meta(_FileDataSetABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True
