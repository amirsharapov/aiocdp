from dataclasses import dataclass, field

from generator.parser.types.base import Node
from generator.parser.types.domain import Domain
from generator.parser.types.version import Version


@dataclass
class Protocol(Node):
    version: 'Version' = field(
        init=False
    )
    domains: list['Domain'] = field(
        init=False
    )

    def resolve(self):
        self.version = Version(
            self.raw['version']
        )

        self.domains = [
            Domain(domain) for
            domain in
            self.raw['domains']
        ]
