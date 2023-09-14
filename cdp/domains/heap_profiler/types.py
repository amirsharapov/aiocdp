from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class SamplingHeapProfile:
    head: SamplingHeapProfileNode
    samples: list


@dataclass
class SamplingHeapProfileNode:
    callFrame: CallFrame
    selfSize: float
    id: int
    children: list


@dataclass
class SamplingHeapProfileSample:
    size: float
    nodeId: int
    ordinal: float
