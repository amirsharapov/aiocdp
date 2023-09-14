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
from cdp.domains.media.types import (
    Timestamp,
    PlayerId
)


@dataclass
class Media(BaseDomain):
    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Media.enable",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Media.disable",
            params
        )

