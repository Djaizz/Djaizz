"""DjAI Image DataSet class."""


from collections.abc import Sequence

from .base import _FileDataSetABC


__all__: Sequence[str] = ('ImageDataSet',)


class ImageDataSet(_FileDataSetABC):
    # pylint: disable=abstract-method,too-many-ancestors
    """DjAI Image DataSet class."""

    class Meta(_FileDataSetABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True
