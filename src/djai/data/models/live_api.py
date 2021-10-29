"""DjAI Image DataSet class."""


from collections.abc import Sequence

from .base import DataSet


__all__: Sequence[str] = ('LiveAPIDataSource',)


class LiveAPIDataSource(DataSet):
    # pylint: disable=abstract-method,too-many-ancestors
    """DjAI Image DataSet class."""

    class Meta(DataSet.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True
