from dataclasses import (
    dataclass
)
from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.dom.types import (
    BackendNodeId,
    Quad,
    Rect,
    NodeId,
    RGBA
)
from cdp.domains.overlay.types import (
    FlexItemHighlightConfig,
    ScrollSnapContainerHighlightConfig,
    FlexContainerHighlightConfig,
    HighlightConfig,
    LineStyle,
    BoxStyle,
    HingeConfig,
    SourceOrderConfig,
    ContrastAlgorithm,
    ContainerQueryContainerHighlightConfig,
    InspectMode,
    ColorFormat,
    GridHighlightConfig,
    IsolationModeHighlightConfig
)
from cdp.domains.page.types import (
    FrameId,
    Viewport
)
from cdp.domains.runtime.types import (
    RemoteObjectId
)


@dataclass
class Overlay(BaseDomain):
    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Overlay.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Overlay.enable",
            params
        )

    def get_highlight_object_for_test(
        self,
        node_id: NodeId,
        include_distance: MaybeUndefined[],
        include_style: MaybeUndefined[],
        color_format: MaybeUndefined[],
        show_accessibility_info: MaybeUndefined[]
    ):
        params = {
            "nodeId": node_id,
        }

        if is_defined(
            include_distance
        ):
            params[] = include_distance

        if is_defined(
            include_style
        ):
            params[] = include_style

        if is_defined(
            color_format
        ):
            params[] = color_format

        if is_defined(
            show_accessibility_info
        ):
            params[] = show_accessibility_info

        return self._send_command(
            "Overlay.getHighlightObjectForTest",
            params
        )

    def get_grid_highlight_objects_for_test(
        self,
        node_ids: list
    ):
        params = {
            "nodeIds": node_ids,
        }

        return self._send_command(
            "Overlay.getGridHighlightObjectsForTest",
            params
        )

    def get_source_order_highlight_object_for_test(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "Overlay.getSourceOrderHighlightObjectForTest",
            params
        )

    def hide_highlight(
        self
    ):
        params = {}

        return self._send_command(
            "Overlay.hideHighlight",
            params
        )

    def highlight_frame(
        self,
        frame_id: FrameId,
        content_color: MaybeUndefined[],
        content_outline_color: MaybeUndefined[]
    ):
        params = {
            "frameId": frame_id,
        }

        if is_defined(
            content_color
        ):
            params[] = content_color

        if is_defined(
            content_outline_color
        ):
            params[] = content_outline_color

        return self._send_command(
            "Overlay.highlightFrame",
            params
        )

    def highlight_node(
        self,
        highlight_config: HighlightConfig,
        node_id: MaybeUndefined[],
        backend_node_id: MaybeUndefined[],
        object_id: MaybeUndefined[],
        selector: MaybeUndefined[]
    ):
        params = {
            "highlightConfig": highlight_config,
        }

        if is_defined(
            node_id
        ):
            params[] = node_id

        if is_defined(
            backend_node_id
        ):
            params[] = backend_node_id

        if is_defined(
            object_id
        ):
            params[] = object_id

        if is_defined(
            selector
        ):
            params[] = selector

        return self._send_command(
            "Overlay.highlightNode",
            params
        )

    def highlight_quad(
        self,
        quad: Quad,
        color: MaybeUndefined[],
        outline_color: MaybeUndefined[]
    ):
        params = {
            "quad": quad,
        }

        if is_defined(
            color
        ):
            params[] = color

        if is_defined(
            outline_color
        ):
            params[] = outline_color

        return self._send_command(
            "Overlay.highlightQuad",
            params
        )

    def highlight_rect(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: MaybeUndefined[],
        outline_color: MaybeUndefined[]
    ):
        params = {
            "x": x,
            "y": y,
            "width": width,
            "height": height,
        }

        if is_defined(
            color
        ):
            params[] = color

        if is_defined(
            outline_color
        ):
            params[] = outline_color

        return self._send_command(
            "Overlay.highlightRect",
            params
        )

    def highlight_source_order(
        self,
        source_order_config: SourceOrderConfig,
        node_id: MaybeUndefined[],
        backend_node_id: MaybeUndefined[],
        object_id: MaybeUndefined[]
    ):
        params = {
            "sourceOrderConfig": source_order_config,
        }

        if is_defined(
            node_id
        ):
            params[] = node_id

        if is_defined(
            backend_node_id
        ):
            params[] = backend_node_id

        if is_defined(
            object_id
        ):
            params[] = object_id

        return self._send_command(
            "Overlay.highlightSourceOrder",
            params
        )

    def set_inspect_mode(
        self,
        mode: InspectMode,
        highlight_config: MaybeUndefined[]
    ):
        params = {
            "mode": mode,
        }

        if is_defined(
            highlight_config
        ):
            params[] = highlight_config

        return self._send_command(
            "Overlay.setInspectMode",
            params
        )

    def set_show_ad_highlights(
        self,
        show: bool
    ):
        params = {
            "show": show,
        }

        return self._send_command(
            "Overlay.setShowAdHighlights",
            params
        )

    def set_paused_in_debugger_message(
        self,
        message: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            message
        ):
            params[] = message

        return self._send_command(
            "Overlay.setPausedInDebuggerMessage",
            params
        )

    def set_show_debug_borders(
        self,
        show: bool
    ):
        params = {
            "show": show,
        }

        return self._send_command(
            "Overlay.setShowDebugBorders",
            params
        )

    def set_show_fps_counter(
        self,
        show: bool
    ):
        params = {
            "show": show,
        }

        return self._send_command(
            "Overlay.setShowFPSCounter",
            params
        )

    def set_show_grid_overlays(
        self,
        grid_node_highlight_configs: list
    ):
        params = {
            "gridNodeHighlightConfigs": grid_node_highlight_configs,
        }

        return self._send_command(
            "Overlay.setShowGridOverlays",
            params
        )

    def set_show_flex_overlays(
        self,
        flex_node_highlight_configs: list
    ):
        params = {
            "flexNodeHighlightConfigs": flex_node_highlight_configs,
        }

        return self._send_command(
            "Overlay.setShowFlexOverlays",
            params
        )

    def set_show_scroll_snap_overlays(
        self,
        scroll_snap_highlight_configs: list
    ):
        params = {
            "scrollSnapHighlightConfigs": scroll_snap_highlight_configs,
        }

        return self._send_command(
            "Overlay.setShowScrollSnapOverlays",
            params
        )

    def set_show_container_query_overlays(
        self,
        container_query_highlight_configs: list
    ):
        params = {
            "containerQueryHighlightConfigs": container_query_highlight_configs,
        }

        return self._send_command(
            "Overlay.setShowContainerQueryOverlays",
            params
        )

    def set_show_paint_rects(
        self,
        result: bool
    ):
        params = {
            "result": result,
        }

        return self._send_command(
            "Overlay.setShowPaintRects",
            params
        )

    def set_show_layout_shift_regions(
        self,
        result: bool
    ):
        params = {
            "result": result,
        }

        return self._send_command(
            "Overlay.setShowLayoutShiftRegions",
            params
        )

    def set_show_scroll_bottleneck_rects(
        self,
        show: bool
    ):
        params = {
            "show": show,
        }

        return self._send_command(
            "Overlay.setShowScrollBottleneckRects",
            params
        )

    def set_show_hit_test_borders(
        self,
        show: bool
    ):
        params = {
            "show": show,
        }

        return self._send_command(
            "Overlay.setShowHitTestBorders",
            params
        )

    def set_show_web_vitals(
        self,
        show: bool
    ):
        params = {
            "show": show,
        }

        return self._send_command(
            "Overlay.setShowWebVitals",
            params
        )

    def set_show_viewport_size_on_resize(
        self,
        show: bool
    ):
        params = {
            "show": show,
        }

        return self._send_command(
            "Overlay.setShowViewportSizeOnResize",
            params
        )

    def set_show_hinge(
        self,
        hinge_config: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            hinge_config
        ):
            params[] = hinge_config

        return self._send_command(
            "Overlay.setShowHinge",
            params
        )

    def set_show_isolated_elements(
        self,
        isolated_element_highlight_configs: list
    ):
        params = {
            "isolatedElementHighlightConfigs": isolated_element_highlight_configs,
        }

        return self._send_command(
            "Overlay.setShowIsolatedElements",
            params
        )

