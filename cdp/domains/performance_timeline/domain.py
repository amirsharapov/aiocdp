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


@dataclass
class PerformanceTimeline(BaseDomain):
    def enable(
        self,
        event_types: list
    ):
        params = {
            "eventTypes": event_types,
        }

        return self._send_command(
            "PerformanceTimeline.enable",
            params
        )

