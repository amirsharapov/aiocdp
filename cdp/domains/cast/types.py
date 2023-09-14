from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class Sink:
    name: str
    id: str
    session: str
