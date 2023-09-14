from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.domains.headless_experimental.types import (
    ScreenshotParams
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)


@dataclass
class HeadlessExperimental(BaseDomain):
    def begin_frame(
        self,
        frame_time_ticks: float = UNDEFINED,
        interval: float = UNDEFINED,
        no_display_updates: bool = UNDEFINED,
        screenshot: ScreenshotParams = UNDEFINED
    ):
        params = {}

        if is_defined(
            frame_time_ticks
        ):
            params["frameTimeTicks"] = frame_time_ticks

        if is_defined(
            interval
        ):
            params["interval"] = interval

        if is_defined(
            no_display_updates
        ):
            params["noDisplayUpdates"] = no_display_updates

        if is_defined(
            screenshot
        ):
            params["screenshot"] = screenshot

        return self._send_command(
            "HeadlessExperimental.beginFrame",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "HeadlessExperimental.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "HeadlessExperimental.enable",
            params
        )

