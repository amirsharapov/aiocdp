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
class Performance(BaseDomain):
    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Performance.disable",
            params
        )

    def enable(
        self,
        time_domain: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            time_domain
        ):
            params[] = time_domain

        return self._send_command(
            "Performance.enable",
            params
        )

    def set_time_domain(
        self,
        time_domain: str
    ):
        params = {
            "timeDomain": time_domain,
        }

        return self._send_command(
            "Performance.setTimeDomain",
            params
        )

    def get_metrics(
        self
    ):
        params = {}

        return self._send_command(
            "Performance.getMetrics",
            params
        )

