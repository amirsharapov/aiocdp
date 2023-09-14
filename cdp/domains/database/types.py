from dataclasses import (
    dataclass
)

DatabaseId = str


@dataclass
class Database:
    id: "DatabaseId"
    domain: str
    name: str
    version: str


@dataclass
class Error:
    message: str
    code: int
