"""Djaizz DataSet/DataSource Model classes."""


from sys import version_info

from .base import DataSchema, DataSet

from .json import InDBJSONDataSet, JSONDataSet
from .numpy import NumPyArray
from .pandas import PandasDataFrame

from .audio import AudioDataSet
from .csv import CSVDataSet
from .hdf import HDFDataSet
from .image import ImageDataSet
from .orc import ORCDataSet
from .parquet import ParquetDataSet
from .text import TextDataSet
from .tfrecord import TFRecordDataSet
from .video import VideoDataSet

from .live_api import LiveAPIDataSource

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'DataSchema', 'DataSet',

    'InDBJSONDataSet', 'JSONDataSet',
    'NumPyArray', 'PandasDataFrame',

    'AudioDataSet',
    'CSVDataSet',
    'HDFDataSet',
    'ImageDataSet',
    'ORCDataSet',
    'ParquetDataSet',
    'TextDataSet',
    'TFRecordDataSet',
    'VideoDataSet',

    'LiveAPIDataSource',
)
