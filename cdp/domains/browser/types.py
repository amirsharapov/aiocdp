from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

BrowserCommandId = Literal[
    "openTabSearch",
    "closeTabSearch"
]

PermissionSetting = Literal[
    "granted",
    "denied",
    "prompt"
]

PermissionType = Literal[
    "accessibilityEvents",
    "audioCapture",
    "backgroundSync",
    "backgroundFetch",
    "clipboardReadWrite",
    "clipboardSanitizedWrite",
    "displayCapture",
    "durableStorage",
    "flash",
    "geolocation",
    "idleDetection",
    "localFonts",
    "midi",
    "midiSysex",
    "nfc",
    "notifications",
    "paymentHandler",
    "periodicBackgroundSync",
    "protectedMediaIdentifier",
    "sensors",
    "storageAccess",
    "topLevelStorageAccess",
    "videoCapture",
    "videoCapturePanTiltZoom",
    "wakeLockScreen",
    "wakeLockSystem",
    "windowManagement"
]

WindowState = Literal[
    "normal",
    "minimized",
    "maximized",
    "fullscreen"
]


@dataclass
class Bounds:
    left: int
    top: int
    width: int
    height: int
    windowState: WindowState


@dataclass
class Bucket:
    low: int
    high: int
    count: int


@dataclass
class Histogram:
    name: str
    sum: int
    count: int
    buckets: list


@dataclass
class PermissionDescriptor:
    name: str
    sysex: bool
    userVisibleOnly: bool
    allowWithoutSanitization: bool
    panTiltZoom: bool
