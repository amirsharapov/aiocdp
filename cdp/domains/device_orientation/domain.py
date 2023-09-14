from dataclasses import (
    dataclass
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)


@dataclass
class DeviceOrientation(BaseDomain):
    def clear_device_orientation_override(
        self
    ):
        params = {}

        return self._send_command(
            "DeviceOrientation.clearDeviceOrientationOverride",
            params
        )

    def set_device_orientation_override(
        self,
        alpha: float,
        beta: float,
        gamma: float
    ):
        params = {
            ""alpha"": alpha,
            ""beta"": beta,
            ""gamma"": gamma,
        }

        return self._send_command(
            "DeviceOrientation.setDeviceOrientationOverride",
            params
        )

