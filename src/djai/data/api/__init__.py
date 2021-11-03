"""DjAI Data API."""


import sys

from djai.data.models import (
    DataSchema, DataSet,

    InDBJSONDataSet, JSONDataSet,
    NumPyArray, PandasDataFrame,

    AudioDataSet,
    CSVDataSet,
    HDFDataSet,
    ImageDataSet,
    ORCDataSet,
    ParquetDataSet,
    TextDataSet,
    TFRecordDataSet,
    VideoDataSet,

    LiveAPIDataSource,
)

if sys.version_info >= (3, 9):
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
