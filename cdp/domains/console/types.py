from dataclasses import (
    dataclass
)


@dataclass
class ConsoleMessage:
    source: str
    level: str
    text: str
    url: str
    line: int
    column: int
