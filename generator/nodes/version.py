from dataclasses import dataclass

from generator.nodes.base import Node


@dataclass
class Version(Node):
    major: int
    minor: int

    @classmethod
    def from_dict(cls, data):
        return cls(
            major=data['major'],
            minor=data['minor']
        )
