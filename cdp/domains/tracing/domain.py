# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)
from cdp.domains.tracing.types import (
    GetCategoriesReturnT,
    MemoryDumpLevelOfDetail,
    RequestMemoryDumpReturnT,
    StreamCompression,
    StreamFormat,
    TraceConfig,
    TracingBackend
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResult
    )


@dataclass
class Tracing(BaseDomain):
    def end(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Tracing.end',
            params,
            False
        )

    def get_categories(
            self
    ) -> IResult['GetCategoriesReturnT']:
        params = {}

        return self._send_command(
            'Tracing.getCategories',
            params,
            True
        )

    def record_clock_sync_marker(
            self,
            sync_id: str
    ) -> IResult[None]:
        params = {
            'syncId': sync_id,
        }

        return self._send_command(
            'Tracing.recordClockSyncMarker',
            params,
            False
        )

    def request_memory_dump(
            self,
            deterministic: bool = UNDEFINED,
            level_of_detail: MemoryDumpLevelOfDetail = UNDEFINED
    ) -> IResult['RequestMemoryDumpReturnT']:
        params = {}

        if is_defined(deterministic):
            params['deterministic'] = deterministic

        if is_defined(level_of_detail):
            params['levelOfDetail'] = level_of_detail

        return self._send_command(
            'Tracing.requestMemoryDump',
            params,
            True
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
    ) -> IResult[None]:
        params = {}

        if is_defined(categories):
            params['categories'] = categories

        if is_defined(options):
            params['options'] = options

        if is_defined(buffer_usage_reporting_interval):
            params['bufferUsageReportingInterval'] = buffer_usage_reporting_interval

        if is_defined(transfer_mode):
            params['transferMode'] = transfer_mode

        if is_defined(stream_format):
            params['streamFormat'] = stream_format

        if is_defined(stream_compression):
            params['streamCompression'] = stream_compression

        if is_defined(trace_config):
            params['traceConfig'] = trace_config

        if is_defined(perfetto_config):
            params['perfettoConfig'] = perfetto_config

        if is_defined(tracing_backend):
            params['tracingBackend'] = tracing_backend

        return self._send_command(
            'Tracing.start',
            params,
            False
        )
