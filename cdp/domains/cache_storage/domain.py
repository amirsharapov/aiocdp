from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.cache_storage.types import (
    CacheId,
    CachedResponse,
    CachedResponseType
)
from cdp.domains.storage.types import (
    StorageBucket
)


@dataclass
class CacheStorage(BaseDomain):
    def delete_cache(
        self,
        cache_id: CacheId
    ):
        params = {
            "cacheId": cache_id,
        }

        return self._send_command(
            "CacheStorage.deleteCache",
            params
        )

    def delete_entry(
        self,
        cache_id: CacheId,
        request: str
    ):
        params = {
            "cacheId": cache_id,
            "request": request,
        }

        return self._send_command(
            "CacheStorage.deleteEntry",
            params
        )

    def request_cache_names(
        self,
        security_origin: MaybeUndefined[str],
        storage_key: MaybeUndefined[str],
        storage_bucket: MaybeUndefined[StorageBucket]
    ):
        params = {}

        if is_defined(
            security_origin
        ):
            params["securityOrigin"] = security_origin

        if is_defined(
            storage_key
        ):
            params["storageKey"] = storage_key

        if is_defined(
            storage_bucket
        ):
            params["storageBucket"] = storage_bucket

        return self._send_command(
            "CacheStorage.requestCacheNames",
            params
        )

    def request_cached_response(
        self,
        cache_id: CacheId,
        request_url: str,
        request_headers: list
    ):
        params = {
            "cacheId": cache_id,
            "requestURL": request_url,
            "requestHeaders": request_headers,
        }

        return self._send_command(
            "CacheStorage.requestCachedResponse",
            params
        )

    def request_entries(
        self,
        cache_id: CacheId,
        skip_count: MaybeUndefined[int],
        page_size: MaybeUndefined[int],
        path_filter: MaybeUndefined[str]
    ):
        params = {
            "cacheId": cache_id,
        }

        if is_defined(
            skip_count
        ):
            params["skipCount"] = skip_count

        if is_defined(
            page_size
        ):
            params["pageSize"] = page_size

        if is_defined(
            path_filter
        ):
            params["pathFilter"] = path_filter

        return self._send_command(
            "CacheStorage.requestEntries",
            params
        )

