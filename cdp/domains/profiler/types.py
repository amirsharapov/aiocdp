from dataclasses import (
    dataclass
)
from cdp.domains.runtime.types import (
    CallFrame,
    ScriptId
)


@dataclass
class ProfileNode:
    id: int
    call_frame: "CallFrame"
    hit_count: int
    children: list
    deopt_reason: str
    position_ticks: list


@dataclass
class Profile:
    nodes: list
    start_time: float
    end_time: float
    samples: list
    time_deltas: list


@dataclass
class PositionTickInfo:
    line: int
    ticks: int


@dataclass
class CoverageRange:
    start_offset: int
    end_offset: int
    count: int


@dataclass
class FunctionCoverage:
    function_name: str
    ranges: list
    is_block_coverage: bool


@dataclass
class ScriptCoverage:
    script_id: "ScriptId"
    url: str
    functions: list


@dataclass
class TypeObject:
    name: str


@dataclass
class TypeProfileEntry:
    offset: int
    types: list


@dataclass
class ScriptTypeProfile:
    script_id: "ScriptId"
    url: str
    entries: list


@dataclass
class GetBestEffortCoverageReturnT:
    result: list


@dataclass
class StopReturnT:
    profile: "Profile"


@dataclass
class TakePreciseCoverageReturnT:
    result: list


@dataclass
class TakeTypeProfileReturnT:
    result: list
