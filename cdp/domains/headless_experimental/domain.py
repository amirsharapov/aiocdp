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
from cdp.domains.headless_experimental.types import (
    ScreenshotParams
)


@dataclass
class HeadlessExperimental(BaseDomain):
    def begin_frame(
        self,
        frame_time_ticks: MaybeUndefined[],
        interval: MaybeUndefined[],
        no_display_updates: MaybeUndefined[],
        screenshot: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            frame_time_ticks
        ):
            params[] = frame_time_ticks

        if is_defined(
            interval
        ):
            params[] = interval

        if is_defined(
            no_display_updates
        ):
            params[] = no_display_updates

        if is_defined(
            screenshot
        ):
            params[] = screenshot

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

