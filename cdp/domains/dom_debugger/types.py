from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.runtime.types import (
    RemoteObject,
    ScriptId
)
from cdp.domains.dom.types import (
    BackendNodeId
)

DOMBreakpointType = Literal[
    "subtree-modified",
    "attribute-modified",
    "node-removed"
]

CSPViolationType = Literal[
    "trustedtype-sink-violation",
    "trustedtype-policy-violation"
]


@dataclass
class EventListener:
    type: str
    use_capture: bool
    passive: bool
    once: bool
    script_id: "ScriptId"
    line_number: int
    column_number: int
    handler: "RemoteObject"
    original_handler: "RemoteObject"
    backend_node_id: "BackendNodeId"
