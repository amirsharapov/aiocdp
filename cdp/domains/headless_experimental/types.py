from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class ScreenshotParams:
    format: str
    quality: int
    optimizeForSpeed: bool
