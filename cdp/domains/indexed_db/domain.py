from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.indexed_db.types import (
    Key,
    KeyRange,
    DatabaseWithObjectStores,
    KeyPath
)
from cdp.domains.runtime.types import (
    RemoteObject
)
from cdp.domains.storage.types import (
    StorageBucket
)


@dataclass
class IndexedDB(BaseDomain):
    def clear_object_store(
        self,
        security_origin: MaybeUndefined[str],
        storage_key: MaybeUndefined[str],
        storage_bucket: MaybeUndefined[StorageBucket],
        database_name: str,
        object_store_name: str
    ):
        params = {
            "databaseName": database_name,
            "objectStoreName": object_store_name,
        }

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
            "IndexedDB.clearObjectStore",
            params
        )

    def delete_database(
        self,
        security_origin: MaybeUndefined[str],
        storage_key: MaybeUndefined[str],
        storage_bucket: MaybeUndefined[StorageBucket],
        database_name: str
    ):
        params = {
            "databaseName": database_name,
        }

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
            "IndexedDB.deleteDatabase",
            params
        )

    def delete_object_store_entries(
        self,
        security_origin: MaybeUndefined[str],
        storage_key: MaybeUndefined[str],
        storage_bucket: MaybeUndefined[StorageBucket],
        database_name: str,
        object_store_name: str,
        key_range: KeyRange
    ):
        params = {
            "databaseName": database_name,
            "objectStoreName": object_store_name,
            "keyRange": key_range,
        }

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
            "IndexedDB.deleteObjectStoreEntries",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "IndexedDB.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "IndexedDB.enable",
            params
        )

    def request_data(
        self,
        security_origin: MaybeUndefined[str],
        storage_key: MaybeUndefined[str],
        storage_bucket: MaybeUndefined[StorageBucket],
        database_name: str,
        object_store_name: str,
        index_name: str,
        skip_count: int,
        page_size: int,
        key_range: MaybeUndefined[KeyRange]
    ):
        params = {
            "databaseName": database_name,
            "objectStoreName": object_store_name,
            "indexName": index_name,
            "skipCount": skip_count,
            "pageSize": page_size,
        }

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

        if is_defined(
            key_range
        ):
            params["keyRange"] = key_range

        return self._send_command(
            "IndexedDB.requestData",
            params
        )

    def get_metadata(
        self,
        security_origin: MaybeUndefined[str],
        storage_key: MaybeUndefined[str],
        storage_bucket: MaybeUndefined[StorageBucket],
        database_name: str,
        object_store_name: str
    ):
        params = {
            "databaseName": database_name,
            "objectStoreName": object_store_name,
        }

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
            "IndexedDB.getMetadata",
            params
        )

    def request_database(
        self,
        security_origin: MaybeUndefined[str],
        storage_key: MaybeUndefined[str],
        storage_bucket: MaybeUndefined[StorageBucket],
        database_name: str
    ):
        params = {
            "databaseName": database_name,
        }

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
            "IndexedDB.requestDatabase",
            params
        )

    def request_database_names(
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
            "IndexedDB.requestDatabaseNames",
            params
        )

