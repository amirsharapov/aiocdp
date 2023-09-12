from dataclasses import dataclass

from generator.nodes.base import Node
from generator.nodes.domain import Domain
from generator.nodes.version import Version
from generator.utils import MaybeUndefined, UNDEFINED


@dataclass
class Protocol(Node):
    version: 'Version'
    domains: list['Domain']

    @classmethod
    def from_dict(cls, data):
        return cls(
            version=Version.from_dict(data['version']),
            domains=[Domain.from_dict(domain) for domain in data['domains']]
        )
