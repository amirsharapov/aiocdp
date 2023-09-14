from dataclasses import (
    dataclass
)
from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.heap_profiler.types import (
    SamplingHeapProfile,
    HeapSnapshotObjectId
)
from cdp.domains.runtime.types import (
    RemoteObject,
    RemoteObjectId
)


@dataclass
class HeapProfiler(BaseDomain):
    def add_inspected_heap_object(
        self,
        heap_object_id: HeapSnapshotObjectId
    ):
        params = {
            "heapObjectId": heap_object_id,
        }

        return self._send_command(
            "HeapProfiler.addInspectedHeapObject",
            params
        )

    def collect_garbage(
        self
    ):
        params = {}

        return self._send_command(
            "HeapProfiler.collectGarbage",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "HeapProfiler.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "HeapProfiler.enable",
            params
        )

    def get_heap_object_id(
        self,
        object_id: RemoteObjectId
    ):
        params = {
            "objectId": object_id,
        }

        return self._send_command(
            "HeapProfiler.getHeapObjectId",
            params
        )

    def get_object_by_heap_object_id(
        self,
        object_id: HeapSnapshotObjectId,
        object_group: str = UNDEFINED
    ):
        params = {
            "objectId": object_id,
        }

        if is_defined(
            object_group
        ):
            params["objectGroup"] = object_group

        return self._send_command(
            "HeapProfiler.getObjectByHeapObjectId",
            params
        )

    def get_sampling_profile(
        self
    ):
        params = {}

        return self._send_command(
            "HeapProfiler.getSamplingProfile",
            params
        )

    def start_sampling(
        self,
        sampling_interval: float = UNDEFINED
    ):
        params = {}

        if is_defined(
            sampling_interval
        ):
            params["samplingInterval"] = sampling_interval

        return self._send_command(
            "HeapProfiler.startSampling",
            params
        )

    def start_tracking_heap_objects(
        self,
        track_allocations: bool = UNDEFINED
    ):
        params = {}

        if is_defined(
            track_allocations
        ):
            params["trackAllocations"] = track_allocations

        return self._send_command(
            "HeapProfiler.startTrackingHeapObjects",
            params
        )

    def stop_sampling(
        self
    ):
        params = {}

        return self._send_command(
            "HeapProfiler.stopSampling",
            params
        )

    def stop_tracking_heap_objects(
        self,
        report_progress: bool = UNDEFINED
    ):
        params = {}

        if is_defined(
            report_progress
        ):
            params["reportProgress"] = report_progress

        return self._send_command(
            "HeapProfiler.stopTrackingHeapObjects",
            params
        )

    def take_heap_snapshot(
        self,
        report_progress: bool = UNDEFINED
    ):
        params = {}

        if is_defined(
            report_progress
        ):
            params["reportProgress"] = report_progress

        return self._send_command(
            "HeapProfiler.takeHeapSnapshot",
            params
        )

