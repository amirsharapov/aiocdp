from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser.types.base import Node

if TYPE_CHECKING:
    from generator.parser.types.protocol import Protocol


@dataclass
class Version(Node):
    parent: 'Protocol' = field(
        init=False,
        repr=False
    )

    major: int
    minor: int

    def resolve(self):
        self.major = self.raw['major']
        self.minor = self.raw['minor']
