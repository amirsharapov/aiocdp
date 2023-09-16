# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

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
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResult
    )


@dataclass
class DeviceOrientation(BaseDomain):
    def clear_device_orientation_override(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'DeviceOrientation.clearDeviceOrientationOverride',
            params,
            False
        )

    def set_device_orientation_override(
            self,
            alpha: float,
            beta: float,
            gamma: float
    ) -> IResult[None]:
        params = {
            'alpha': alpha,
            'beta': beta,
            'gamma': gamma,
        }

        return self._send_command(
            'DeviceOrientation.setDeviceOrientationOverride',
            params,
            False
        )
