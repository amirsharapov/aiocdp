from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.domains.service_worker.types import (
    RegistrationID
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)


@dataclass
class ServiceWorker(BaseDomain):
    def deliver_push_message(
        self,
        origin: str,
        registration_id: RegistrationID,
        data: str
    ):
        params = {
            "origin": origin,
            "registrationId": registration_id,
            "data": data,
        }

        return self._send_command(
            "ServiceWorker.deliverPushMessage",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "ServiceWorker.disable",
            params
        )

    def dispatch_sync_event(
        self,
        origin: str,
        registration_id: RegistrationID,
        tag: str,
        last_chance: bool
    ):
        params = {
            "origin": origin,
            "registrationId": registration_id,
            "tag": tag,
            "lastChance": last_chance,
        }

        return self._send_command(
            "ServiceWorker.dispatchSyncEvent",
            params
        )

    def dispatch_periodic_sync_event(
        self,
        origin: str,
        registration_id: RegistrationID,
        tag: str
    ):
        params = {
            "origin": origin,
            "registrationId": registration_id,
            "tag": tag,
        }

        return self._send_command(
            "ServiceWorker.dispatchPeriodicSyncEvent",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "ServiceWorker.enable",
            params
        )

    def inspect_worker(
        self,
        version_id: str
    ):
        params = {
            "versionId": version_id,
        }

        return self._send_command(
            "ServiceWorker.inspectWorker",
            params
        )

    def set_force_update_on_page_load(
        self,
        force_update_on_page_load: bool
    ):
        params = {
            "forceUpdateOnPageLoad": force_update_on_page_load,
        }

        return self._send_command(
            "ServiceWorker.setForceUpdateOnPageLoad",
            params
        )

    def skip_waiting(
        self,
        scope_url: str
    ):
        params = {
            "scopeURL": scope_url,
        }

        return self._send_command(
            "ServiceWorker.skipWaiting",
            params
        )

    def start_worker(
        self,
        scope_url: str
    ):
        params = {
            "scopeURL": scope_url,
        }

        return self._send_command(
            "ServiceWorker.startWorker",
            params
        )

    def stop_all_workers(
        self
    ):
        params = {}

        return self._send_command(
            "ServiceWorker.stopAllWorkers",
            params
        )

    def stop_worker(
        self,
        version_id: str
    ):
        params = {
            "versionId": version_id,
        }

        return self._send_command(
            "ServiceWorker.stopWorker",
            params
        )

    def unregister(
        self,
        scope_url: str
    ):
        params = {
            "scopeURL": scope_url,
        }

        return self._send_command(
            "ServiceWorker.unregister",
            params
        )

    def update_registration(
        self,
        scope_url: str
    ):
        params = {
            "scopeURL": scope_url,
        }

        return self._send_command(
            "ServiceWorker.updateRegistration",
            params
        )

