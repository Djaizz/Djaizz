"""Djaizz SciKit-Learn Machine Learning Model class."""


import pickle
from sys import version_info

import joblib

from ..base import _AIModelWithArtifactFilesABC

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('SKLModel',)


class SKLModel(_AIModelWithArtifactFilesABC):
    # pylint: disable=abstract-method
    """Djaizz SciKit-Learn Machine Learning Model class."""

    class Meta(_AIModelWithArtifactFilesABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True

    # scikit-learn.org/stable/modules/model_persistence.html#python-specific-serialization
    def save(self, *args, **kwargs):
        """Save the Model into the DB, and its native object into file."""
        assert self.native_obj, \
            ValueError(f'*** MODEL OBJECT {self.native_obj} INVALID ***')

        joblib.dump(value=self.native_obj,
                    filename=self.artifact_local_path,
                    compress=9,
                    protocol=pickle.HIGHEST_PROTOCOL,
                    cache_size=None,)

        super().save(*args, **kwargs)

    def load(self) -> None:
        """Load the Model's native object from it artifact file."""
        if self.native_obj is None:
            self.native_obj = \
                joblib.load(filename=self.artifact_local_path, mmap_mode=None)
