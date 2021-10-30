"""DjAI NumPyArray class."""


import sys
if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence

from .json import _FileDataSetWithInDBJSONCacheABC


__all__: Sequence[str] = ('PandasDataFrame',)


class PandasDataFrame(_FileDataSetWithInDBJSONCacheABC):
    # pylint: disable=abstract-method,too-many-ancestors
    """DjAI JSON DataSet class."""

    class Meta(_FileDataSetWithInDBJSONCacheABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True
