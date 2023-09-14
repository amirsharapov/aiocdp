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
    RGBA
)
from cdp.domains.emulation.types import (
    ScreenOrientation,
    VirtualTimePolicy,
    UserAgentMetadata,
    DisplayFeature
)
from cdp.domains.page.types import (
    Viewport
)
from cdp.domains.network.types import (
    TimeSinceEpoch
)


@dataclass
class Emulation(BaseDomain):
    def can_emulate(
        self
    ):
        params = {}

        return self._send_command(
            "Emulation.canEmulate",
            params
        )

    def clear_device_metrics_override(
        self
    ):
        params = {}

        return self._send_command(
            "Emulation.clearDeviceMetricsOverride",
            params
        )

    def clear_geolocation_override(
        self
    ):
        params = {}

        return self._send_command(
            "Emulation.clearGeolocationOverride",
            params
        )

    def reset_page_scale_factor(
        self
    ):
        params = {}

        return self._send_command(
            "Emulation.resetPageScaleFactor",
            params
        )

    def set_focus_emulation_enabled(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Emulation.setFocusEmulationEnabled",
            params
        )

    def set_auto_dark_mode_override(
        self,
        enabled: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            enabled
        ):
            params[] = enabled

        return self._send_command(
            "Emulation.setAutoDarkModeOverride",
            params
        )

    def set_cpu_throttling_rate(
        self,
        rate: float
    ):
        params = {
            "rate": rate,
        }

        return self._send_command(
            "Emulation.setCPUThrottlingRate",
            params
        )

    def set_default_background_color_override(
        self,
        color: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            color
        ):
            params[] = color

        return self._send_command(
            "Emulation.setDefaultBackgroundColorOverride",
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
        viewport: MaybeUndefined[],
        display_feature: MaybeUndefined[]
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

        if is_defined(
            display_feature
        ):
            params[] = display_feature

        return self._send_command(
            "Emulation.setDeviceMetricsOverride",
            params
        )

    def set_scrollbars_hidden(
        self,
        hidden: bool
    ):
        params = {
            "hidden": hidden,
        }

        return self._send_command(
            "Emulation.setScrollbarsHidden",
            params
        )

    def set_document_cookie_disabled(
        self,
        disabled: bool
    ):
        params = {
            "disabled": disabled,
        }

        return self._send_command(
            "Emulation.setDocumentCookieDisabled",
            params
        )

    def set_emit_touch_events_for_mouse(
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
            "Emulation.setEmitTouchEventsForMouse",
            params
        )

    def set_emulated_media(
        self,
        media: MaybeUndefined[],
        features: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            media
        ):
            params[] = media

        if is_defined(
            features
        ):
            params[] = features

        return self._send_command(
            "Emulation.setEmulatedMedia",
            params
        )

    def set_emulated_vision_deficiency(
        self,
        type_: str
    ):
        params = {
            "type": type_,
        }

        return self._send_command(
            "Emulation.setEmulatedVisionDeficiency",
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
            "Emulation.setGeolocationOverride",
            params
        )

    def set_idle_override(
        self,
        is_user_active: bool,
        is_screen_unlocked: bool
    ):
        params = {
            "isUserActive": is_user_active,
            "isScreenUnlocked": is_screen_unlocked,
        }

        return self._send_command(
            "Emulation.setIdleOverride",
            params
        )

    def clear_idle_override(
        self
    ):
        params = {}

        return self._send_command(
            "Emulation.clearIdleOverride",
            params
        )

    def set_navigator_overrides(
        self,
        platform: str
    ):
        params = {
            "platform": platform,
        }

        return self._send_command(
            "Emulation.setNavigatorOverrides",
            params
        )

    def set_page_scale_factor(
        self,
        page_scale_factor: float
    ):
        params = {
            "pageScaleFactor": page_scale_factor,
        }

        return self._send_command(
            "Emulation.setPageScaleFactor",
            params
        )

    def set_script_execution_disabled(
        self,
        value: bool
    ):
        params = {
            "value": value,
        }

        return self._send_command(
            "Emulation.setScriptExecutionDisabled",
            params
        )

    def set_touch_emulation_enabled(
        self,
        enabled: bool,
        max_touch_points: MaybeUndefined[]
    ):
        params = {
            "enabled": enabled,
        }

        if is_defined(
            max_touch_points
        ):
            params[] = max_touch_points

        return self._send_command(
            "Emulation.setTouchEmulationEnabled",
            params
        )

    def set_virtual_time_policy(
        self,
        policy: VirtualTimePolicy,
        budget: MaybeUndefined[],
        max_virtual_time_task_starvation_count: MaybeUndefined[],
        initial_virtual_time: MaybeUndefined[]
    ):
        params = {
            "policy": policy,
        }

        if is_defined(
            budget
        ):
            params[] = budget

        if is_defined(
            max_virtual_time_task_starvation_count
        ):
            params[] = max_virtual_time_task_starvation_count

        if is_defined(
            initial_virtual_time
        ):
            params[] = initial_virtual_time

        return self._send_command(
            "Emulation.setVirtualTimePolicy",
            params
        )

    def set_locale_override(
        self,
        locale: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            locale
        ):
            params[] = locale

        return self._send_command(
            "Emulation.setLocaleOverride",
            params
        )

    def set_timezone_override(
        self,
        timezone_id: str
    ):
        params = {
            "timezoneId": timezone_id,
        }

        return self._send_command(
            "Emulation.setTimezoneOverride",
            params
        )

    def set_visible_size(
        self,
        width: int,
        height: int
    ):
        params = {
            "width": width,
            "height": height,
        }

        return self._send_command(
            "Emulation.setVisibleSize",
            params
        )

    def set_disabled_image_types(
        self,
        image_types: list
    ):
        params = {
            "imageTypes": image_types,
        }

        return self._send_command(
            "Emulation.setDisabledImageTypes",
            params
        )

    def set_hardware_concurrency_override(
        self,
        hardware_concurrency: int
    ):
        params = {
            "hardwareConcurrency": hardware_concurrency,
        }

        return self._send_command(
            "Emulation.setHardwareConcurrencyOverride",
            params
        )

    def set_user_agent_override(
        self,
        user_agent: str,
        accept_language: MaybeUndefined[],
        platform: MaybeUndefined[],
        user_agent_metadata: MaybeUndefined[]
    ):
        params = {
            "userAgent": user_agent,
        }

        if is_defined(
            accept_language
        ):
            params[] = accept_language

        if is_defined(
            platform
        ):
            params[] = platform

        if is_defined(
            user_agent_metadata
        ):
            params[] = user_agent_metadata

        return self._send_command(
            "Emulation.setUserAgentOverride",
            params
        )

    def set_automation_override(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Emulation.setAutomationOverride",
            params
        )

