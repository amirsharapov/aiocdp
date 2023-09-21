from dataclasses import dataclass, field

from cdp.utils import UNDEFINED
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

    def __post_init__(self):
        self.version = Version(
            self.raw.get(
                'version',
                UNDEFINED
            )
        )

        self.domains = [
            Domain(domain) for
            domain in
            self.raw['domains']
        ]
