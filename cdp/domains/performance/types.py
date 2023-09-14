from dataclasses import (
    dataclass
)


@dataclass
class Metric:
    name: str
    value: float


@dataclass
class GetMetricsReturnT:
    metrics: list
