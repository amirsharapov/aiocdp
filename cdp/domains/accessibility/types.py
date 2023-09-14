from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.dom.types import (
    BackendNodeId
)
from cdp.domains.page.types import (
    FrameId
)

AXNodeId = str

AXValueType = Literal[
    "boolean",
    "tristate",
    "booleanOrUndefined",
    "idref",
    "idrefList",
    "integer",
    "node",
    "nodeList",
    "number",
    "string",
    "computedString",
    "token",
    "tokenList",
    "domRelation",
    "role",
    "internalRole",
    "valueUndefined"
]

AXValueSourceType = Literal[
    "attribute",
    "implicit",
    "style",
    "contents",
    "placeholder",
    "relatedElement"
]

AXValueNativeSourceType = Literal[
    "description",
    "figcaption",
    "label",
    "labelfor",
    "labelwrapped",
    "legend",
    "rubyannotation",
    "tablecaption",
    "title",
    "other"
]

AXPropertyName = Literal[
    "busy",
    "disabled",
    "editable",
    "focusable",
    "focused",
    "hidden",
    "hiddenRoot",
    "invalid",
    "keyshortcuts",
    "settable",
    "roledescription",
    "live",
    "atomic",
    "relevant",
    "root",
    "autocomplete",
    "hasPopup",
    "level",
    "multiselectable",
    "orientation",
    "multiline",
    "readonly",
    "required",
    "valuemin",
    "valuemax",
    "valuetext",
    "checked",
    "expanded",
    "modal",
    "pressed",
    "selected",
    "activedescendant",
    "controls",
    "describedby",
    "details",
    "errormessage",
    "flowto",
    "labelledby",
    "owns"
]


@dataclass
class AXValueSource:
    type: "AXValueSourceType"
    value: "AXValue"
    attribute: str
    attribute_value: "AXValue"
    superseded: bool
    native_source: "AXValueNativeSourceType"
    native_source_value: "AXValue"
    invalid: bool
    invalid_reason: str


@dataclass
class AXRelatedNode:
    backend_dom_node_id: "BackendNodeId"
    idref: str
    text: str


@dataclass
class AXProperty:
    name: "AXPropertyName"
    value: "AXValue"


@dataclass
class AXValue:
    type: "AXValueType"
    value: Any
    related_nodes: list
    sources: list


@dataclass
class AXNode:
    node_id: "AXNodeId"
    ignored: bool
    ignored_reasons: list
    role: "AXValue"
    chrome_role: "AXValue"
    name: "AXValue"
    description: "AXValue"
    value: "AXValue"
    properties: list
    parent_id: "AXNodeId"
    child_ids: list
    backend_dom_node_id: "BackendNodeId"
    frame_id: "FrameId"
