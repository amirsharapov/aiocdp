# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from cdp.generated.types import (
    dom,
    network,
    page
)
from typing import (
    Literal,
    TypedDict
)

VirtualTimePolicy = Literal[
    'advance',
    'pause',
    'pauseIfNetworkFetchesPending'
]

DisabledImageType = Literal[
    'avif',
    'webp'
]


class ScreenOrientation(TypedDict):
    type: str
    angle: int


class DisplayFeature(TypedDict):
    orientation: str
    offset: int
    mask_length: int


class MediaFeature(TypedDict):
    name: str
    value: str


class UserAgentBrandVersion(TypedDict):
    brand: str
    version: str


class UserAgentMetadata(TypedDict):
    platform: str
    platform_version: str
    architecture: str
    model: str
    mobile: bool
    brands: list
    full_version_list: list
    full_version: str
    bitness: str
    wow64: bool


class SetFocusEmulationEnabledParamsT(TypedDict):
    enabled: bool


class SetAutoDarkModeOverrideParamsT(TypedDict):
    enabled: bool


class SetCPUThrottlingRateParamsT(TypedDict):
    rate: float


class SetDefaultBackgroundColorOverrideParamsT(TypedDict):
    color: 'dom.RGBA'


class SetDeviceMetricsOverrideParamsT(TypedDict):
    width: int
    height: int
    device_scale_factor: float
    mobile: bool
    scale: float
    screen_width: int
    screen_height: int
    position_x: int
    position_y: int
    dont_set_visible_size: bool
    screen_orientation: 'ScreenOrientation'
    viewport: 'page.Viewport'
    display_feature: 'DisplayFeature'


class SetScrollbarsHiddenParamsT(TypedDict):
    hidden: bool


class SetDocumentCookieDisabledParamsT(TypedDict):
    disabled: bool


class SetEmitTouchEventsForMouseParamsT(TypedDict):
    enabled: bool
    configuration: str


class SetEmulatedMediaParamsT(TypedDict):
    media: str
    features: list


class SetEmulatedVisionDeficiencyParamsT(TypedDict):
    type: str


class SetGeolocationOverrideParamsT(TypedDict):
    latitude: float
    longitude: float
    accuracy: float


class SetIdleOverrideParamsT(TypedDict):
    is_user_active: bool
    is_screen_unlocked: bool


class SetNavigatorOverridesParamsT(TypedDict):
    platform: str


class SetPageScaleFactorParamsT(TypedDict):
    page_scale_factor: float


class SetScriptExecutionDisabledParamsT(TypedDict):
    value: bool


class SetTouchEmulationEnabledParamsT(TypedDict):
    enabled: bool
    max_touch_points: int


class SetVirtualTimePolicyParamsT(TypedDict):
    policy: 'VirtualTimePolicy'
    budget: float
    max_virtual_time_task_starvation_count: int
    initial_virtual_time: 'network.TimeSinceEpoch'


class SetLocaleOverrideParamsT(TypedDict):
    locale: str


class SetTimezoneOverrideParamsT(TypedDict):
    timezone_id: str


class SetVisibleSizeParamsT(TypedDict):
    width: int
    height: int


class SetDisabledImageTypesParamsT(TypedDict):
    image_types: list


class SetHardwareConcurrencyOverrideParamsT(TypedDict):
    hardware_concurrency: int


class SetUserAgentOverrideParamsT(TypedDict):
    user_agent: str
    accept_language: str
    platform: str
    user_agent_metadata: 'UserAgentMetadata'


class SetAutomationOverrideParamsT(TypedDict):
    enabled: bool


class CanEmulateReturnT(TypedDict):
    result: bool


class SetVirtualTimePolicyReturnT(TypedDict):
    virtual_time_ticks_base: float


class VirtualTimeBudgetExpiredEventT(TypedDict):
    name: Literal['virtual_time_budget_expired']
    params: None
