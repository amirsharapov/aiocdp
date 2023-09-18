# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from typing import (
    Any,
    Literal,
    TYPE_CHECKING
)
from dataclasses import (
    dataclass
)

CacheId = str
CachedResponseType = Literal[
    'basic',
    'cors',
    'default',
    'error',
    'opaqueResponse',
    'opaqueRedirect'
]

@dataclass
class DataEntry:
    request_url: str
    request_method: str
    request_headers: list['Header']
    response_time: float
    response_status: int
    response_status_text: str
    response_type: 'CachedResponseType'
    response_headers: list['Header']


@dataclass
class Cache:
    cache_id: 'CacheId'
    security_origin: str
    storage_key: str
    storage_bucket: 'StorageBucket'
    cache_name: str


@dataclass
class Header:
    name: str
    value: str


@dataclass
class CachedResponse:
    body: str


@dataclass
class RequestCacheNamesReturnType:
    caches: list


@dataclass
class RequestCachedResponseReturnType:
    response: 'CachedResponse'


@dataclass
class RequestEntriesReturnType:
    cache_data_entries: list
    return_count: float
