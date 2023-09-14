from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

RequestStage = Literal[
    "Request",
    "Response"
]


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
class HeaderEntry:
    name: str
    value: str


@dataclass
class RequestPattern:
    urlPattern: str
    resourceType: ResourceType
    requestStage: RequestStage
