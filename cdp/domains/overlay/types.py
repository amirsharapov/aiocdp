from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

ColorFormat = Literal[
    "rgb",
    "hsl",
    "hwb",
    "hex"
]

ContrastAlgorithm = Literal[
    "aa",
    "aaa",
    "apca"
]

InspectMode = Literal[
    "searchForNode",
    "searchForUAShadowDOM",
    "captureAreaScreenshot",
    "showDistances",
    "none"
]


@dataclass
class BoxStyle:
    fillColor: RGBA
    hatchColor: RGBA


@dataclass
class ContainerQueryContainerHighlightConfig:
    containerBorder: LineStyle
    descendantBorder: LineStyle


@dataclass
class ContainerQueryHighlightConfig:
    containerQueryContainerHighlightConfig: ContainerQueryContainerHighlightConfig
    nodeId: NodeId


@dataclass
class FlexContainerHighlightConfig:
    containerBorder: LineStyle
    lineSeparator: LineStyle
    itemSeparator: LineStyle
    mainDistributedSpace: BoxStyle
    crossDistributedSpace: BoxStyle
    rowGapSpace: BoxStyle
    columnGapSpace: BoxStyle
    crossAlignment: LineStyle


@dataclass
class FlexItemHighlightConfig:
    baseSizeBox: BoxStyle
    baseSizeBorder: LineStyle
    flexibilityArrow: LineStyle


@dataclass
class FlexNodeHighlightConfig:
    flexContainerHighlightConfig: FlexContainerHighlightConfig
    nodeId: NodeId


@dataclass
class GridHighlightConfig:
    showGridExtensionLines: bool
    showPositiveLineNumbers: bool
    showNegativeLineNumbers: bool
    showAreaNames: bool
    showLineNames: bool
    showTrackSizes: bool
    gridBorderColor: RGBA
    cellBorderColor: RGBA
    rowLineColor: RGBA
    columnLineColor: RGBA
    gridBorderDash: bool
    cellBorderDash: bool
    rowLineDash: bool
    columnLineDash: bool
    rowGapColor: RGBA
    rowHatchColor: RGBA
    columnGapColor: RGBA
    columnHatchColor: RGBA
    areaBorderColor: RGBA
    gridBackgroundColor: RGBA


@dataclass
class GridNodeHighlightConfig:
    gridHighlightConfig: GridHighlightConfig
    nodeId: NodeId


@dataclass
class HighlightConfig:
    showInfo: bool
    showStyles: bool
    showRulers: bool
    showAccessibilityInfo: bool
    showExtensionLines: bool
    contentColor: RGBA
    paddingColor: RGBA
    borderColor: RGBA
    marginColor: RGBA
    eventTargetColor: RGBA
    shapeColor: RGBA
    shapeMarginColor: RGBA
    cssGridColor: RGBA
    colorFormat: ColorFormat
    gridHighlightConfig: GridHighlightConfig
    flexContainerHighlightConfig: FlexContainerHighlightConfig
    flexItemHighlightConfig: FlexItemHighlightConfig
    contrastAlgorithm: ContrastAlgorithm
    containerQueryContainerHighlightConfig: ContainerQueryContainerHighlightConfig


@dataclass
class HingeConfig:
    rect: Rect
    contentColor: RGBA
    outlineColor: RGBA


@dataclass
class IsolatedElementHighlightConfig:
    isolationModeHighlightConfig: IsolationModeHighlightConfig
    nodeId: NodeId


@dataclass
class IsolationModeHighlightConfig:
    resizerColor: RGBA
    resizerHandleColor: RGBA
    maskColor: RGBA


@dataclass
class LineStyle:
    color: RGBA
    pattern: str


@dataclass
class ScrollSnapContainerHighlightConfig:
    snapportBorder: LineStyle
    snapAreaBorder: LineStyle
    scrollMarginColor: RGBA
    scrollPaddingColor: RGBA


@dataclass
class ScrollSnapHighlightConfig:
    scrollSnapContainerHighlightConfig: ScrollSnapContainerHighlightConfig
    nodeId: NodeId


@dataclass
class SourceOrderConfig:
    parentOutlineColor: RGBA
    childOutlineColor: RGBA
