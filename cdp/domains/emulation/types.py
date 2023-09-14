from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

VirtualTimePolicy = Literal[
    "advance",
    "pause",
    "pauseIfNetworkFetchesPending"
]

DisabledImageType = Literal[
    "avif",
    "webp"
]


@dataclass
class ScreenOrientation:
    type: str
    angle: int


@dataclass
class DisplayFeature:
    orientation: str
    offset: int
    mask_length: int


@dataclass
class MediaFeature:
    name: str
    value: str


@dataclass
class UserAgentBrandVersion:
    brand: str
    version: str


@dataclass
class UserAgentMetadata:
    brands: list
    full_version_list: list
    full_version: str
    platform: str
    platform_version: str
    architecture: str
    model: str
    mobile: bool
    bitness: str
    wow64: bool
