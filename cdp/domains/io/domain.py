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
from cdp.domains.io.types import (
    StreamHandle
)
from cdp.domains.runtime.types import (
    RemoteObjectId
)


@dataclass
class IO(BaseDomain):
    def close(
        self,
        handle: StreamHandle
    ):
        params = {
            "handle": handle,
        }

        return self._send_command(
            "IO.close",
            params
        )

    def read(
        self,
        handle: StreamHandle,
        offset: MaybeUndefined[],
        size: MaybeUndefined[]
    ):
        params = {
            "handle": handle,
        }

        if is_defined(
            offset
        ):
            params[] = offset

        if is_defined(
            size
        ):
            params[] = size

        return self._send_command(
            "IO.read",
            params
        )

    def resolve_blob(
        self,
        object_id: RemoteObjectId
    ):
        params = {
            "objectId": object_id,
        }

        return self._send_command(
            "IO.resolveBlob",
            params
        )

