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


@dataclass
class Cast(BaseDomain):
    def enable(
        self,
        presentation_url: str = UNDEFINED
    ):
        params = {}

        if is_defined(
            presentation_url
        ):
            params["presentationUrl"] = presentation_url

        return self._send_command(
            "Cast.enable",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Cast.disable",
            params
        )

    def set_sink_to_use(
        self,
        sink_name: str
    ):
        params = {
            "sinkName": sink_name,
        }

        return self._send_command(
            "Cast.setSinkToUse",
            params
        )

    def start_desktop_mirroring(
        self,
        sink_name: str
    ):
        params = {
            "sinkName": sink_name,
        }

        return self._send_command(
            "Cast.startDesktopMirroring",
            params
        )

    def start_tab_mirroring(
        self,
        sink_name: str
    ):
        params = {
            "sinkName": sink_name,
        }

        return self._send_command(
            "Cast.startTabMirroring",
            params
        )

    def stop_casting(
        self,
        sink_name: str
    ):
        params = {
            "sinkName": sink_name,
        }

        return self._send_command(
            "Cast.stopCasting",
            params
        )

