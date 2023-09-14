from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class Layer:
    layerId: LayerId
    parentLayerId: LayerId
    backendNodeId: BackendNodeId
    offsetX: float
    offsetY: float
    width: float
    height: float
    transform: list
    anchorX: float
    anchorY: float
    anchorZ: float
    paintCount: int
    drawsContent: bool
    invisible: bool
    scrollRects: list
    stickyPositionConstraint: StickyPositionConstraint


@dataclass
class PictureTile:
    x: float
    y: float
    picture: str


@dataclass
class ScrollRect:
    rect: Rect
    type: str


@dataclass
class StickyPositionConstraint:
    stickyBoxRect: Rect
    containingBlockRect: Rect
    nearestLayerShiftingStickyBox: LayerId
    nearestLayerShiftingContainingBlock: LayerId
