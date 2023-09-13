from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.runtime.types import (
    Timestamp,
    StackTrace
)
from cdp.domains.network.types import (
    RequestId
)
from cdp.domains.log.types import (
    LogEntry
)


@dataclass
class Log(BaseDomain):
    def clear(
        self
    ):
        params = {}

        return self._send_command(
            "Log.clear",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Log.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Log.enable",
            params
        )

    def start_violations_report(
        self,
        config: list
    ):
        params = {
            "config": config,
        }

        return self._send_command(
            "Log.startViolationsReport",
            params
        )

    def stop_violations_report(
        self
    ):
        params = {}

        return self._send_command(
            "Log.stopViolationsReport",
            params
        )

