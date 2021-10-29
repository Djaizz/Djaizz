"""DjAI Video DataSet class."""


from collections.abc import Sequence

from .base import _FileDataSetABC


__all__: Sequence[str] = ('VideoDataSet',)


class VideoDataSet(_FileDataSetABC):
    # pylint: disable=abstract-method,too-many-ancestors
    """DjAI Video DataSet class."""

    class Meta(_FileDataSetABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True
