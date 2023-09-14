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
    TraceConfig,
    TracingBackend,
    StreamCompression,
    StreamFormat,
    MemoryDumpLevelOfDetail
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
        deterministic: bool = UNDEFINED,
        level_of_detail: MemoryDumpLevelOfDetail = UNDEFINED
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
        categories: str = UNDEFINED,
        options: str = UNDEFINED,
        buffer_usage_reporting_interval: float = UNDEFINED,
        transfer_mode: str = UNDEFINED,
        stream_format: StreamFormat = UNDEFINED,
        stream_compression: StreamCompression = UNDEFINED,
        trace_config: TraceConfig = UNDEFINED,
        perfetto_config: str = UNDEFINED,
        tracing_backend: TracingBackend = UNDEFINED
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

