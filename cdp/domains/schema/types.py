from dataclasses import (
    dataclass
)


@dataclass
class Domain:
    name: str
    version: str


@dataclass
class GetDomainsReturnT:
    domains: list
