from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class ComputedStyle:
    properties: list


@dataclass
class DOMNode:
    nodeType: int
    nodeName: str
    nodeValue: str
    textValue: str
    inputValue: str
    inputChecked: bool
    optionSelected: bool
    backendNodeId: BackendNodeId
    childNodeIndexes: list
    attributes: list
    pseudoElementIndexes: list
    layoutNodeIndex: int
    documentURL: str
    baseURL: str
    contentLanguage: str
    documentEncoding: str
    publicId: str
    systemId: str
    frameId: FrameId
    contentDocumentIndex: int
    pseudoType: PseudoType
    shadowRootType: ShadowRootType
    isClickable: bool
    eventListeners: list
    currentSourceURL: str
    originURL: str
    scrollOffsetX: float
    scrollOffsetY: float


@dataclass
class DocumentSnapshot:
    documentURL: StringIndex
    title: StringIndex
    baseURL: StringIndex
    contentLanguage: StringIndex
    encodingName: StringIndex
    publicId: StringIndex
    systemId: StringIndex
    frameId: StringIndex
    nodes: NodeTreeSnapshot
    layout: LayoutTreeSnapshot
    textBoxes: TextBoxSnapshot
    scrollOffsetX: float
    scrollOffsetY: float
    contentWidth: float
    contentHeight: float


@dataclass
class InlineTextBox:
    boundingBox: Rect
    startCharacterIndex: int
    numCharacters: int


@dataclass
class LayoutTreeNode:
    domNodeIndex: int
    boundingBox: Rect
    layoutText: str
    inlineTextNodes: list
    styleIndex: int
    paintOrder: int
    isStackingContext: bool


@dataclass
class LayoutTreeSnapshot:
    nodeIndex: list
    styles: list
    bounds: list
    text: list
    stackingContexts: RareBooleanData
    paintOrders: list
    offsetRects: list
    scrollRects: list
    clientRects: list
    blendedBackgroundColors: list
    textColorOpacities: list


@dataclass
class NameValue:
    name: str
    value: str


@dataclass
class NodeTreeSnapshot:
    parentIndex: list
    nodeType: list
    shadowRootType: RareStringData
    nodeName: list
    nodeValue: list
    backendNodeId: list
    attributes: list
    textValue: RareStringData
    inputValue: RareStringData
    inputChecked: RareBooleanData
    optionSelected: RareBooleanData
    contentDocumentIndex: RareIntegerData
    pseudoType: RareStringData
    pseudoIdentifier: RareStringData
    isClickable: RareBooleanData
    currentSourceURL: RareStringData
    originURL: RareStringData


@dataclass
class RareBooleanData:
    index: list


@dataclass
class RareIntegerData:
    index: list
    value: list


@dataclass
class RareStringData:
    index: list
    value: list


@dataclass
class TextBoxSnapshot:
    layoutIndex: list
    bounds: list
    start: list
    length: list
