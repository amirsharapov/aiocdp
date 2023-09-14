from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class StorageId:
    securityOrigin: str
    storageKey: SerializedStorageKey
    isLocalStorage: bool
