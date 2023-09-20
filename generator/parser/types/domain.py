from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser import registry
from generator.parser.utils import ExtendedString
from generator.parser.types.base import Node
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
class Domain(Node):
    parent: 'Protocol' = field(
        init=False,
        repr=False
    )

    name: str = field(
        init=False
    )
    description: MaybeUndefined[str] = field(
        init=False
    )
    types: list['Type'] = field(
        init=False
    )
    commands: list['Command'] = field(
        init=False
    )
    events: list['Event'] = field(
        init=False
    )
    dependencies: list[str] = field(
        init=False
    )
    experimental: MaybeUndefined[bool] = field(
        init=False
    )
    deprecated: MaybeUndefined[bool] = field(
        init=False
    )

    def __post_init__(self):
        registry.add_domain(self)

    def resolve(self, parent: None = None):
        self.name = ExtendedString(
            self.raw['domain']
        )

        self.description = self.raw.get(
            'description',
            UNDEFINED
        )

        self.types = [
            Type(type_) for
            type_ in
            self.raw.get(
                'types',
                []
            )
        ]

        self.commands = [
            Command(command) for
            command in
            self.raw.get(
                'commands',
                []
            )
        ]

        self.events = [
            Event(event) for
            event in
            self.raw.get(
                'events',
                []
            )
        ]

        self.dependencies = self.raw.get(
            'dependencies',
            []
        )

        self.experimental = self.raw.get(
            'experimental',
            UNDEFINED
        )

        self.deprecated = self.raw.get(
            'deprecated',
            UNDEFINED
        )

        for type_ in self.types:
            type_.resolve(self)

        for command in self.commands:
            command.resolve(self)

        for event in self.events:
            event.resolve(self)

    def get_refs(self) -> list[Ref]:
        refs = []

        for type_ in self.types:
            for property_ in type_.properties:
                if property_.ref:
                    refs.append(property_.ref)

                if property_.items:
                    if property_.items.ref:
                        refs.append(property_.items.ref)

        for command in self.commands:
            for parameter in command.parameters:
                if parameter.ref:
                    refs.append(parameter.ref)

                if parameter.items:
                    if parameter.items.ref:
                        refs.append(parameter.items.ref)

            for return_ in command.returns:
                if return_.ref:
                    refs.append(return_.ref)

                if return_.items:
                    if return_.items.ref:
                        refs.append(return_.items.ref)

        for event in self.events:
            for parameter in event.parameters:
                if parameter.ref:
                    refs.append(parameter.ref)

                if parameter.items:
                    if parameter.items.ref:
                        refs.append(parameter.items.ref)

        return refs
