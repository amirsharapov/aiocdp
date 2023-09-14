from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

ServiceWorkerVersionRunningStatus = Literal[
    "stopped",
    "starting",
    "running",
    "stopping"
]

ServiceWorkerVersionStatus = Literal[
    "new",
    "installing",
    "installed",
    "activating",
    "activated",
    "redundant"
]


@dataclass
class ServiceWorkerErrorMessage:
    errorMessage: str
    registrationId: RegistrationID
    versionId: str
    sourceURL: str
    lineNumber: int
    columnNumber: int


@dataclass
class ServiceWorkerRegistration:
    registrationId: RegistrationID
    scopeURL: str
    isDeleted: bool


@dataclass
class ServiceWorkerVersion:
    versionId: str
    registrationId: RegistrationID
    scriptURL: str
    runningStatus: ServiceWorkerVersionRunningStatus
    status: ServiceWorkerVersionStatus
    scriptLastModified: float
    scriptResponseTime: float
    controlledClients: list
    targetId: TargetID
