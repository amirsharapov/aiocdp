# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from cdp.generated.types import (
    storage
)
from typing import (
    Literal,
    NotRequired,
    TypedDict
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


class DataEntry(TypedDict):
    request_url: str
    request_method: str
    request_headers: list
    response_time: float
    response_status: int
    response_status_text: str
    response_type: 'CachedResponseType'
    response_headers: list


class Cache(TypedDict):
    cache_id: 'CacheId'
    security_origin: str
    storage_key: str
    cache_name: str
    storage_bucket: NotRequired['storage.StorageBucket']


class Header(TypedDict):
    name: str
    value: str


class CachedResponse(TypedDict):
    body: str


class DeleteCacheParamsT(TypedDict):
    cache_id: 'CacheId'


class DeleteEntryParamsT(TypedDict):
    cache_id: 'CacheId'
    request: str


class RequestCacheNamesParamsT(TypedDict):
    security_origin: NotRequired[str]
    storage_key: NotRequired[str]
    storage_bucket: NotRequired['storage.StorageBucket']


class RequestCachedResponseParamsT(TypedDict):
    cache_id: 'CacheId'
    request_url: str
    request_headers: list


class RequestEntriesParamsT(TypedDict):
    cache_id: 'CacheId'
    skip_count: NotRequired[int]
    page_size: NotRequired[int]
    path_filter: NotRequired[str]


class RequestCacheNamesReturnT(TypedDict):
    caches: list


class RequestCachedResponseReturnT(TypedDict):
    response: 'CachedResponse'


class RequestEntriesReturnT(TypedDict):
    cache_data_entries: list
    return_count: float