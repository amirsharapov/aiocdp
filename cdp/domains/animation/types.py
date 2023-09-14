from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class Animation:
    id: str
    name: str
    pausedState: bool
    playState: str
    playbackRate: float
    startTime: float
    currentTime: float
    type: str
    source: AnimationEffect
    cssId: str


@dataclass
class AnimationEffect:
    delay: float
    endDelay: float
    iterationStart: float
    iterations: float
    duration: float
    direction: str
    fill: str
    backendNodeId: BackendNodeId
    keyframesRule: KeyframesRule
    easing: str


@dataclass
class KeyframeStyle:
    offset: str
    easing: str


@dataclass
class KeyframesRule:
    name: str
    keyframes: list
