# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)
from cdp.domains.css.types import (
    AddRuleReturnT,
    CollectClassNamesReturnT,
    CreateStyleSheetReturnT,
    GetBackgroundColorsReturnT,
    GetComputedStyleForNodeReturnT,
    GetInlineStylesForNodeReturnT,
    GetLayersForNodeReturnT,
    GetMatchedStylesForNodeReturnT,
    GetMediaQueriesReturnT,
    GetPlatformFontsForNodeReturnT,
    GetStyleSheetTextReturnT,
    SetContainerQueryTextReturnT,
    SetKeyframeKeyReturnT,
    SetMediaTextReturnT,
    SetRuleSelectorReturnT,
    SetScopeTextReturnT,
    SetStyleSheetTextReturnT,
    SetStyleTextsReturnT,
    SetSupportsTextReturnT,
    SourceRange,
    StopRuleUsageTrackingReturnT,
    StyleSheetId,
    TakeComputedStyleUpdatesReturnT,
    TakeCoverageDeltaReturnT
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.dom.types import (
    NodeId
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResult
    )


@dataclass
class CSS(BaseDomain):
    def add_rule(
            self,
            style_sheet_id: StyleSheetId,
            rule_text: str,
            location: SourceRange
    ) -> IResult['AddRuleReturnT']:
        params = {
            'styleSheetId': style_sheet_id,
            'ruleText': rule_text,
            'location': location,
        }

        return self._send_command(
            'CSS.addRule',
            params,
            True
        )

    def collect_class_names(
            self,
            style_sheet_id: StyleSheetId
    ) -> IResult['CollectClassNamesReturnT']:
        params = {
            'styleSheetId': style_sheet_id,
        }

        return self._send_command(
            'CSS.collectClassNames',
            params,
            True
        )

    def create_style_sheet(
            self,
            frame_id: FrameId
    ) -> IResult['CreateStyleSheetReturnT']:
        params = {
            'frameId': frame_id,
        }

        return self._send_command(
            'CSS.createStyleSheet',
            params,
            True
        )

    def disable(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'CSS.disable',
            params,
            False
        )

    def enable(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'CSS.enable',
            params,
            False
        )

    def force_pseudo_state(
            self,
            node_id: NodeId,
            forced_pseudo_classes: list
    ) -> IResult[None]:
        params = {
            'nodeId': node_id,
            'forcedPseudoClasses': forced_pseudo_classes,
        }

        return self._send_command(
            'CSS.forcePseudoState',
            params,
            False
        )

    def get_background_colors(
            self,
            node_id: NodeId
    ) -> IResult['GetBackgroundColorsReturnT']:
        params = {
            'nodeId': node_id,
        }

        return self._send_command(
            'CSS.getBackgroundColors',
            params,
            True
        )

    def get_computed_style_for_node(
            self,
            node_id: NodeId
    ) -> IResult['GetComputedStyleForNodeReturnT']:
        params = {
            'nodeId': node_id,
        }

        return self._send_command(
            'CSS.getComputedStyleForNode',
            params,
            True
        )

    def get_inline_styles_for_node(
            self,
            node_id: NodeId
    ) -> IResult['GetInlineStylesForNodeReturnT']:
        params = {
            'nodeId': node_id,
        }

        return self._send_command(
            'CSS.getInlineStylesForNode',
            params,
            True
        )

    def get_matched_styles_for_node(
            self,
            node_id: NodeId
    ) -> IResult['GetMatchedStylesForNodeReturnT']:
        params = {
            'nodeId': node_id,
        }

        return self._send_command(
            'CSS.getMatchedStylesForNode',
            params,
            True
        )

    def get_media_queries(
            self
    ) -> IResult['GetMediaQueriesReturnT']:
        params = {}

        return self._send_command(
            'CSS.getMediaQueries',
            params,
            True
        )

    def get_platform_fonts_for_node(
            self,
            node_id: NodeId
    ) -> IResult['GetPlatformFontsForNodeReturnT']:
        params = {
            'nodeId': node_id,
        }

        return self._send_command(
            'CSS.getPlatformFontsForNode',
            params,
            True
        )

    def get_style_sheet_text(
            self,
            style_sheet_id: StyleSheetId
    ) -> IResult['GetStyleSheetTextReturnT']:
        params = {
            'styleSheetId': style_sheet_id,
        }

        return self._send_command(
            'CSS.getStyleSheetText',
            params,
            True
        )

    def get_layers_for_node(
            self,
            node_id: NodeId
    ) -> IResult['GetLayersForNodeReturnT']:
        params = {
            'nodeId': node_id,
        }

        return self._send_command(
            'CSS.getLayersForNode',
            params,
            True
        )

    def track_computed_style_updates(
            self,
            properties_to_track: list
    ) -> IResult[None]:
        params = {
            'propertiesToTrack': properties_to_track,
        }

        return self._send_command(
            'CSS.trackComputedStyleUpdates',
            params,
            False
        )

    def take_computed_style_updates(
            self
    ) -> IResult['TakeComputedStyleUpdatesReturnT']:
        params = {}

        return self._send_command(
            'CSS.takeComputedStyleUpdates',
            params,
            True
        )

    def set_effective_property_value_for_node(
            self,
            node_id: NodeId,
            property_name: str,
            value: str
    ) -> IResult[None]:
        params = {
            'nodeId': node_id,
            'propertyName': property_name,
            'value': value,
        }

        return self._send_command(
            'CSS.setEffectivePropertyValueForNode',
            params,
            False
        )

    def set_keyframe_key(
            self,
            style_sheet_id: StyleSheetId,
            range_: SourceRange,
            key_text: str
    ) -> IResult['SetKeyframeKeyReturnT']:
        params = {
            'styleSheetId': style_sheet_id,
            'range': range_,
            'keyText': key_text,
        }

        return self._send_command(
            'CSS.setKeyframeKey',
            params,
            True
        )

    def set_media_text(
            self,
            style_sheet_id: StyleSheetId,
            range_: SourceRange,
            text: str
    ) -> IResult['SetMediaTextReturnT']:
        params = {
            'styleSheetId': style_sheet_id,
            'range': range_,
            'text': text,
        }

        return self._send_command(
            'CSS.setMediaText',
            params,
            True
        )

    def set_container_query_text(
            self,
            style_sheet_id: StyleSheetId,
            range_: SourceRange,
            text: str
    ) -> IResult['SetContainerQueryTextReturnT']:
        params = {
            'styleSheetId': style_sheet_id,
            'range': range_,
            'text': text,
        }

        return self._send_command(
            'CSS.setContainerQueryText',
            params,
            True
        )

    def set_supports_text(
            self,
            style_sheet_id: StyleSheetId,
            range_: SourceRange,
            text: str
    ) -> IResult['SetSupportsTextReturnT']:
        params = {
            'styleSheetId': style_sheet_id,
            'range': range_,
            'text': text,
        }

        return self._send_command(
            'CSS.setSupportsText',
            params,
            True
        )

    def set_scope_text(
            self,
            style_sheet_id: StyleSheetId,
            range_: SourceRange,
            text: str
    ) -> IResult['SetScopeTextReturnT']:
        params = {
            'styleSheetId': style_sheet_id,
            'range': range_,
            'text': text,
        }

        return self._send_command(
            'CSS.setScopeText',
            params,
            True
        )

    def set_rule_selector(
            self,
            style_sheet_id: StyleSheetId,
            range_: SourceRange,
            selector: str
    ) -> IResult['SetRuleSelectorReturnT']:
        params = {
            'styleSheetId': style_sheet_id,
            'range': range_,
            'selector': selector,
        }

        return self._send_command(
            'CSS.setRuleSelector',
            params,
            True
        )

    def set_style_sheet_text(
            self,
            style_sheet_id: StyleSheetId,
            text: str
    ) -> IResult['SetStyleSheetTextReturnT']:
        params = {
            'styleSheetId': style_sheet_id,
            'text': text,
        }

        return self._send_command(
            'CSS.setStyleSheetText',
            params,
            True
        )

    def set_style_texts(
            self,
            edits: list
    ) -> IResult['SetStyleTextsReturnT']:
        params = {
            'edits': edits,
        }

        return self._send_command(
            'CSS.setStyleTexts',
            params,
            True
        )

    def start_rule_usage_tracking(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'CSS.startRuleUsageTracking',
            params,
            False
        )

    def stop_rule_usage_tracking(
            self
    ) -> IResult['StopRuleUsageTrackingReturnT']:
        params = {}

        return self._send_command(
            'CSS.stopRuleUsageTracking',
            params,
            True
        )

    def take_coverage_delta(
            self
    ) -> IResult['TakeCoverageDeltaReturnT']:
        params = {}

        return self._send_command(
            'CSS.takeCoverageDelta',
            params,
            True
        )

    def set_local_fonts_enabled(
            self,
            enabled: bool
    ) -> IResult[None]:
        params = {
            'enabled': enabled,
        }

        return self._send_command(
            'CSS.setLocalFontsEnabled',
            params,
            False
        )
