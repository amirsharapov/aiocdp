from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class Database:
    id: DatabaseId
    domain: str
    name: str
    version: str


@dataclass
class Error:
    message: str
    code: int
