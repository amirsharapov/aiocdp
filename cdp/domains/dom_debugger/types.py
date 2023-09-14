from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

CSPViolationType = Literal[
    "trustedtype-sink-violation",
    "trustedtype-policy-violation"
]

DOMBreakpointType = Literal[
    "subtree-modified",
    "attribute-modified",
    "node-removed"
]


@dataclass
class EventListener:
    type: str
    useCapture: bool
    passive: bool
    once: bool
    scriptId: ScriptId
    lineNumber: int
    columnNumber: int
    handler: RemoteObject
    originalHandler: RemoteObject
    backendNodeId: BackendNodeId
