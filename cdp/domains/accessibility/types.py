from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

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

AXValueSourceType = Literal[
    "attribute",
    "implicit",
    "style",
    "contents",
    "placeholder",
    "relatedElement"
]

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


@dataclass
class AXNode:
    nodeId: AXNodeId
    ignored: bool
    ignoredReasons: list
    role: AXValue
    chromeRole: AXValue
    name: AXValue
    description: AXValue
    value: AXValue
    properties: list
    parentId: AXNodeId
    childIds: list
    backendDOMNodeId: BackendNodeId
    frameId: FrameId


@dataclass
class AXProperty:
    name: AXPropertyName
    value: AXValue


@dataclass
class AXRelatedNode:
    backendDOMNodeId: BackendNodeId
    idref: str
    text: str


@dataclass
class AXValue:
    type: AXValueType
    value: Any
    relatedNodes: list
    sources: list


@dataclass
class AXValueSource:
    type: AXValueSourceType
    value: AXValue
    attribute: str
    attributeValue: AXValue
    superseded: bool
    nativeSource: AXValueNativeSourceType
    nativeSourceValue: AXValue
    invalid: bool
    invalidReason: str
