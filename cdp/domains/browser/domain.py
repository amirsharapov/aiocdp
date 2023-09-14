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
from cdp.domains.browser.types import (
    PermissionDescriptor,
    WindowID,
    WindowState,
    BrowserContextID,
    BrowserCommandId,
    PermissionSetting,
    Histogram,
    Bounds
)
from cdp.domains.target.types import (
    TargetID
)
from cdp.domains.page.types import (
    FrameId
)


@dataclass
class Browser(BaseDomain):
    def set_permission(
        self,
        permission: PermissionDescriptor,
        setting: PermissionSetting,
        origin: MaybeUndefined[],
        browser_context_id: MaybeUndefined[]
    ):
        params = {
            "permission": permission,
            "setting": setting,
        }

        if is_defined(
            origin
        ):
            params[] = origin

        if is_defined(
            browser_context_id
        ):
            params[] = browser_context_id

        return self._send_command(
            "Browser.setPermission",
            params
        )

    def grant_permissions(
        self,
        permissions: list,
        origin: MaybeUndefined[],
        browser_context_id: MaybeUndefined[]
    ):
        params = {
            "permissions": permissions,
        }

        if is_defined(
            origin
        ):
            params[] = origin

        if is_defined(
            browser_context_id
        ):
            params[] = browser_context_id

        return self._send_command(
            "Browser.grantPermissions",
            params
        )

    def reset_permissions(
        self,
        browser_context_id: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            browser_context_id
        ):
            params[] = browser_context_id

        return self._send_command(
            "Browser.resetPermissions",
            params
        )

    def set_download_behavior(
        self,
        behavior: str,
        browser_context_id: MaybeUndefined[],
        download_path: MaybeUndefined[],
        events_enabled: MaybeUndefined[]
    ):
        params = {
            "behavior": behavior,
        }

        if is_defined(
            browser_context_id
        ):
            params[] = browser_context_id

        if is_defined(
            download_path
        ):
            params[] = download_path

        if is_defined(
            events_enabled
        ):
            params[] = events_enabled

        return self._send_command(
            "Browser.setDownloadBehavior",
            params
        )

    def cancel_download(
        self,
        guid: str,
        browser_context_id: MaybeUndefined[]
    ):
        params = {
            "guid": guid,
        }

        if is_defined(
            browser_context_id
        ):
            params[] = browser_context_id

        return self._send_command(
            "Browser.cancelDownload",
            params
        )

    def close(
        self
    ):
        params = {}

        return self._send_command(
            "Browser.close",
            params
        )

    def crash(
        self
    ):
        params = {}

        return self._send_command(
            "Browser.crash",
            params
        )

    def crash_gpu_process(
        self
    ):
        params = {}

        return self._send_command(
            "Browser.crashGpuProcess",
            params
        )

    def get_version(
        self
    ):
        params = {}

        return self._send_command(
            "Browser.getVersion",
            params
        )

    def get_browser_command_line(
        self
    ):
        params = {}

        return self._send_command(
            "Browser.getBrowserCommandLine",
            params
        )

    def get_histograms(
        self,
        query: MaybeUndefined[],
        delta: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            query
        ):
            params[] = query

        if is_defined(
            delta
        ):
            params[] = delta

        return self._send_command(
            "Browser.getHistograms",
            params
        )

    def get_histogram(
        self,
        name: str,
        delta: MaybeUndefined[]
    ):
        params = {
            "name": name,
        }

        if is_defined(
            delta
        ):
            params[] = delta

        return self._send_command(
            "Browser.getHistogram",
            params
        )

    def get_window_bounds(
        self,
        window_id: WindowID
    ):
        params = {
            "windowId": window_id,
        }

        return self._send_command(
            "Browser.getWindowBounds",
            params
        )

    def get_window_for_target(
        self,
        target_id: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            target_id
        ):
            params[] = target_id

        return self._send_command(
            "Browser.getWindowForTarget",
            params
        )

    def set_window_bounds(
        self,
        window_id: WindowID,
        bounds: Bounds
    ):
        params = {
            "windowId": window_id,
            "bounds": bounds,
        }

        return self._send_command(
            "Browser.setWindowBounds",
            params
        )

    def set_dock_tile(
        self,
        badge_label: MaybeUndefined[],
        image: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            badge_label
        ):
            params[] = badge_label

        if is_defined(
            image
        ):
            params[] = image

        return self._send_command(
            "Browser.setDockTile",
            params
        )

    def execute_browser_command(
        self,
        command_id: BrowserCommandId
    ):
        params = {
            "commandId": command_id,
        }

        return self._send_command(
            "Browser.executeBrowserCommand",
            params
        )

    def add_privacy_sandbox_enrollment_override(
        self,
        url: str
    ):
        params = {
            "url": url,
        }

        return self._send_command(
            "Browser.addPrivacySandboxEnrollmentOverride",
            params
        )

