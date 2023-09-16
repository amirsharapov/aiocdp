from dataclasses import dataclass

from generator.parser.types.base import ComplexNode
from generator.parser.types.domain import Domain
from generator.parser.types.version import Version


@dataclass
class Protocol(ComplexNode):
    version: 'Version'
    domains: list['Domain']

    @classmethod
    def from_dict(cls, data):
        return cls(
            version=Version.from_dict(data['version']),
            domains=[Domain.from_dict(domain) for domain in data['domains']]
        )
