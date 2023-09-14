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
class Schema(BaseDomain):
    def get_domains(
        self
    ):
        params = {}

        return self._send_command(
            "Schema.getDomains",
            params
        )

