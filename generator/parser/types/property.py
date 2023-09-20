from abc import ABC
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser.utils import ExtendedString
from generator.parser.types.base import Node
from generator.parser.types.items import Items
from generator.parser.types.ref import PropertyRef
from generator.utils import UNDEFINED, MaybeUndefined, is_defined, snake_case, camel_case, pascal_case, is_builtin

if TYPE_CHECKING:
    from generator.parser.types import Type
    from generator.parser.types.command import Command
    from generator.parser.types.event import Event


def split_properties_by_optional_flag(properties: list['Property']):
    required = []
    optional = []

    for property_ in properties:
        if is_defined(property_.optional):
            optional.append(property_)
        else:
            required.append(property_)

    return required, optional


@dataclass
class Property(Node, ABC):
    parent: 'Type | Command | Event' = field(
        init=False,
        repr=False
    )

    name: str
    type: MaybeUndefined[str]
    ref: MaybeUndefined[PropertyRef]
    items: MaybeUndefined['Items']
    description: MaybeUndefined[str]
    optional: MaybeUndefined[bool]
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    def resolve(self, parent: 'Type | Command | Event'):
        ref = raw.get('$ref', UNDEFINED)

        if is_defined(ref):
            ref = PropertyRef.from_str(ref)

        items = raw.get('items', UNDEFINED)

        if is_defined(items):
            items = Items.from_dict(items)

        return cls(
            name=raw['name'],
            type=raw.get('type', UNDEFINED),
            ref=ref,
            items=items,
            description=raw.get('description', UNDEFINED),
            optional=raw.get('optional', UNDEFINED),
            experimental=raw.get('experimental', UNDEFINED),
            deprecated=raw.get('deprecated', UNDEFINED)
        )

    @property
    def domain(self):
        return self.parent.domain

    @property
    def is_array_of_complex_type(self):
        return is_defined(self.items) and is_defined(self.items.ref)

    @property
    def is_array_of_simple_type(self):
        return is_defined(self.items) and is_defined(self.items.type)

    @property
    def is_complex_type(self):
        return is_defined(self.ref)

    @property
    def is_simple_type(self):
        return is_defined(self.type)


@dataclass
class TypeProperty(Property):
    parent: 'Type' = field(
        init=False,
        repr=False
    )


@dataclass
class CommandParameter(Property):
    parent: 'Command' = field(
        init=False,
        repr=False
    )


@dataclass
class CommandReturnProperty(Property):
    parent: 'Command' = field(
        init=False,
        repr=False
    )


@dataclass
class EventProperty(Property):
    parent: 'Event' = field(
        init=False,
        repr=False
    )
