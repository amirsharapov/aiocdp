from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.tracing.types import (
    TracingBackend,
    MemoryDumpLevelOfDetail,
    StreamFormat,
    TraceConfig,
    StreamCompression,
    MemoryDumpConfig
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
        deterministic: MaybeUndefined[bool],
        level_of_detail: MaybeUndefined[MemoryDumpLevelOfDetail]
    ):
        params = {}

        if is_defined(
            deterministic
        ):
            params["deterministic"] = deterministic

        if is_defined(
            level_of_detail
        ):
            params["levelOfDetail"] = level_of_detail

        return self._send_command(
            "Tracing.requestMemoryDump",
            params
        )

    def start(
        self,
        categories: MaybeUndefined[str],
        options: MaybeUndefined[str],
        buffer_usage_reporting_interval: MaybeUndefined[float],
        transfer_mode: MaybeUndefined[str],
        stream_format: MaybeUndefined[StreamFormat],
        stream_compression: MaybeUndefined[StreamCompression],
        trace_config: MaybeUndefined[TraceConfig],
        perfetto_config: MaybeUndefined[str],
        tracing_backend: MaybeUndefined[TracingBackend]
    ):
        params = {}

        if is_defined(
            categories
        ):
            params["categories"] = categories

        if is_defined(
            options
        ):
            params["options"] = options

        if is_defined(
            buffer_usage_reporting_interval
        ):
            params["bufferUsageReportingInterval"] = buffer_usage_reporting_interval

        if is_defined(
            transfer_mode
        ):
            params["transferMode"] = transfer_mode

        if is_defined(
            stream_format
        ):
            params["streamFormat"] = stream_format

        if is_defined(
            stream_compression
        ):
            params["streamCompression"] = stream_compression

        if is_defined(
            trace_config
        ):
            params["traceConfig"] = trace_config

        if is_defined(
            perfetto_config
        ):
            params["perfettoConfig"] = perfetto_config

        if is_defined(
            tracing_backend
        ):
            params["tracingBackend"] = tracing_backend

        return self._send_command(
            "Tracing.start",
            params
        )

