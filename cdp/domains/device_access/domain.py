# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.domains.base import (
    BaseDomain
)
from cdp.domains import (
    mappers
)
from cdp.utils import (
    UNDEFINED,
    is_defined
)
from dataclasses import (
    dataclass
)
from typing import (
    TYPE_CHECKING
)
from cdp.domains.device_access.types import (
    DeviceId,
    RequestId
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IFutureResponse
    )


@dataclass
class DeviceAccess(BaseDomain):
    def enable(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'DeviceAccess.enable',
            params,
            False
        )

    def disable(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'DeviceAccess.disable',
            params,
            False
        )

    def select_prompt(
            self,
            id_: 'RequestId',
            device_id: 'DeviceId'
    ) -> 'IFutureResponse[None]':
        params = {
            'id': to_dict(
                id_,
                'camel'
            ),
            'deviceId': to_dict(
                device_id,
                'camel'
            ),
        }

        return self._send_command(
            'DeviceAccess.selectPrompt',
            params,
            False
        )

    def cancel_prompt(
            self,
            id_: 'RequestId'
    ) -> 'IFutureResponse[None]':
        params = {
            'id': to_dict(
                id_,
                'camel'
            ),
        }

        return self._send_command(
            'DeviceAccess.cancelPrompt',
            params,
            False
        )
