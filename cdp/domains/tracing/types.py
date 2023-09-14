from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

MemoryDumpLevelOfDetail = Literal[
    "background",
    "light",
    "detailed"
]

StreamCompression = Literal[
    "none",
    "gzip"
]

StreamFormat = Literal[
    "json",
    "proto"
]

TracingBackend = Literal[
    "auto",
    "chrome",
    "system"
]


@dataclass
class TraceConfig:
    recordMode: str
    traceBufferSizeInKb: float
    enableSampling: bool
    enableSystrace: bool
    enableArgumentFilter: bool
    includedCategories: list
    excludedCategories: list
    syntheticDelays: list
    memoryDumpConfig: MemoryDumpConfig
