# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from typing import (
    Any,
    Literal,
    TYPE_CHECKING
)
from dataclasses import (
    dataclass
)

HeapSnapshotObjectId = str

@dataclass
class SamplingHeapProfileNode:
    call_frame: 'CallFrame'
    self_size: float
    id: int
    children: list['SamplingHeapProfileNode']


@dataclass
class SamplingHeapProfileSample:
    size: float
    node_id: int
    ordinal: float


@dataclass
class SamplingHeapProfile:
    head: 'SamplingHeapProfileNode'
    samples: list['SamplingHeapProfileSample']


@dataclass
class GetHeapObjectIdReturnType:
    heap_snapshot_object_id: 'HeapSnapshotObjectId'


@dataclass
class GetObjectByHeapObjectIdReturnType:
    result: 'RemoteObject'


@dataclass
class GetSamplingProfileReturnType:
    profile: 'SamplingHeapProfile'


@dataclass
class StopSamplingReturnType:
    profile: 'SamplingHeapProfile'
