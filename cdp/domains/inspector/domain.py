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
class Inspector(BaseDomain):
    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Inspector.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Inspector.enable",
            params
        )

