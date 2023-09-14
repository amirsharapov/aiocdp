from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.network.types import (
    ErrorReason,
    ResourceType
)
from cdp.domains.io.types import (
    StreamHandle
)

RequestId = str

RequestStage = Literal[
    "Request",
    "Response"
]


@dataclass
class RequestPattern:
    url_pattern: str
    resource_type: "ResourceType"
    request_stage: "RequestStage"


@dataclass
class HeaderEntry:
    name: str
    value: str


@dataclass
class AuthChallenge:
    source: str
    origin: str
    scheme: str
    realm: str


@dataclass
class AuthChallengeResponse:
    response: str
    username: str
    password: str


@dataclass
class GetResponseBodyReturnT:
    body: str
    base64_encoded: bool


@dataclass
class TakeResponseBodyAsStreamReturnT:
    stream: "StreamHandle"
