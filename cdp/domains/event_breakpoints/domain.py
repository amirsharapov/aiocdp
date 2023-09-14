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
class EventBreakpoints(BaseDomain):
    def set_instrumentation_breakpoint(
        self,
        event_name: str
    ):
        params = {
            "eventName": event_name,
        }

        return self._send_command(
            "EventBreakpoints.setInstrumentationBreakpoint",
            params
        )

    def remove_instrumentation_breakpoint(
        self,
        event_name: str
    ):
        params = {
            "eventName": event_name,
        }

        return self._send_command(
            "EventBreakpoints.removeInstrumentationBreakpoint",
            params
        )

