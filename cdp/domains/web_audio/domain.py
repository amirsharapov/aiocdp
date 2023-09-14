from dataclasses import (
    dataclass
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)


@dataclass
class WebAudio(BaseDomain):
    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "WebAudio.enable",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "WebAudio.disable",
            params
        )

    def get_realtime_data(
        self,
        context_id: GraphObjectId
    ):
        params = {
            ""contextId"": context_id,
        }

        return self._send_command(
            "WebAudio.getRealtimeData",
            params
        )

