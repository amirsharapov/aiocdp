from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

DisabledImageType = Literal[
    "avif",
    "webp"
]

VirtualTimePolicy = Literal[
    "advance",
    "pause",
    "pauseIfNetworkFetchesPending"
]


@dataclass
class DisplayFeature:
    orientation: str
    offset: int
    maskLength: int


@dataclass
class MediaFeature:
    name: str
    value: str


@dataclass
class ScreenOrientation:
    type: str
    angle: int


@dataclass
class UserAgentBrandVersion:
    brand: str
    version: str


@dataclass
class UserAgentMetadata:
    brands: list
    fullVersionList: list
    fullVersion: str
    platform: str
    platformVersion: str
    architecture: str
    model: str
    mobile: bool
    bitness: str
    wow64: bool
