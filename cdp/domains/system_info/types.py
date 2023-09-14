from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

ImageType = Literal[
    "jpeg",
    "webp",
    "unknown"
]

SubsamplingFormat = Literal[
    "yuv420",
    "yuv422",
    "yuv444"
]


@dataclass
class GPUDevice:
    vendorId: float
    deviceId: float
    subSysId: float
    revision: float
    vendorString: str
    deviceString: str
    driverVendor: str
    driverVersion: str


@dataclass
class GPUInfo:
    devices: list
    auxAttributes: object
    featureStatus: object
    driverBugWorkarounds: list
    videoDecoding: list
    videoEncoding: list
    imageDecoding: list


@dataclass
class ImageDecodeAcceleratorCapability:
    imageType: ImageType
    maxDimensions: Size
    minDimensions: Size
    subsamplings: list


@dataclass
class ProcessInfo:
    type: str
    id: int
    cpuTime: float


@dataclass
class Size:
    width: int
    height: int


@dataclass
class VideoDecodeAcceleratorCapability:
    profile: str
    maxResolution: Size
    minResolution: Size


@dataclass
class VideoEncodeAcceleratorCapability:
    profile: str
    maxResolution: Size
    maxFramerateNumerator: int
    maxFramerateDenominator: int
