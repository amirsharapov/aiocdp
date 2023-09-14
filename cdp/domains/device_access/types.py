from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class PromptDevice:
    id: DeviceId
    name: str
