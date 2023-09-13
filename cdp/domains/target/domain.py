from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.target.types import (
    TargetFilter,
    TargetID,
    TargetInfo,
    SessionID
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.browser.types import (
    BrowserContextID
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
        flatten: MaybeUndefined[bool]
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
        binding_name: MaybeUndefined[str]
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
        dispose_on_detach: MaybeUndefined[bool],
        proxy_server: MaybeUndefined[str],
        proxy_bypass_list: MaybeUndefined[str],
        origins_with_universal_network_access: MaybeUndefined[list]
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
        width: MaybeUndefined[int],
        height: MaybeUndefined[int],
        browser_context_id: MaybeUndefined[BrowserContextID],
        enable_begin_frame_control: MaybeUndefined[bool],
        new_window: MaybeUndefined[bool],
        background: MaybeUndefined[bool],
        for_tab: MaybeUndefined[bool]
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
        session_id: MaybeUndefined[SessionID],
        target_id: MaybeUndefined[TargetID]
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
        target_id: MaybeUndefined[TargetID]
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
        filter_: MaybeUndefined[TargetFilter]
    ):
        params = {}

        if is_defined(
            filter_
        ):
            params["filter"] = filter_

        return self._send_command(
            "Target.getTargets",
            params
        )

    def send_message_to_target(
        self,
        message: str,
        session_id: MaybeUndefined[SessionID],
        target_id: MaybeUndefined[TargetID]
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
        flatten: MaybeUndefined[bool],
        filter_: MaybeUndefined[TargetFilter]
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
            filter_
        ):
            params["filter"] = filter_

        return self._send_command(
            "Target.setAutoAttach",
            params
        )

    def auto_attach_related(
        self,
        target_id: TargetID,
        wait_for_debugger_on_start: bool,
        filter_: MaybeUndefined[TargetFilter]
    ):
        params = {
            "targetId": target_id,
            "waitForDebuggerOnStart": wait_for_debugger_on_start,
        }

        if is_defined(
            filter_
        ):
            params["filter"] = filter_

        return self._send_command(
            "Target.autoAttachRelated",
            params
        )

    def set_discover_targets(
        self,
        discover: bool,
        filter_: MaybeUndefined[TargetFilter]
    ):
        params = {
            "discover": discover,
        }

        if is_defined(
            filter_
        ):
            params["filter"] = filter_

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

