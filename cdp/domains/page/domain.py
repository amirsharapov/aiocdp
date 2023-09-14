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
from cdp.domains.page.types import (
    AppManifestParsedProperties,
    FrameTree,
    BackForwardCacheNotRestoredReasonType,
    LayoutViewport,
    FrameResourceTree,
    FrameId,
    OriginTrialStatus,
    PermissionsPolicyBlockLocator,
    AdFrameType,
    BackForwardCacheNotRestoredExplanationTree,
    Viewport,
    ScreencastFrameMetadata,
    OriginTrialToken,
    CrossOriginIsolatedContextType,
    AdFrameStatus,
    SecureContextType,
    PermissionsPolicyBlockReason,
    ScriptIdentifier,
    ClientNavigationReason,
    ClientNavigationDisposition,
    Frame,
    VisualViewport,
    FontFamilies,
    BackForwardCacheNotRestoredReason,
    NavigationType,
    TransitionType,
    FontSizes,
    OriginTrialUsageRestriction,
    ReferrerPolicy,
    DialogType,
    PermissionsPolicyFeature,
    OriginTrialTokenStatus,
    AutoResponseMode,
    AdScriptId
)
from cdp.domains.runtime.types import (
    UniqueDebuggerId,
    ScriptId,
    ExecutionContextId,
    StackTrace
)
from cdp.domains.network.types import (
    ResourceType,
    TimeSinceEpoch,
    MonotonicTime,
    LoaderId
)
from cdp.domains.dom.types import (
    Rect,
    BackendNodeId
)
from cdp.domains.io.types import (
    StreamHandle
)
from cdp.domains.emulation.types import (
    ScreenOrientation
)


@dataclass
class Page(BaseDomain):
    def add_script_to_evaluate_on_load(
        self,
        script_source: str
    ):
        params = {
            "scriptSource": script_source,
        }

        return self._send_command(
            "Page.addScriptToEvaluateOnLoad",
            params
        )

    def add_script_to_evaluate_on_new_document(
        self,
        source: str,
        world_name: MaybeUndefined[],
        include_command_line_api: MaybeUndefined[],
        run_immediately: MaybeUndefined[]
    ):
        params = {
            "source": source,
        }

        if is_defined(
            world_name
        ):
            params[] = world_name

        if is_defined(
            include_command_line_api
        ):
            params[] = include_command_line_api

        if is_defined(
            run_immediately
        ):
            params[] = run_immediately

        return self._send_command(
            "Page.addScriptToEvaluateOnNewDocument",
            params
        )

    def bring_to_front(
        self
    ):
        params = {}

        return self._send_command(
            "Page.bringToFront",
            params
        )

    def capture_screenshot(
        self,
        format_: MaybeUndefined[],
        quality: MaybeUndefined[],
        clip: MaybeUndefined[],
        from_surface: MaybeUndefined[],
        capture_beyond_viewport: MaybeUndefined[],
        optimize_for_speed: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            format_
        ):
            params[] = format_

        if is_defined(
            quality
        ):
            params[] = quality

        if is_defined(
            clip
        ):
            params[] = clip

        if is_defined(
            from_surface
        ):
            params[] = from_surface

        if is_defined(
            capture_beyond_viewport
        ):
            params[] = capture_beyond_viewport

        if is_defined(
            optimize_for_speed
        ):
            params[] = optimize_for_speed

        return self._send_command(
            "Page.captureScreenshot",
            params
        )

    def capture_snapshot(
        self,
        format_: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            format_
        ):
            params[] = format_

        return self._send_command(
            "Page.captureSnapshot",
            params
        )

    def clear_device_metrics_override(
        self
    ):
        params = {}

        return self._send_command(
            "Page.clearDeviceMetricsOverride",
            params
        )

    def clear_device_orientation_override(
        self
    ):
        params = {}

        return self._send_command(
            "Page.clearDeviceOrientationOverride",
            params
        )

    def clear_geolocation_override(
        self
    ):
        params = {}

        return self._send_command(
            "Page.clearGeolocationOverride",
            params
        )

    def create_isolated_world(
        self,
        frame_id: FrameId,
        world_name: MaybeUndefined[],
        grant_univeral_access: MaybeUndefined[]
    ):
        params = {
            "frameId": frame_id,
        }

        if is_defined(
            world_name
        ):
            params[] = world_name

        if is_defined(
            grant_univeral_access
        ):
            params[] = grant_univeral_access

        return self._send_command(
            "Page.createIsolatedWorld",
            params
        )

    def delete_cookie(
        self,
        cookie_name: str,
        url: str
    ):
        params = {
            "cookieName": cookie_name,
            "url": url,
        }

        return self._send_command(
            "Page.deleteCookie",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Page.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Page.enable",
            params
        )

    def get_app_manifest(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getAppManifest",
            params
        )

    def get_installability_errors(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getInstallabilityErrors",
            params
        )

    def get_manifest_icons(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getManifestIcons",
            params
        )

    def get_app_id(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getAppId",
            params
        )

    def get_ad_script_id(
        self,
        frame_id: FrameId
    ):
        params = {
            "frameId": frame_id,
        }

        return self._send_command(
            "Page.getAdScriptId",
            params
        )

    def get_cookies(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getCookies",
            params
        )

    def get_frame_tree(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getFrameTree",
            params
        )

    def get_layout_metrics(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getLayoutMetrics",
            params
        )

    def get_navigation_history(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getNavigationHistory",
            params
        )

    def reset_navigation_history(
        self
    ):
        params = {}

        return self._send_command(
            "Page.resetNavigationHistory",
            params
        )

    def get_resource_content(
        self,
        frame_id: FrameId,
        url: str
    ):
        params = {
            "frameId": frame_id,
            "url": url,
        }

        return self._send_command(
            "Page.getResourceContent",
            params
        )

    def get_resource_tree(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getResourceTree",
            params
        )

    def handle_java_script_dialog(
        self,
        accept: bool,
        prompt_text: MaybeUndefined[]
    ):
        params = {
            "accept": accept,
        }

        if is_defined(
            prompt_text
        ):
            params[] = prompt_text

        return self._send_command(
            "Page.handleJavaScriptDialog",
            params
        )

    def navigate(
        self,
        url: str,
        referrer: MaybeUndefined[],
        transition_type: MaybeUndefined[],
        frame_id: MaybeUndefined[],
        referrer_policy: MaybeUndefined[]
    ):
        params = {
            "url": url,
        }

        if is_defined(
            referrer
        ):
            params[] = referrer

        if is_defined(
            transition_type
        ):
            params[] = transition_type

        if is_defined(
            frame_id
        ):
            params[] = frame_id

        if is_defined(
            referrer_policy
        ):
            params[] = referrer_policy

        return self._send_command(
            "Page.navigate",
            params
        )

    def navigate_to_history_entry(
        self,
        entry_id: int
    ):
        params = {
            "entryId": entry_id,
        }

        return self._send_command(
            "Page.navigateToHistoryEntry",
            params
        )

    def print_to_pdf(
        self,
        landscape: MaybeUndefined[],
        display_header_footer: MaybeUndefined[],
        print_background: MaybeUndefined[],
        scale: MaybeUndefined[],
        paper_width: MaybeUndefined[],
        paper_height: MaybeUndefined[],
        margin_top: MaybeUndefined[],
        margin_bottom: MaybeUndefined[],
        margin_left: MaybeUndefined[],
        margin_right: MaybeUndefined[],
        page_ranges: MaybeUndefined[],
        header_template: MaybeUndefined[],
        footer_template: MaybeUndefined[],
        prefer_css_page_size: MaybeUndefined[],
        transfer_mode: MaybeUndefined[],
        generate_tagged_pdf: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            landscape
        ):
            params[] = landscape

        if is_defined(
            display_header_footer
        ):
            params[] = display_header_footer

        if is_defined(
            print_background
        ):
            params[] = print_background

        if is_defined(
            scale
        ):
            params[] = scale

        if is_defined(
            paper_width
        ):
            params[] = paper_width

        if is_defined(
            paper_height
        ):
            params[] = paper_height

        if is_defined(
            margin_top
        ):
            params[] = margin_top

        if is_defined(
            margin_bottom
        ):
            params[] = margin_bottom

        if is_defined(
            margin_left
        ):
            params[] = margin_left

        if is_defined(
            margin_right
        ):
            params[] = margin_right

        if is_defined(
            page_ranges
        ):
            params[] = page_ranges

        if is_defined(
            header_template
        ):
            params[] = header_template

        if is_defined(
            footer_template
        ):
            params[] = footer_template

        if is_defined(
            prefer_css_page_size
        ):
            params[] = prefer_css_page_size

        if is_defined(
            transfer_mode
        ):
            params[] = transfer_mode

        if is_defined(
            generate_tagged_pdf
        ):
            params[] = generate_tagged_pdf

        return self._send_command(
            "Page.printToPDF",
            params
        )

    def reload(
        self,
        ignore_cache: MaybeUndefined[],
        script_to_evaluate_on_load: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            ignore_cache
        ):
            params[] = ignore_cache

        if is_defined(
            script_to_evaluate_on_load
        ):
            params[] = script_to_evaluate_on_load

        return self._send_command(
            "Page.reload",
            params
        )

    def remove_script_to_evaluate_on_load(
        self,
        identifier: ScriptIdentifier
    ):
        params = {
            "identifier": identifier,
        }

        return self._send_command(
            "Page.removeScriptToEvaluateOnLoad",
            params
        )

    def remove_script_to_evaluate_on_new_document(
        self,
        identifier: ScriptIdentifier
    ):
        params = {
            "identifier": identifier,
        }

        return self._send_command(
            "Page.removeScriptToEvaluateOnNewDocument",
            params
        )

    def screencast_frame_ack(
        self,
        session_id: int
    ):
        params = {
            "sessionId": session_id,
        }

        return self._send_command(
            "Page.screencastFrameAck",
            params
        )

    def search_in_resource(
        self,
        frame_id: FrameId,
        url: str,
        query: str,
        case_sensitive: MaybeUndefined[],
        is_regex: MaybeUndefined[]
    ):
        params = {
            "frameId": frame_id,
            "url": url,
            "query": query,
        }

        if is_defined(
            case_sensitive
        ):
            params[] = case_sensitive

        if is_defined(
            is_regex
        ):
            params[] = is_regex

        return self._send_command(
            "Page.searchInResource",
            params
        )

    def set_ad_blocking_enabled(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Page.setAdBlockingEnabled",
            params
        )

    def set_bypass_csp(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Page.setBypassCSP",
            params
        )

    def get_permissions_policy_state(
        self,
        frame_id: FrameId
    ):
        params = {
            "frameId": frame_id,
        }

        return self._send_command(
            "Page.getPermissionsPolicyState",
            params
        )

    def get_origin_trials(
        self,
        frame_id: FrameId
    ):
        params = {
            "frameId": frame_id,
        }

        return self._send_command(
            "Page.getOriginTrials",
            params
        )

    def set_device_metrics_override(
        self,
        width: int,
        height: int,
        device_scale_factor: float,
        mobile: bool,
        scale: MaybeUndefined[],
        screen_width: MaybeUndefined[],
        screen_height: MaybeUndefined[],
        position_x: MaybeUndefined[],
        position_y: MaybeUndefined[],
        dont_set_visible_size: MaybeUndefined[],
        screen_orientation: MaybeUndefined[],
        viewport: MaybeUndefined[]
    ):
        params = {
            "width": width,
            "height": height,
            "deviceScaleFactor": device_scale_factor,
            "mobile": mobile,
        }

        if is_defined(
            scale
        ):
            params[] = scale

        if is_defined(
            screen_width
        ):
            params[] = screen_width

        if is_defined(
            screen_height
        ):
            params[] = screen_height

        if is_defined(
            position_x
        ):
            params[] = position_x

        if is_defined(
            position_y
        ):
            params[] = position_y

        if is_defined(
            dont_set_visible_size
        ):
            params[] = dont_set_visible_size

        if is_defined(
            screen_orientation
        ):
            params[] = screen_orientation

        if is_defined(
            viewport
        ):
            params[] = viewport

        return self._send_command(
            "Page.setDeviceMetricsOverride",
            params
        )

    def set_device_orientation_override(
        self,
        alpha: float,
        beta: float,
        gamma: float
    ):
        params = {
            "alpha": alpha,
            "beta": beta,
            "gamma": gamma,
        }

        return self._send_command(
            "Page.setDeviceOrientationOverride",
            params
        )

    def set_font_families(
        self,
        font_families: FontFamilies,
        for_scripts: MaybeUndefined[]
    ):
        params = {
            "fontFamilies": font_families,
        }

        if is_defined(
            for_scripts
        ):
            params[] = for_scripts

        return self._send_command(
            "Page.setFontFamilies",
            params
        )

    def set_font_sizes(
        self,
        font_sizes: FontSizes
    ):
        params = {
            "fontSizes": font_sizes,
        }

        return self._send_command(
            "Page.setFontSizes",
            params
        )

    def set_document_content(
        self,
        frame_id: FrameId,
        html: str
    ):
        params = {
            "frameId": frame_id,
            "html": html,
        }

        return self._send_command(
            "Page.setDocumentContent",
            params
        )

    def set_download_behavior(
        self,
        behavior: str,
        download_path: MaybeUndefined[]
    ):
        params = {
            "behavior": behavior,
        }

        if is_defined(
            download_path
        ):
            params[] = download_path

        return self._send_command(
            "Page.setDownloadBehavior",
            params
        )

    def set_geolocation_override(
        self,
        latitude: MaybeUndefined[],
        longitude: MaybeUndefined[],
        accuracy: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            latitude
        ):
            params[] = latitude

        if is_defined(
            longitude
        ):
            params[] = longitude

        if is_defined(
            accuracy
        ):
            params[] = accuracy

        return self._send_command(
            "Page.setGeolocationOverride",
            params
        )

    def set_lifecycle_events_enabled(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Page.setLifecycleEventsEnabled",
            params
        )

    def set_touch_emulation_enabled(
        self,
        enabled: bool,
        configuration: MaybeUndefined[]
    ):
        params = {
            "enabled": enabled,
        }

        if is_defined(
            configuration
        ):
            params[] = configuration

        return self._send_command(
            "Page.setTouchEmulationEnabled",
            params
        )

    def start_screencast(
        self,
        format_: MaybeUndefined[],
        quality: MaybeUndefined[],
        max_width: MaybeUndefined[],
        max_height: MaybeUndefined[],
        every_nth_frame: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            format_
        ):
            params[] = format_

        if is_defined(
            quality
        ):
            params[] = quality

        if is_defined(
            max_width
        ):
            params[] = max_width

        if is_defined(
            max_height
        ):
            params[] = max_height

        if is_defined(
            every_nth_frame
        ):
            params[] = every_nth_frame

        return self._send_command(
            "Page.startScreencast",
            params
        )

    def stop_loading(
        self
    ):
        params = {}

        return self._send_command(
            "Page.stopLoading",
            params
        )

    def crash(
        self
    ):
        params = {}

        return self._send_command(
            "Page.crash",
            params
        )

    def close(
        self
    ):
        params = {}

        return self._send_command(
            "Page.close",
            params
        )

    def set_web_lifecycle_state(
        self,
        state: str
    ):
        params = {
            "state": state,
        }

        return self._send_command(
            "Page.setWebLifecycleState",
            params
        )

    def stop_screencast(
        self
    ):
        params = {}

        return self._send_command(
            "Page.stopScreencast",
            params
        )

    def produce_compilation_cache(
        self,
        scripts: list
    ):
        params = {
            "scripts": scripts,
        }

        return self._send_command(
            "Page.produceCompilationCache",
            params
        )

    def add_compilation_cache(
        self,
        url: str,
        data: str
    ):
        params = {
            "url": url,
            "data": data,
        }

        return self._send_command(
            "Page.addCompilationCache",
            params
        )

    def clear_compilation_cache(
        self
    ):
        params = {}

        return self._send_command(
            "Page.clearCompilationCache",
            params
        )

    def set_spc_transaction_mode(
        self,
        mode: AutoResponseMode
    ):
        params = {
            "mode": mode,
        }

        return self._send_command(
            "Page.setSPCTransactionMode",
            params
        )

    def set_rph_registration_mode(
        self,
        mode: AutoResponseMode
    ):
        params = {
            "mode": mode,
        }

        return self._send_command(
            "Page.setRPHRegistrationMode",
            params
        )

    def generate_test_report(
        self,
        message: str,
        group: MaybeUndefined[]
    ):
        params = {
            "message": message,
        }

        if is_defined(
            group
        ):
            params[] = group

        return self._send_command(
            "Page.generateTestReport",
            params
        )

    def wait_for_debugger(
        self
    ):
        params = {}

        return self._send_command(
            "Page.waitForDebugger",
            params
        )

    def set_intercept_file_chooser_dialog(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Page.setInterceptFileChooserDialog",
            params
        )

    def set_prerendering_allowed(
        self,
        is_allowed: bool
    ):
        params = {
            "isAllowed": is_allowed,
        }

        return self._send_command(
            "Page.setPrerenderingAllowed",
            params
        )

