from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

StreamFormat = Literal[
    "json",
    "proto"
]

StreamCompression = Literal[
    "none",
    "gzip"
]

MemoryDumpLevelOfDetail = Literal[
    "background",
    "light",
    "detailed"
]

TracingBackend = Literal[
    "auto",
    "chrome",
    "system"
]


@dataclass
class TraceConfig:
    record_mode: str
    trace_buffer_size_in_kb: float
    enable_sampling: bool
    enable_systrace: bool
    enable_argument_filter: bool
    included_categories: list
    excluded_categories: list
    synthetic_delays: list
    memory_dump_config: "MemoryDumpConfig"


@dataclass
class GetCategoriesReturnT:
    categories: list


@dataclass
class RequestMemoryDumpReturnT:
    dump_guid: str
    success: bool
