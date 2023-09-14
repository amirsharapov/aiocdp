from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class ConsoleMessage:
    source: str
    level: str
    text: str
    url: str
    line: int
    column: int
