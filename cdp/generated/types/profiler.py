# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from cdp.generated.types import (
    debugger,
    runtime
)
from typing import (
    Literal,
    TypedDict
)


class ProfileNode(TypedDict):
    id: int
    call_frame: 'runtime.CallFrame'
    hit_count: int
    children: list
    deopt_reason: str
    position_ticks: list


class Profile(TypedDict):
    nodes: list
    start_time: float
    end_time: float
    samples: list
    time_deltas: list


class PositionTickInfo(TypedDict):
    line: int
    ticks: int


class CoverageRange(TypedDict):
    start_offset: int
    end_offset: int
    count: int


class FunctionCoverage(TypedDict):
    function_name: str
    ranges: list
    is_block_coverage: bool


class ScriptCoverage(TypedDict):
    script_id: 'runtime.ScriptId'
    url: str
    functions: list


class TypeObject(TypedDict):
    name: str


class TypeProfileEntry(TypedDict):
    offset: int
    types: list


class ScriptTypeProfile(TypedDict):
    script_id: 'runtime.ScriptId'
    url: str
    entries: list


class SetSamplingIntervalParamsT(TypedDict):
    interval: int


class StartPreciseCoverageParamsT(TypedDict):
    call_count: bool
    detailed: bool


class GetBestEffortCoverageReturnT(TypedDict):
    result: list


class StopReturnT(TypedDict):
    profile: 'Profile'


class TakePreciseCoverageReturnT(TypedDict):
    result: list


class TakeTypeProfileReturnT(TypedDict):
    result: list


class ConsoleProfileFinishedEventT(TypedDict):
    name: Literal['console_profile_finished']
    params: 'ConsoleProfileFinishedParamsT'


class ConsoleProfileStartedEventT(TypedDict):
    name: Literal['console_profile_started']
    params: 'ConsoleProfileStartedParamsT'


class ConsoleProfileFinishedParamsT(TypedDict):
    id: str
    location: 'debugger.Location'
    profile: 'Profile'
    title: str


class ConsoleProfileStartedParamsT(TypedDict):
    id: str
    location: 'debugger.Location'
    title: str
