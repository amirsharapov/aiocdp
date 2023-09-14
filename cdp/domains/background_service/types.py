from dataclasses import (
    dataclass
)
from typing import (
    Literal
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
class BackgroundServiceEvent:
    timestamp: TimeSinceEpoch
    origin: str
    serviceWorkerRegistrationId: RegistrationID
    service: ServiceName
    eventName: str
    instanceId: str
    eventMetadata: list
    storageKey: str


@dataclass
class EventMetadata:
    key: str
    value: str
