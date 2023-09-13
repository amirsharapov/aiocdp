from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.animation.types import (
    Animation,
    AnimationEffect,
    KeyframesRule
)
from cdp.domains.dom.types import (
    BackendNodeId
)
from cdp.domains.runtime.types import (
    RemoteObject
)


@dataclass
class Animation(BaseDomain):
    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Animation.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Animation.enable",
            params
        )

    def get_current_time(
        self,
        id_: str
    ):
        params = {
            "id": id_,
        }

        return self._send_command(
            "Animation.getCurrentTime",
            params
        )

    def get_playback_rate(
        self
    ):
        params = {}

        return self._send_command(
            "Animation.getPlaybackRate",
            params
        )

    def release_animations(
        self,
        animations: list
    ):
        params = {
            "animations": animations,
        }

        return self._send_command(
            "Animation.releaseAnimations",
            params
        )

    def resolve_animation(
        self,
        animation_id: str
    ):
        params = {
            "animationId": animation_id,
        }

        return self._send_command(
            "Animation.resolveAnimation",
            params
        )

    def seek_animations(
        self,
        animations: list,
        current_time: float
    ):
        params = {
            "animations": animations,
            "currentTime": current_time,
        }

        return self._send_command(
            "Animation.seekAnimations",
            params
        )

    def set_paused(
        self,
        animations: list,
        paused: bool
    ):
        params = {
            "animations": animations,
            "paused": paused,
        }

        return self._send_command(
            "Animation.setPaused",
            params
        )

    def set_playback_rate(
        self,
        playback_rate: float
    ):
        params = {
            "playbackRate": playback_rate,
        }

        return self._send_command(
            "Animation.setPlaybackRate",
            params
        )

    def set_timing(
        self,
        animation_id: str,
        duration: float,
        delay: float
    ):
        params = {
            "animationId": animation_id,
            "duration": duration,
            "delay": delay,
        }

        return self._send_command(
            "Animation.setTiming",
            params
        )

