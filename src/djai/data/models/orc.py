"""DjAI ORC DataSet class."""


import sys

from .base import _FileDataSetABC

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('ORCDataSet',)


class ORCDataSet(_FileDataSetABC):
    # pylint: disable=abstract-method,too-many-ancestors
    """DjAI ORC DataSet class."""

    class Meta(_FileDataSetABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True
