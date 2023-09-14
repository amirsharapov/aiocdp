from dataclasses import (
    dataclass
)

SerializedStorageKey = str

Item = list[str]


@dataclass
class StorageId:
    security_origin: str
    storage_key: "SerializedStorageKey"
    is_local_storage: bool
