"""DjAI TensorFlow.Keras Deep Learning Model class."""


from collections.abc import Sequence
from pathlib import Path

import h5py
from tensorflow.python.keras.saving.save import \
    load_model   # pylint: disable=no-name-in-module

from ...base import _AIModelWithArtifactFilesABC


__all__: Sequence[str] = ('KerasModel',)


class KerasModel(_AIModelWithArtifactFilesABC):
    # pylint: disable=abstract-method
    """DjAI TensorFlow.Keras Deep Learning Model class."""

    class Meta(_AIModelWithArtifactFilesABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True

    def load(self) -> None:
        """Load the Model's native object from it artifact file."""
        artifact_local_path = str(Path(self.artifact_local_path).expanduser())

        self.native_obj = \
            load_model(filepath=(h5py.File(name=artifact_local_path, mode='r')
                                 if artifact_local_path.endswith('.h5')
                                 else artifact_local_path),
                       custom_objects=None,
                       compile=True,
                       options=None)
