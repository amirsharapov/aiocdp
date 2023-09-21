from abc import ABC
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser.types.datatype import DataType
from generator.parser.utils import ExtendedString
from generator.parser.types.base import Node
from generator.parser.types.items import Items
from generator.parser.types.ref import PropertyRef
from generator.utils import UNDEFINED, MaybeUndefined, is_defined, snake_case, camel_case, pascal_case, is_builtin

if TYPE_CHECKING:
    from generator.parser.types import Type
    from generator.parser.types.command import Command
    from generator.parser.types.event import Event


def order_by_required_flag(properties: list['Property']):
    required = []
    optional = []

    for property_ in properties:
        if is_defined(property_.optional):
            optional.append(property_)
        else:
            required.append(property_)

    return required + optional


@dataclass
class Property(Node, ABC):
    parent: 'Type | Command | Event' = field(
        init=False,
        repr=False
    )

    name: str = field(
        init=False
    )
    type: MaybeUndefined[DataType] = field(
        init=False
    )
    ref: MaybeUndefined[PropertyRef] = field(
        init=False
    )
    items: MaybeUndefined['Items'] = field(
        init=False
    )
    description: MaybeUndefined[str] = field(
        init=False
    )
    optional: MaybeUndefined[bool] = field(
        init=False
    )
    experimental: MaybeUndefined[bool] = field(
        init=False
    )
    deprecated: MaybeUndefined[bool] = field(
        init=False
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

    def __post_init__(self):
        self.name = ExtendedString(
            self.raw['name']
        )

        self.type = DataType.from_maybe_undefined(
            self.raw.get(
                'type',
                UNDEFINED
            )
        )

        self.ref = PropertyRef.from_maybe_undefined(
            self.raw.get(
                '$ref',
                UNDEFINED
            )
        )

        self.items = Items.from_maybe_undefined(
            self.raw.get(
                'items',
                UNDEFINED
            )
        )

        self.description = self.raw.get(
            'description',
            UNDEFINED
        )

        self.optional = self.raw.get(
            'optional',
            UNDEFINED
        )

        self.experimental = self.raw.get(
            'experimental',
            UNDEFINED
        )

        self.deprecated = self.raw.get(
            'deprecated',
            UNDEFINED
        )


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
