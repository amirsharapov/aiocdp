from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class LogEntry:
    source: str
    level: str
    text: str
    category: str
    timestamp: Timestamp
    url: str
    lineNumber: int
    stackTrace: StackTrace
    networkRequestId: RequestId
    workerId: str
    args: list


@dataclass
class ViolationSetting:
    name: str
    threshold: float
