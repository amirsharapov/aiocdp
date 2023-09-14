from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class PlayerError:
    errorType: str
    code: int
    stack: list
    cause: list
    data: object


@dataclass
class PlayerErrorSourceLocation:
    file: str
    line: int


@dataclass
class PlayerEvent:
    timestamp: Timestamp
    value: str


@dataclass
class PlayerMessage:
    level: str
    message: str


@dataclass
class PlayerProperty:
    name: str
    value: str
