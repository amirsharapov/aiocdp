import logging
from dataclasses import dataclass

from generator.types.base import ComplexNode
from generator.types.command import Command
from generator.types.event import Event
from generator.types.ref import Ref
from generator.types.type import Type
from generator.utils import (
    convert_to_snake_case,
    UNDEFINED,
    MaybeUndefined
)

logger = logging.getLogger(
    'cdp.generator'
)


@dataclass
class Domain(ComplexNode):
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
    def class_name(self):
        return self.domain

    @property
    def module_name(self):
        return convert_to_snake_case(self.domain)

    def get_refs(self) -> list[Ref]:
        refs = []

        for type_ in self.types:
            refs += type_.get_refs()

        for command in self.commands:
            refs += command.get_refs()

        for event in self.events:
            refs += event.get_refs()

        return refs
