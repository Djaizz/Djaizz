"""DjAI Torch Deep Learning Model class."""


from collections.abc import Sequence

from torch.serialization import load

from ...base import _AIModelWithArtifactFilesABC


__all__: Sequence[str] = ('TorchModel',)


class TorchModel(_AIModelWithArtifactFilesABC):
    # pylint: disable=abstract-method
    """DjAI Torch Deep Learning Model class."""

    class Meta(_AIModelWithArtifactFilesABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True

    def load(self) -> None:
        """Load the Model's native object from it artifact file."""
        if not self.native_obj:
            self.native_obj = load(f=self.artifact_local_path)
