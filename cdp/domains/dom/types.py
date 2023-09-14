from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

CompatibilityMode = Literal[
    "QuirksMode",
    "LimitedQuirksMode",
    "NoQuirksMode"
]

LogicalAxes = Literal[
    "Inline",
    "Block",
    "Both"
]

PhysicalAxes = Literal[
    "Horizontal",
    "Vertical",
    "Both"
]

PseudoType = Literal[
    "first-line",
    "first-letter",
    "before",
    "after",
    "marker",
    "backdrop",
    "selection",
    "target-text",
    "spelling-error",
    "grammar-error",
    "highlight",
    "first-line-inherited",
    "scrollbar",
    "scrollbar-thumb",
    "scrollbar-button",
    "scrollbar-track",
    "scrollbar-track-piece",
    "scrollbar-corner",
    "resizer",
    "input-list-button",
    "view-transition",
    "view-transition-group",
    "view-transition-image-pair",
    "view-transition-old",
    "view-transition-new"
]

ShadowRootType = Literal[
    "user-agent",
    "open",
    "closed"
]


@dataclass
class BackendNode:
    nodeType: int
    nodeName: str
    backendNodeId: BackendNodeId


@dataclass
class BoxModel:
    content: Quad
    padding: Quad
    border: Quad
    margin: Quad
    width: int
    height: int
    shapeOutside: ShapeOutsideInfo


@dataclass
class CSSComputedStyleProperty:
    name: str
    value: str


@dataclass
class Node:
    nodeId: NodeId
    parentId: NodeId
    backendNodeId: BackendNodeId
    nodeType: int
    nodeName: str
    localName: str
    nodeValue: str
    childNodeCount: int
    children: list
    attributes: list
    documentURL: str
    baseURL: str
    publicId: str
    systemId: str
    internalSubset: str
    xmlVersion: str
    name: str
    value: str
    pseudoType: PseudoType
    pseudoIdentifier: str
    shadowRootType: ShadowRootType
    frameId: FrameId
    contentDocument: Node
    shadowRoots: list
    templateContent: Node
    pseudoElements: list
    importedDocument: Node
    distributedNodes: list
    isSVG: bool
    compatibilityMode: CompatibilityMode
    assignedSlot: BackendNode


@dataclass
class RGBA:
    r: int
    g: int
    b: int
    a: float


@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float


@dataclass
class ShapeOutsideInfo:
    bounds: Quad
    shape: list
    marginShape: list
