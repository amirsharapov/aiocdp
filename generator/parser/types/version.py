from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser.types.base import ComplexNode

if TYPE_CHECKING:
    from generator.parser.types.protocol import Protocol


@dataclass
class Version(ComplexNode):
    parent: 'Protocol' = field(
        init=False,
        repr=False
    )

    major: int
    minor: int

    @classmethod
    def from_dict(cls, data):
        return cls(
            major=data['major'],
            minor=data['minor']
        )
