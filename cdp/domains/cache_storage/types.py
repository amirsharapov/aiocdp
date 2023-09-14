from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.storage.types import (
    StorageBucket
)

CacheId = str

CachedResponseType = Literal[
    "basic",
    "cors",
    "default",
    "error",
    "opaqueResponse",
    "opaqueRedirect"
]


@dataclass
class DataEntry:
    request_url: str
    request_method: str
    request_headers: list
    response_time: float
    response_status: int
    response_status_text: str
    response_type: "CachedResponseType"
    response_headers: list


@dataclass
class Cache:
    cache_id: "CacheId"
    security_origin: str
    storage_key: str
    storage_bucket: "StorageBucket"
    cache_name: str


@dataclass
class Header:
    name: str
    value: str


@dataclass
class CachedResponse:
    body: str


@dataclass
class RequestCacheNamesReturnT:
    caches: list


@dataclass
class RequestCachedResponseReturnT:
    response: "CachedResponse"


@dataclass
class RequestEntriesReturnT:
    cache_data_entries: list
    return_count: float
