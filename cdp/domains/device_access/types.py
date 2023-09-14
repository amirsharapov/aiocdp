from dataclasses import (
    dataclass
)

RequestId = str

DeviceId = str


@dataclass
class PromptDevice:
    id: "DeviceId"
    name: str
