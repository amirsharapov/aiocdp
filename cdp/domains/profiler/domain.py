from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.domains.profiler.types import (
    Profile
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)


@dataclass
class Profiler(BaseDomain):
    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Profiler.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Profiler.enable",
            params
        )

    def get_best_effort_coverage(
        self
    ):
        params = {}

        return self._send_command(
            "Profiler.getBestEffortCoverage",
            params
        )

    def set_sampling_interval(
        self,
        interval: int
    ):
        params = {
            "interval": interval,
        }

        return self._send_command(
            "Profiler.setSamplingInterval",
            params
        )

    def start(
        self
    ):
        params = {}

        return self._send_command(
            "Profiler.start",
            params
        )

    def start_precise_coverage(
        self,
        call_count: bool = UNDEFINED,
        detailed: bool = UNDEFINED
    ):
        params = {}

        if is_defined(
            call_count
        ):
            params["callCount"] = call_count

        if is_defined(
            detailed
        ):
            params["detailed"] = detailed

        return self._send_command(
            "Profiler.startPreciseCoverage",
            params
        )

    def start_type_profile(
        self
    ):
        params = {}

        return self._send_command(
            "Profiler.startTypeProfile",
            params
        )

    def stop(
        self
    ):
        params = {}

        return self._send_command(
            "Profiler.stop",
            params
        )

    def stop_precise_coverage(
        self
    ):
        params = {}

        return self._send_command(
            "Profiler.stopPreciseCoverage",
            params
        )

    def stop_type_profile(
        self
    ):
        params = {}

        return self._send_command(
            "Profiler.stopTypeProfile",
            params
        )

    def take_precise_coverage(
        self
    ):
        params = {}

        return self._send_command(
            "Profiler.takePreciseCoverage",
            params
        )

    def take_type_profile(
        self
    ):
        params = {}

        return self._send_command(
            "Profiler.takeTypeProfile",
            params
        )

