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
from cdp.domains.system_info.types import (
    ImageType,
    Size,
    GPUInfo
)


@dataclass
class SystemInfo(BaseDomain):
    def get_info(
        self
    ):
        params = {}

        return self._send_command(
            "SystemInfo.getInfo",
            params
        )

    def get_feature_state(
        self,
        feature_state: str
    ):
        params = {
            "featureState": feature_state,
        }

        return self._send_command(
            "SystemInfo.getFeatureState",
            params
        )

    def get_process_info(
        self
    ):
        params = {}

        return self._send_command(
            "SystemInfo.getProcessInfo",
            params
        )

