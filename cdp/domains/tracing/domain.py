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
from cdp.domains.tracing.types import (
    MemoryDumpConfig,
    TraceConfig,
    StreamCompression,
    TracingBackend,
    MemoryDumpLevelOfDetail,
    StreamFormat
)
from cdp.domains.io.types import (
    StreamHandle
)


@dataclass
class Tracing(BaseDomain):
    def end(
        self
    ):
        params = {}

        return self._send_command(
            "Tracing.end",
            params
        )

    def get_categories(
        self
    ):
        params = {}

        return self._send_command(
            "Tracing.getCategories",
            params
        )

    def record_clock_sync_marker(
        self,
        sync_id: str
    ):
        params = {
            "syncId": sync_id,
        }

        return self._send_command(
            "Tracing.recordClockSyncMarker",
            params
        )

    def request_memory_dump(
        self,
        deterministic: MaybeUndefined[],
        level_of_detail: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            deterministic
        ):
            params[] = deterministic

        if is_defined(
            level_of_detail
        ):
            params[] = level_of_detail

        return self._send_command(
            "Tracing.requestMemoryDump",
            params
        )

    def start(
        self,
        categories: MaybeUndefined[],
        options: MaybeUndefined[],
        buffer_usage_reporting_interval: MaybeUndefined[],
        transfer_mode: MaybeUndefined[],
        stream_format: MaybeUndefined[],
        stream_compression: MaybeUndefined[],
        trace_config: MaybeUndefined[],
        perfetto_config: MaybeUndefined[],
        tracing_backend: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            categories
        ):
            params[] = categories

        if is_defined(
            options
        ):
            params[] = options

        if is_defined(
            buffer_usage_reporting_interval
        ):
            params[] = buffer_usage_reporting_interval

        if is_defined(
            transfer_mode
        ):
            params[] = transfer_mode

        if is_defined(
            stream_format
        ):
            params[] = stream_format

        if is_defined(
            stream_compression
        ):
            params[] = stream_compression

        if is_defined(
            trace_config
        ):
            params[] = trace_config

        if is_defined(
            perfetto_config
        ):
            params[] = perfetto_config

        if is_defined(
            tracing_backend
        ):
            params[] = tracing_backend

        return self._send_command(
            "Tracing.start",
            params
        )

