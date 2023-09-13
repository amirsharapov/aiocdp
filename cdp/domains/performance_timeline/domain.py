from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.network.types import (
    TimeSinceEpoch
)
from cdp.domains.dom.types import (
    Rect,
    BackendNodeId
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.performance_timeline.types import (
    LargestContentfulPaint,
    LayoutShift,
    TimelineEvent
)


@dataclass
class PerformanceTimeline(BaseDomain):
    def enable(
        self,
        event_types: list
    ):
        params = {
            "eventTypes": event_types,
        }

        return self._send_command(
            "PerformanceTimeline.enable",
            params
        )

