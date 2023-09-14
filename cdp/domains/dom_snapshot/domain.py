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
    PseudoType,
    ShadowRootType,
    Rect
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.dom_snapshot.types import (
    NodeTreeSnapshot,
    LayoutTreeSnapshot,
    StringIndex,
    RareBooleanData,
    RareIntegerData,
    RareStringData,
    TextBoxSnapshot
)


@dataclass
class DOMSnapshot(BaseDomain):
    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "DOMSnapshot.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "DOMSnapshot.enable",
            params
        )

    def get_snapshot(
        self,
        computed_style_whitelist: list,
        include_event_listeners: MaybeUndefined[],
        include_paint_order: MaybeUndefined[],
        include_user_agent_shadow_tree: MaybeUndefined[]
    ):
        params = {
            "computedStyleWhitelist": computed_style_whitelist,
        }

        if is_defined(
            include_event_listeners
        ):
            params[] = include_event_listeners

        if is_defined(
            include_paint_order
        ):
            params[] = include_paint_order

        if is_defined(
            include_user_agent_shadow_tree
        ):
            params[] = include_user_agent_shadow_tree

        return self._send_command(
            "DOMSnapshot.getSnapshot",
            params
        )

    def capture_snapshot(
        self,
        computed_styles: list,
        include_paint_order: MaybeUndefined[],
        include_dom_rects: MaybeUndefined[],
        include_blended_background_colors: MaybeUndefined[],
        include_text_color_opacities: MaybeUndefined[]
    ):
        params = {
            "computedStyles": computed_styles,
        }

        if is_defined(
            include_paint_order
        ):
            params[] = include_paint_order

        if is_defined(
            include_dom_rects
        ):
            params[] = include_dom_rects

        if is_defined(
            include_blended_background_colors
        ):
            params[] = include_blended_background_colors

        if is_defined(
            include_text_color_opacities
        ):
            params[] = include_text_color_opacities

        return self._send_command(
            "DOMSnapshot.captureSnapshot",
            params
        )

