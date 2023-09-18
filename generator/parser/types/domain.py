from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser.extensions import ExtendedString
from generator.parser.types.base import ComplexNode
from generator.parser.types.command import Command
from generator.parser.types.event import Event
from generator.parser.types.ref import Ref
from generator.parser.types.type import Type
from generator.utils import (
    snake_case,
    UNDEFINED,
    MaybeUndefined, is_builtin
)

if TYPE_CHECKING:
    from generator.parser.types import Protocol


@dataclass
class Domain(ComplexNode):
    parent: 'Protocol' = field(
        init=False,
        repr=False
    )

    domain: str
    description: MaybeUndefined[str]
    types: list['Type']
    commands: list['Command']
    events: list['Event']
    dependencies: list[str]
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @classmethod
    def from_dict(cls, data):
        return cls(
            domain=data['domain'],
            description=data.get('description', UNDEFINED),
            types=[Type.from_dict(type_) for type_ in data.get('types', [])],
            commands=[Command.from_dict(command) for command in data.get('commands', [])],
            events=[Event.from_dict(event) for event in data.get('events', [])],
            dependencies=data.get('dependencies', []),
            experimental=data.get('experimental', UNDEFINED),
            deprecated=data.get('deprecated', UNDEFINED)
        )

    @property
    def domain_(self):
        return ExtendedString(self.domain)

    @property
    def domain_snake_case(self):
        return snake_case(self.domain)

    @property
    def domain_snake_case_collision_safe(self):
        res = self.domain_snake_case

        if is_builtin(res):
            res += '_'

        return res

    def get_refs(self) -> list[Ref]:
        refs = []

        for type_ in self.types:
            refs += type_.get_refs()

        for command in self.commands:
            refs += command.get_refs()

        for event in self.events:
            refs += event.get_refs()

        return refs
