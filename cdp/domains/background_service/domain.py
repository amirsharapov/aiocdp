from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.network.types import (
    TimeSinceEpoch
)
from cdp.domains.service_worker.types import (
    RegistrationID
)
from cdp.domains.background_service.types import (
    BackgroundServiceEvent,
    ServiceName
)


@dataclass
class BackgroundService(BaseDomain):
    def start_observing(
        self,
        service: ServiceName
    ):
        params = {
            "service": service,
        }

        return self._send_command(
            "BackgroundService.startObserving",
            params
        )

    def stop_observing(
        self,
        service: ServiceName
    ):
        params = {
            "service": service,
        }

        return self._send_command(
            "BackgroundService.stopObserving",
            params
        )

    def set_recording(
        self,
        should_record: bool,
        service: ServiceName
    ):
        params = {
            "shouldRecord": should_record,
            "service": service,
        }

        return self._send_command(
            "BackgroundService.setRecording",
            params
        )

    def clear_events(
        self,
        service: ServiceName
    ):
        params = {
            "service": service,
        }

        return self._send_command(
            "BackgroundService.clearEvents",
            params
        )

