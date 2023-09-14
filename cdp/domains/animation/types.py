from dataclasses import (
    dataclass
)
from cdp.domains.dom.types import (
    BackendNodeId
)
from cdp.domains.runtime.types import (
    RemoteObject
)


@dataclass
class Animation:
    id: str
    name: str
    paused_state: bool
    play_state: str
    playback_rate: float
    start_time: float
    current_time: float
    type: str
    source: "AnimationEffect"
    css_id: str


@dataclass
class AnimationEffect:
    delay: float
    end_delay: float
    iteration_start: float
    iterations: float
    duration: float
    direction: str
    fill: str
    backend_node_id: "BackendNodeId"
    keyframes_rule: "KeyframesRule"
    easing: str


@dataclass
class KeyframesRule:
    name: str
    keyframes: list


@dataclass
class KeyframeStyle:
    offset: str
    easing: str


@dataclass
class GetCurrentTimeReturnT:
    current_time: float


@dataclass
class GetPlaybackRateReturnT:
    playback_rate: float


@dataclass
class ResolveAnimationReturnT:
    remote_object: "RemoteObject"
