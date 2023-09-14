from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class LargestContentfulPaint:
    renderTime: TimeSinceEpoch
    loadTime: TimeSinceEpoch
    size: float
    elementId: str
    url: str
    nodeId: BackendNodeId


@dataclass
class LayoutShift:
    value: float
    hadRecentInput: bool
    lastInputTime: TimeSinceEpoch
    sources: list


@dataclass
class LayoutShiftAttribution:
    previousRect: Rect
    currentRect: Rect
    nodeId: BackendNodeId


@dataclass
class TimelineEvent:
    frameId: FrameId
    type: str
    name: str
    time: TimeSinceEpoch
    duration: float
    lcpDetails: LargestContentfulPaint
    layoutShiftDetails: LayoutShift
