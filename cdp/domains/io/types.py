from cdp.domains.runtime.types import (
    RemoteObjectId
)

StreamHandle = str


@dataclass
class ReadReturnT:
    base64_encoded: bool
    data: str
    eof: bool


@dataclass
class ResolveBlobReturnT:
    uuid: str
