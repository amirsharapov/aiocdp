from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.domains.device_access.types import (
    DeviceId,
    RequestId
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)


@dataclass
class DeviceAccess(BaseDomain):
    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "DeviceAccess.enable",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "DeviceAccess.disable",
            params
        )

    def select_prompt(
        self,
        id_: RequestId,
        device_id: DeviceId
    ):
        params = {
            "id": id_,
            "deviceId": device_id,
        }

        return self._send_command(
            "DeviceAccess.selectPrompt",
            params
        )

    def cancel_prompt(
        self,
        id_: RequestId
    ):
        params = {
            "id": id_,
        }

        return self._send_command(
            "DeviceAccess.cancelPrompt",
            params
        )

