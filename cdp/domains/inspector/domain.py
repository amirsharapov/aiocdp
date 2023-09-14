from cdp.utils import (
    is_defined,
    MaybeUndefined,
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

