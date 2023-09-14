from dataclasses import (
    dataclass
)

PlayerId = str

Timestamp = float


@dataclass
class PlayerMessage:
    level: str
    message: str


@dataclass
class PlayerProperty:
    name: str
    value: str


@dataclass
class PlayerEvent:
    timestamp: "Timestamp"
    value: str


@dataclass
class PlayerErrorSourceLocation:
    file: str
    line: int


@dataclass
class PlayerError:
    error_type: str
    code: int
    stack: list
    cause: list
    data: object
