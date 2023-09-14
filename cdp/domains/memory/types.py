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
class Module:
    name: str
    uuid: str
    baseAddress: str
    size: float


@dataclass
class SamplingProfile:
    samples: list
    modules: list


@dataclass
class SamplingProfileNode:
    size: float
    total: float
    stack: list
