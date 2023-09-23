# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from cdp.generated.types import (
    network,
    runtime
)
from typing import (
    Literal,
    TypedDict
)


class LogEntry(TypedDict):
    source: str
    level: str
    text: str
    timestamp: 'runtime.Timestamp'
    category: str
    url: str
    line_number: int
    stack_trace: 'runtime.StackTrace'
    network_request_id: 'network.RequestId'
    worker_id: str
    args: list


class ViolationSetting(TypedDict):
    name: str
    threshold: float


class StartViolationsReportParamsT(TypedDict):
    config: list


class EntryAddedEventT(TypedDict):
    name: Literal['entry_added']
    params: 'EntryAddedParamsT'


class EntryAddedParamsT(TypedDict):
    entry: 'LogEntry'
