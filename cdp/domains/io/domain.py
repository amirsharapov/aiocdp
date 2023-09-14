from dataclasses import (
    dataclass
)
from cdp.domains.runtime.types import (
    RemoteObjectId
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)


@dataclass
class IO(BaseDomain):
    def close(
        self,
        handle: StreamHandle
    ):
        params = {
            ""handle"": handle,
        }

        return self._send_command(
            "IO.close",
            params
        )

    def read(
        self,
        handle: StreamHandle,
        offset: int = UNDEFINED,
        size: int = UNDEFINED
    ):
        params = {
            ""handle"": handle,
        }

        if is_defined(
            offset
        ):
            params["offset"] = offset

        if is_defined(
            size
        ):
            params["size"] = size

        return self._send_command(
            "IO.read",
            params
        )

    def resolve_blob(
        self,
        object_id: RemoteObjectId
    ):
        params = {
            ""objectId"": object_id,
        }

        return self._send_command(
            "IO.resolveBlob",
            params
        )

