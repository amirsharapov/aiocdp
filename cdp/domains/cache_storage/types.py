from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

CachedResponseType = Literal[
    "basic",
    "cors",
    "default",
    "error",
    "opaqueResponse",
    "opaqueRedirect"
]


@dataclass
class Cache:
    cacheId: CacheId
    securityOrigin: str
    storageKey: str
    storageBucket: StorageBucket
    cacheName: str


@dataclass
class CachedResponse:
    body: str


@dataclass
class DataEntry:
    requestURL: str
    requestMethod: str
    requestHeaders: list
    responseTime: float
    responseStatus: int
    responseStatusText: str
    responseType: CachedResponseType
    responseHeaders: list


@dataclass
class Header:
    name: str
    value: str
