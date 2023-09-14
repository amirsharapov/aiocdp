from dataclasses import (
    dataclass
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.browser.types import (
    BrowserContextID
)

TargetID = str

SessionID = str


@dataclass
class TargetInfo:
    target_id: "TargetID"
    type: str
    title: str
    url: str
    attached: bool
    opener_id: "TargetID"
    can_access_opener: bool
    opener_frame_id: "FrameId"
    browser_context_id: "BrowserContextID"
    subtype: str


@dataclass
class FilterEntry:
    exclude: bool
    type: str


@dataclass
class RemoteLocation:
    host: str
    port: int
