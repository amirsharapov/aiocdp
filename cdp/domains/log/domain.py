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

