from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class FilterEntry:
    exclude: bool
    type: str


@dataclass
class RemoteLocation:
    host: str
    port: int


@dataclass
class TargetInfo:
    targetId: TargetID
    type: str
    title: str
    url: str
    attached: bool
    openerId: TargetID
    canAccessOpener: bool
    openerFrameId: FrameId
    browserContextId: BrowserContextID
    subtype: str
