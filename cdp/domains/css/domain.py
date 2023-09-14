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
from cdp.domains.css.types import (
    CSSScope,
    StyleSheetId,
    CSSContainerQuery,
    SelectorList,
    CSSMedia,
    SourceRange,
    CSSRule,
    Value,
    CSSLayerData,
    CSSStyle,
    CSSSupports
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.dom.types import (
    NodeId
)


@dataclass
class CSS(BaseDomain):
    def add_rule(
        self,
        style_sheet_id: StyleSheetId,
        rule_text: str,
        location: SourceRange
    ):
        params = {
            "styleSheetId": style_sheet_id,
            "ruleText": rule_text,
            "location": location,
        }

        return self._send_command(
            "CSS.addRule",
            params
        )

    def collect_class_names(
        self,
        style_sheet_id: StyleSheetId
    ):
        params = {
            "styleSheetId": style_sheet_id,
        }

        return self._send_command(
            "CSS.collectClassNames",
            params
        )

    def create_style_sheet(
        self,
        frame_id: FrameId
    ):
        params = {
            "frameId": frame_id,
        }

        return self._send_command(
            "CSS.createStyleSheet",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "CSS.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "CSS.enable",
            params
        )

    def force_pseudo_state(
        self,
        node_id: NodeId,
        forced_pseudo_classes: list
    ):
        params = {
            "nodeId": node_id,
            "forcedPseudoClasses": forced_pseudo_classes,
        }

        return self._send_command(
            "CSS.forcePseudoState",
            params
        )

    def get_background_colors(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "CSS.getBackgroundColors",
            params
        )

    def get_computed_style_for_node(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "CSS.getComputedStyleForNode",
            params
        )

    def get_inline_styles_for_node(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "CSS.getInlineStylesForNode",
            params
        )

    def get_matched_styles_for_node(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "CSS.getMatchedStylesForNode",
            params
        )

    def get_media_queries(
        self
    ):
        params = {}

        return self._send_command(
            "CSS.getMediaQueries",
            params
        )

    def get_platform_fonts_for_node(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "CSS.getPlatformFontsForNode",
            params
        )

    def get_style_sheet_text(
        self,
        style_sheet_id: StyleSheetId
    ):
        params = {
            "styleSheetId": style_sheet_id,
        }

        return self._send_command(
            "CSS.getStyleSheetText",
            params
        )

    def get_layers_for_node(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "CSS.getLayersForNode",
            params
        )

    def track_computed_style_updates(
        self,
        properties_to_track: list
    ):
        params = {
            "propertiesToTrack": properties_to_track,
        }

        return self._send_command(
            "CSS.trackComputedStyleUpdates",
            params
        )

    def take_computed_style_updates(
        self
    ):
        params = {}

        return self._send_command(
            "CSS.takeComputedStyleUpdates",
            params
        )

    def set_effective_property_value_for_node(
        self,
        node_id: NodeId,
        property_name: str,
        value: str
    ):
        params = {
            "nodeId": node_id,
            "propertyName": property_name,
            "value": value,
        }

        return self._send_command(
            "CSS.setEffectivePropertyValueForNode",
            params
        )

    def set_keyframe_key(
        self,
        style_sheet_id: StyleSheetId,
        range_: SourceRange,
        key_text: str
    ):
        params = {
            "styleSheetId": style_sheet_id,
            "range": range_,
            "keyText": key_text,
        }

        return self._send_command(
            "CSS.setKeyframeKey",
            params
        )

    def set_media_text(
        self,
        style_sheet_id: StyleSheetId,
        range_: SourceRange,
        text: str
    ):
        params = {
            "styleSheetId": style_sheet_id,
            "range": range_,
            "text": text,
        }

        return self._send_command(
            "CSS.setMediaText",
            params
        )

    def set_container_query_text(
        self,
        style_sheet_id: StyleSheetId,
        range_: SourceRange,
        text: str
    ):
        params = {
            "styleSheetId": style_sheet_id,
            "range": range_,
            "text": text,
        }

        return self._send_command(
            "CSS.setContainerQueryText",
            params
        )

    def set_supports_text(
        self,
        style_sheet_id: StyleSheetId,
        range_: SourceRange,
        text: str
    ):
        params = {
            "styleSheetId": style_sheet_id,
            "range": range_,
            "text": text,
        }

        return self._send_command(
            "CSS.setSupportsText",
            params
        )

    def set_scope_text(
        self,
        style_sheet_id: StyleSheetId,
        range_: SourceRange,
        text: str
    ):
        params = {
            "styleSheetId": style_sheet_id,
            "range": range_,
            "text": text,
        }

        return self._send_command(
            "CSS.setScopeText",
            params
        )

    def set_rule_selector(
        self,
        style_sheet_id: StyleSheetId,
        range_: SourceRange,
        selector: str
    ):
        params = {
            "styleSheetId": style_sheet_id,
            "range": range_,
            "selector": selector,
        }

        return self._send_command(
            "CSS.setRuleSelector",
            params
        )

    def set_style_sheet_text(
        self,
        style_sheet_id: StyleSheetId,
        text: str
    ):
        params = {
            "styleSheetId": style_sheet_id,
            "text": text,
        }

        return self._send_command(
            "CSS.setStyleSheetText",
            params
        )

    def set_style_texts(
        self,
        edits: list
    ):
        params = {
            "edits": edits,
        }

        return self._send_command(
            "CSS.setStyleTexts",
            params
        )

    def start_rule_usage_tracking(
        self
    ):
        params = {}

        return self._send_command(
            "CSS.startRuleUsageTracking",
            params
        )

    def stop_rule_usage_tracking(
        self
    ):
        params = {}

        return self._send_command(
            "CSS.stopRuleUsageTracking",
            params
        )

    def take_coverage_delta(
        self
    ):
        params = {}

        return self._send_command(
            "CSS.takeCoverageDelta",
            params
        )

    def set_local_fonts_enabled(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "CSS.setLocalFontsEnabled",
            params
        )

