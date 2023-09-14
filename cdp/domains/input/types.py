from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

GestureSourceType = Literal[
    "default",
    "touch",
    "mouse"
]

MouseButton = Literal[
    "none",
    "left",
    "middle",
    "right",
    "back",
    "forward"
]


@dataclass
class DragData:
    items: list
    files: list
    dragOperationsMask: int


@dataclass
class DragDataItem:
    mimeType: str
    data: str
    title: str
    baseURL: str


@dataclass
class TouchPoint:
    x: float
    y: float
    radiusX: float
    radiusY: float
    rotationAngle: float
    force: float
    tangentialPressure: float
    tiltX: int
    tiltY: int
    twist: int
    id: float
