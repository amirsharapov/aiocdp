from dataclasses import (
    dataclass
)
from cdp.domains.dom.types import (
    BackendNodeId,
    Rect
)

LayerId = str

SnapshotId = str

PaintProfile = list[float]


@dataclass
class ScrollRect:
    rect: "Rect"
    type: str


@dataclass
class StickyPositionConstraint:
    sticky_box_rect: "Rect"
    containing_block_rect: "Rect"
    nearest_layer_shifting_sticky_box: "LayerId"
    nearest_layer_shifting_containing_block: "LayerId"


@dataclass
class PictureTile:
    x: float
    y: float
    picture: str


@dataclass
class Layer:
    layer_id: "LayerId"
    parent_layer_id: "LayerId"
    backend_node_id: "BackendNodeId"
    offset_x: float
    offset_y: float
    width: float
    height: float
    transform: list
    anchor_x: float
    anchor_y: float
    anchor_z: float
    paint_count: int
    draws_content: bool
    invisible: bool
    scroll_rects: list
    sticky_position_constraint: "StickyPositionConstraint"
