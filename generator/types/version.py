from dataclasses import dataclass

from generator.types.base import ComplexNode


@dataclass
class Version(ComplexNode):
    major: int
    minor: int

    @classmethod
    def from_dict(cls, data):
        return cls(
            major=data['major'],
            minor=data['minor']
        )
