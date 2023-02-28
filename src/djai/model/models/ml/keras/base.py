"""Djaizz TensorFlow.Keras Deep Learning Model class."""


from pathlib import Path
from sys import version_info

import h5py
from tensorflow.python.keras.saving.save import \
    load_model   # pylint: disable=no-name-in-module

from ...base import _AIModelWithArtifactFilesABC

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('KerasModel',)


class KerasModel(_AIModelWithArtifactFilesABC):
    # pylint: disable=abstract-method
    """Djaizz TensorFlow.Keras Deep Learning Model class."""

    class Meta(_AIModelWithArtifactFilesABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True

    def load(self) -> None:
        """Load the Model's native object from it artifact file."""
        if not self.native_obj:
            artifact_local_path = str(Path(self.artifact_local_path)
                                      .expanduser())

            self.native_obj = \
                load_model(filepath=(h5py.File(name=artifact_local_path,
                                               mode='r',
                                               driver=None,
                                               libver=None,
                                               userblock_size=None,
                                               swmr=False,
                                               rdcc_nslots=None,
                                               rdcc_nbytes=None,
                                               rdcc_w0=None,
                                               track_order=None,
                                               fs_strategy=None,
                                               fs_persist=False,
                                               fs_threshold=1)
                                     if artifact_local_path.endswith('.h5')
                                     else artifact_local_path),
                           custom_objects=None,
                           compile=True,
                           options=None)
