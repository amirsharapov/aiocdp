from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.network.types import (
    TimeSinceEpoch
)
from cdp.domains.service_worker.types import (
    RegistrationID
)

ServiceName = Literal[
    "backgroundFetch",
    "backgroundSync",
    "pushMessaging",
    "notifications",
    "paymentHandler",
    "periodicBackgroundSync"
]


@dataclass
class EventMetadata:
    key: str
    value: str


@dataclass
class BackgroundServiceEvent:
    timestamp: "TimeSinceEpoch"
    origin: str
    service_worker_registration_id: "RegistrationID"
    service: "ServiceName"
    event_name: str
    instance_id: str
    event_metadata: list
    storage_key: str
