from dataclasses import (
    dataclass
)


@dataclass
class ScreenshotParams:
    format: str
    quality: int
    optimize_for_speed: bool


@dataclass
class BeginFrameReturnT:
    has_damage: bool
    screenshot_data: str
