from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class CoverageRange:
    startOffset: int
    endOffset: int
    count: int


@dataclass
class FunctionCoverage:
    functionName: str
    ranges: list
    isBlockCoverage: bool


@dataclass
class PositionTickInfo:
    line: int
    ticks: int


@dataclass
class Profile:
    nodes: list
    startTime: float
    endTime: float
    samples: list
    timeDeltas: list


@dataclass
class ProfileNode:
    id: int
    callFrame: CallFrame
    hitCount: int
    children: list
    deoptReason: str
    positionTicks: list


@dataclass
class ScriptCoverage:
    scriptId: ScriptId
    url: str
    functions: list


@dataclass
class ScriptTypeProfile:
    scriptId: ScriptId
    url: str
    entries: list


@dataclass
class TypeObject:
    name: str


@dataclass
class TypeProfileEntry:
    offset: int
    types: list
