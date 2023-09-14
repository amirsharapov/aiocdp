from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.runtime.types import (
    ExecutionContextId,
    RemoteObject,
    RemoteObjectId,
    StackTrace
)

NodeId = int

BackendNodeId = int

Quad = list[float]

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

CompatibilityMode = Literal[
    "QuirksMode",
    "LimitedQuirksMode",
    "NoQuirksMode"
]

PhysicalAxes = Literal[
    "Horizontal",
    "Vertical",
    "Both"
]

LogicalAxes = Literal[
    "Inline",
    "Block",
    "Both"
]


@dataclass
class BackendNode:
    node_type: int
    node_name: str
    backend_node_id: "BackendNodeId"


@dataclass
class Node:
    node_id: "NodeId"
    parent_id: "NodeId"
    backend_node_id: "BackendNodeId"
    node_type: int
    node_name: str
    local_name: str
    node_value: str
    child_node_count: int
    children: list
    attributes: list
    document_url: str
    base_url: str
    public_id: str
    system_id: str
    internal_subset: str
    xml_version: str
    name: str
    value: str
    pseudo_type: "PseudoType"
    pseudo_identifier: str
    shadow_root_type: "ShadowRootType"
    frame_id: "FrameId"
    content_document: "Node"
    shadow_roots: list
    template_content: "Node"
    pseudo_elements: list
    imported_document: "Node"
    distributed_nodes: list
    is_svg: bool
    compatibility_mode: "CompatibilityMode"
    assigned_slot: "BackendNode"


@dataclass
class RGBA:
    r: int
    g: int
    b: int
    a: float


@dataclass
class BoxModel:
    content: "Quad"
    padding: "Quad"
    border: "Quad"
    margin: "Quad"
    width: int
    height: int
    shape_outside: "ShapeOutsideInfo"


@dataclass
class ShapeOutsideInfo:
    bounds: "Quad"
    shape: list
    margin_shape: list


@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float


@dataclass
class CSSComputedStyleProperty:
    name: str
    value: str


@dataclass
class CollectClassNamesFromSubtreeReturnT:
    class_names: list


@dataclass
class CopyToReturnT:
    node_id: "NodeId"


@dataclass
class DescribeNodeReturnT:
    node: "Node"


@dataclass
class GetAttributesReturnT:
    attributes: list


@dataclass
class GetBoxModelReturnT:
    model: "BoxModel"


@dataclass
class GetContentQuadsReturnT:
    quads: list


@dataclass
class GetDocumentReturnT:
    root: "Node"


@dataclass
class GetFlattenedDocumentReturnT:
    nodes: list


@dataclass
class GetNodesForSubtreeByStyleReturnT:
    node_ids: list


@dataclass
class GetNodeForLocationReturnT:
    backend_node_id: "BackendNodeId"
    frame_id: "FrameId"
    node_id: "NodeId"


@dataclass
class GetOuterHTMLReturnT:
    outer_html: str


@dataclass
class GetRelayoutBoundaryReturnT:
    node_id: "NodeId"


@dataclass
class GetSearchResultsReturnT:
    node_ids: list


@dataclass
class MoveToReturnT:
    node_id: "NodeId"


@dataclass
class PerformSearchReturnT:
    search_id: str
    result_count: int


@dataclass
class PushNodeByPathToFrontendReturnT:
    node_id: "NodeId"


@dataclass
class PushNodesByBackendIdsToFrontendReturnT:
    node_ids: list


@dataclass
class QuerySelectorReturnT:
    node_id: "NodeId"


@dataclass
class QuerySelectorAllReturnT:
    node_ids: list


@dataclass
class GetTopLayerElementsReturnT:
    node_ids: list


@dataclass
class RequestNodeReturnT:
    node_id: "NodeId"


@dataclass
class ResolveNodeReturnT:
    object: "RemoteObject"


@dataclass
class GetNodeStackTracesReturnT:
    creation: "StackTrace"


@dataclass
class GetFileInfoReturnT:
    path: str


@dataclass
class SetNodeNameReturnT:
    node_id: "NodeId"


@dataclass
class GetFrameOwnerReturnT:
    backend_node_id: "BackendNodeId"
    node_id: "NodeId"


@dataclass
class GetContainerForNodeReturnT:
    node_id: "NodeId"


@dataclass
class GetQueryingDescendantsForContainerReturnT:
    node_ids: list
