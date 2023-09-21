# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.types import (
    dom,
    runtime
)
from typing import (
    TypedDict
)


class Animation(TypedDict):
    id: str
    name: str
    paused_state: bool
    play_state: str
    playback_rate: float
    start_time: float
    current_time: float
    type: str
    source: 'AnimationEffect'
    css_id: str


class AnimationEffect(TypedDict):
    delay: float
    end_delay: float
    iteration_start: float
    iterations: float
    duration: float
    direction: str
    fill: str
    easing: str
    backend_node_id: 'dom.BackendNodeId'
    keyframes_rule: 'KeyframesRule'


class KeyframesRule(TypedDict):
    keyframes: list
    name: str


class KeyframeStyle(TypedDict):
    offset: str
    easing: str