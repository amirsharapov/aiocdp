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
class Preload(BaseDomain):
    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Preload.enable",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Preload.disable",
            params
        )

