from abc import ABC
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser.extensions import ExtendedString
from generator.parser.types.base import ComplexNode
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
class Property(ComplexNode, ABC):
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

    @classmethod
    def from_dict(cls, data):
        ref = data.get('$ref', UNDEFINED)

        if is_defined(ref):
            ref = PropertyRef.from_str(ref)

        items = data.get('items', UNDEFINED)

        if is_defined(items):
            items = Items.from_dict(items)

        return cls(
            name=data['name'],
            type=data.get('type', UNDEFINED),
            ref=ref,
            items=items,
            description=data.get('description', UNDEFINED),
            optional=data.get('optional', UNDEFINED),
            experimental=data.get('experimental', UNDEFINED),
            deprecated=data.get('deprecated', UNDEFINED)
        )

    @property
    def actual_domain(self):
        return self.parent.actual_domain

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

    @property
    def name_(self):
        return ExtendedString(self.name)

    def get_refs(self) -> list[PropertyRef]:
        if is_defined(self.ref):
            return [self.ref]
        else:
            return []


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
