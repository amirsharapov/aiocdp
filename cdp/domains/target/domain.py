from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.domains.target.types import (
    SessionID,
    TargetFilter,
    TargetID,
    TargetInfo
)
from cdp.domains.browser.types import (
    BrowserContextID
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)


@dataclass
class Target(BaseDomain):
    def activate_target(
        self,
        target_id: TargetID
    ):
        params = {
            "targetId": target_id,
        }

        return self._send_command(
            "Target.activateTarget",
            params
        )

    def attach_to_target(
        self,
        target_id: TargetID,
        flatten: bool = UNDEFINED
    ):
        params = {
            "targetId": target_id,
        }

        if is_defined(
            flatten
        ):
            params["flatten"] = flatten

        return self._send_command(
            "Target.attachToTarget",
            params
        )

    def attach_to_browser_target(
        self
    ):
        params = {}

        return self._send_command(
            "Target.attachToBrowserTarget",
            params
        )

    def close_target(
        self,
        target_id: TargetID
    ):
        params = {
            "targetId": target_id,
        }

        return self._send_command(
            "Target.closeTarget",
            params
        )

    def expose_dev_tools_protocol(
        self,
        target_id: TargetID,
        binding_name: str = UNDEFINED
    ):
        params = {
            "targetId": target_id,
        }

        if is_defined(
            binding_name
        ):
            params["bindingName"] = binding_name

        return self._send_command(
            "Target.exposeDevToolsProtocol",
            params
        )

    def create_browser_context(
        self,
        dispose_on_detach: bool = UNDEFINED,
        proxy_server: str = UNDEFINED,
        proxy_bypass_list: str = UNDEFINED,
        origins_with_universal_network_access: list = UNDEFINED
    ):
        params = {}

        if is_defined(
            dispose_on_detach
        ):
            params["disposeOnDetach"] = dispose_on_detach

        if is_defined(
            proxy_server
        ):
            params["proxyServer"] = proxy_server

        if is_defined(
            proxy_bypass_list
        ):
            params["proxyBypassList"] = proxy_bypass_list

        if is_defined(
            origins_with_universal_network_access
        ):
            params["originsWithUniversalNetworkAccess"] = origins_with_universal_network_access

        return self._send_command(
            "Target.createBrowserContext",
            params
        )

    def get_browser_contexts(
        self
    ):
        params = {}

        return self._send_command(
            "Target.getBrowserContexts",
            params
        )

    def create_target(
        self,
        url: str,
        width: int = UNDEFINED,
        height: int = UNDEFINED,
        browser_context_id: BrowserContextID = UNDEFINED,
        enable_begin_frame_control: bool = UNDEFINED,
        new_window: bool = UNDEFINED,
        background: bool = UNDEFINED,
        for_tab: bool = UNDEFINED
    ):
        params = {
            "url": url,
        }

        if is_defined(
            width
        ):
            params["width"] = width

        if is_defined(
            height
        ):
            params["height"] = height

        if is_defined(
            browser_context_id
        ):
            params["browserContextId"] = browser_context_id

        if is_defined(
            enable_begin_frame_control
        ):
            params["enableBeginFrameControl"] = enable_begin_frame_control

        if is_defined(
            new_window
        ):
            params["newWindow"] = new_window

        if is_defined(
            background
        ):
            params["background"] = background

        if is_defined(
            for_tab
        ):
            params["forTab"] = for_tab

        return self._send_command(
            "Target.createTarget",
            params
        )

    def detach_from_target(
        self,
        session_id: SessionID = UNDEFINED,
        target_id: TargetID = UNDEFINED
    ):
        params = {}

        if is_defined(
            session_id
        ):
            params["sessionId"] = session_id

        if is_defined(
            target_id
        ):
            params["targetId"] = target_id

        return self._send_command(
            "Target.detachFromTarget",
            params
        )

    def dispose_browser_context(
        self,
        browser_context_id: BrowserContextID
    ):
        params = {
            "browserContextId": browser_context_id,
        }

        return self._send_command(
            "Target.disposeBrowserContext",
            params
        )

    def get_target_info(
        self,
        target_id: TargetID = UNDEFINED
    ):
        params = {}

        if is_defined(
            target_id
        ):
            params["targetId"] = target_id

        return self._send_command(
            "Target.getTargetInfo",
            params
        )

    def get_targets(
        self,
        filter_: TargetFilter = UNDEFINED
    ):
        params = {}

        if is_defined(
            filter
        ):
            params["filter"] = filter

        return self._send_command(
            "Target.getTargets",
            params
        )

    def send_message_to_target(
        self,
        message: str,
        session_id: SessionID = UNDEFINED,
        target_id: TargetID = UNDEFINED
    ):
        params = {
            "message": message,
        }

        if is_defined(
            session_id
        ):
            params["sessionId"] = session_id

        if is_defined(
            target_id
        ):
            params["targetId"] = target_id

        return self._send_command(
            "Target.sendMessageToTarget",
            params
        )

    def set_auto_attach(
        self,
        auto_attach: bool,
        wait_for_debugger_on_start: bool,
        flatten: bool = UNDEFINED,
        filter_: TargetFilter = UNDEFINED
    ):
        params = {
            "autoAttach": auto_attach,
            "waitForDebuggerOnStart": wait_for_debugger_on_start,
        }

        if is_defined(
            flatten
        ):
            params["flatten"] = flatten

        if is_defined(
            filter
        ):
            params["filter"] = filter

        return self._send_command(
            "Target.setAutoAttach",
            params
        )

    def auto_attach_related(
        self,
        target_id: TargetID,
        wait_for_debugger_on_start: bool,
        filter_: TargetFilter = UNDEFINED
    ):
        params = {
            "targetId": target_id,
            "waitForDebuggerOnStart": wait_for_debugger_on_start,
        }

        if is_defined(
            filter
        ):
            params["filter"] = filter

        return self._send_command(
            "Target.autoAttachRelated",
            params
        )

    def set_discover_targets(
        self,
        discover: bool,
        filter_: TargetFilter = UNDEFINED
    ):
        params = {
            "discover": discover,
        }

        if is_defined(
            filter
        ):
            params["filter"] = filter

        return self._send_command(
            "Target.setDiscoverTargets",
            params
        )

    def set_remote_locations(
        self,
        locations: list
    ):
        params = {
            "locations": locations,
        }

        return self._send_command(
            "Target.setRemoteLocations",
            params
        )

