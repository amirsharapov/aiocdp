from dataclasses import (
    dataclass
)
from cdp.domains.runtime.types import (
    RemoteObject,
    ScriptId
)

BreakpointId = str

CallFrameId = str


@dataclass
class Location:
    script_id: "ScriptId"
    line_number: int
    column_number: int


@dataclass
class ScriptPosition:
    line_number: int
    column_number: int


@dataclass
class CallFrame:
    call_frame_id: "CallFrameId"
    function_name: str
    function_location: "Location"
    location: "Location"
    url: str
    scope_chain: list
    this: "RemoteObject"
    return_value: "RemoteObject"


@dataclass
class Scope:
    type: str
    object: "RemoteObject"
    name: str
    start_location: "Location"
    end_location: "Location"


@dataclass
class SearchMatch:
    line_number: float
    line_content: str


@dataclass
class BreakLocation:
    script_id: "ScriptId"
    line_number: int
    column_number: int
    type: str
