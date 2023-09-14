from dataclasses import (
    dataclass
)
from cdp.domains.runtime.types import (
    CallFrame
)

HeapSnapshotObjectId = str


@dataclass
class SamplingHeapProfileNode:
    call_frame: "CallFrame"
    self_size: float
    id: int
    children: list


@dataclass
class SamplingHeapProfileSample:
    size: float
    node_id: int
    ordinal: float


@dataclass
class SamplingHeapProfile:
    head: "SamplingHeapProfileNode"
    samples: list
