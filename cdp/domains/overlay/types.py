from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.dom.types import (
    NodeId,
    RGBA,
    Rect
)

ContrastAlgorithm = Literal[
    "aa",
    "aaa",
    "apca"
]

ColorFormat = Literal[
    "rgb",
    "hsl",
    "hwb",
    "hex"
]

InspectMode = Literal[
    "searchForNode",
    "searchForUAShadowDOM",
    "captureAreaScreenshot",
    "showDistances",
    "none"
]


@dataclass
class SourceOrderConfig:
    parent_outline_color: "RGBA"
    child_outline_color: "RGBA"


@dataclass
class GridHighlightConfig:
    show_grid_extension_lines: bool
    show_positive_line_numbers: bool
    show_negative_line_numbers: bool
    show_area_names: bool
    show_line_names: bool
    show_track_sizes: bool
    grid_border_color: "RGBA"
    cell_border_color: "RGBA"
    row_line_color: "RGBA"
    column_line_color: "RGBA"
    grid_border_dash: bool
    cell_border_dash: bool
    row_line_dash: bool
    column_line_dash: bool
    row_gap_color: "RGBA"
    row_hatch_color: "RGBA"
    column_gap_color: "RGBA"
    column_hatch_color: "RGBA"
    area_border_color: "RGBA"
    grid_background_color: "RGBA"


@dataclass
class FlexContainerHighlightConfig:
    container_border: "LineStyle"
    line_separator: "LineStyle"
    item_separator: "LineStyle"
    main_distributed_space: "BoxStyle"
    cross_distributed_space: "BoxStyle"
    row_gap_space: "BoxStyle"
    column_gap_space: "BoxStyle"
    cross_alignment: "LineStyle"


@dataclass
class FlexItemHighlightConfig:
    base_size_box: "BoxStyle"
    base_size_border: "LineStyle"
    flexibility_arrow: "LineStyle"


@dataclass
class LineStyle:
    color: "RGBA"
    pattern: str


@dataclass
class BoxStyle:
    fill_color: "RGBA"
    hatch_color: "RGBA"


@dataclass
class HighlightConfig:
    show_info: bool
    show_styles: bool
    show_rulers: bool
    show_accessibility_info: bool
    show_extension_lines: bool
    content_color: "RGBA"
    padding_color: "RGBA"
    border_color: "RGBA"
    margin_color: "RGBA"
    event_target_color: "RGBA"
    shape_color: "RGBA"
    shape_margin_color: "RGBA"
    css_grid_color: "RGBA"
    color_format: "ColorFormat"
    grid_highlight_config: "GridHighlightConfig"
    flex_container_highlight_config: "FlexContainerHighlightConfig"
    flex_item_highlight_config: "FlexItemHighlightConfig"
    contrast_algorithm: "ContrastAlgorithm"
    container_query_container_highlight_config: "ContainerQueryContainerHighlightConfig"


@dataclass
class GridNodeHighlightConfig:
    grid_highlight_config: "GridHighlightConfig"
    node_id: "NodeId"


@dataclass
class FlexNodeHighlightConfig:
    flex_container_highlight_config: "FlexContainerHighlightConfig"
    node_id: "NodeId"


@dataclass
class ScrollSnapContainerHighlightConfig:
    snapport_border: "LineStyle"
    snap_area_border: "LineStyle"
    scroll_margin_color: "RGBA"
    scroll_padding_color: "RGBA"


@dataclass
class ScrollSnapHighlightConfig:
    scroll_snap_container_highlight_config: "ScrollSnapContainerHighlightConfig"
    node_id: "NodeId"


@dataclass
class HingeConfig:
    rect: "Rect"
    content_color: "RGBA"
    outline_color: "RGBA"


@dataclass
class ContainerQueryHighlightConfig:
    container_query_container_highlight_config: "ContainerQueryContainerHighlightConfig"
    node_id: "NodeId"


@dataclass
class ContainerQueryContainerHighlightConfig:
    container_border: "LineStyle"
    descendant_border: "LineStyle"


@dataclass
class IsolatedElementHighlightConfig:
    isolation_mode_highlight_config: "IsolationModeHighlightConfig"
    node_id: "NodeId"


@dataclass
class IsolationModeHighlightConfig:
    resizer_color: "RGBA"
    resizer_handle_color: "RGBA"
    mask_color: "RGBA"
