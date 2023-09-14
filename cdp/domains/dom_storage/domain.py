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
from cdp.domains.dom_storage.types import (
    StorageId,
    SerializedStorageKey
)


@dataclass
class DOMStorage(BaseDomain):
    def clear(
        self,
        storage_id: StorageId
    ):
        params = {
            "storageId": storage_id,
        }

        return self._send_command(
            "DOMStorage.clear",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "DOMStorage.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "DOMStorage.enable",
            params
        )

    def get_dom_storage_items(
        self,
        storage_id: StorageId
    ):
        params = {
            "storageId": storage_id,
        }

        return self._send_command(
            "DOMStorage.getDOMStorageItems",
            params
        )

    def remove_dom_storage_item(
        self,
        storage_id: StorageId,
        key: str
    ):
        params = {
            "storageId": storage_id,
            "key": key,
        }

        return self._send_command(
            "DOMStorage.removeDOMStorageItem",
            params
        )

    def set_dom_storage_item(
        self,
        storage_id: StorageId,
        key: str,
        value: str
    ):
        params = {
            "storageId": storage_id,
            "key": key,
            "value": value,
        }

        return self._send_command(
            "DOMStorage.setDOMStorageItem",
            params
        )

