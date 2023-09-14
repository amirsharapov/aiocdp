from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class Metric:
    name: str
    value: float
