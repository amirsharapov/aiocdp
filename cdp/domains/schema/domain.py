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
class Schema(BaseDomain):
    def get_domains(
        self
    ):
        params = {}

        return self._send_command(
            "Schema.getDomains",
            params
        )

