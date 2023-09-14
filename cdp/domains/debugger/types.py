from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class BreakLocation:
    scriptId: ScriptId
    lineNumber: int
    columnNumber: int
    type: str


@dataclass
class CallFrame:
    callFrameId: CallFrameId
    functionName: str
    functionLocation: Location
    location: Location
    url: str
    scopeChain: list
    this: RemoteObject
    returnValue: RemoteObject


@dataclass
class Location:
    scriptId: ScriptId
    lineNumber: int
    columnNumber: int


@dataclass
class Scope:
    type: str
    object: RemoteObject
    name: str
    startLocation: Location
    endLocation: Location


@dataclass
class ScriptPosition:
    lineNumber: int
    columnNumber: int


@dataclass
class SearchMatch:
    lineNumber: float
    lineContent: str
