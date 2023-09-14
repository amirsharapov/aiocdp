from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

PressureLevel = Literal[
    "moderate",
    "critical"
]


@dataclass
class SamplingProfileNode:
    size: float
    total: float
    stack: list


@dataclass
class SamplingProfile:
    samples: list
    modules: list


@dataclass
class Module:
    name: str
    uuid: str
    base_address: str
    size: float
