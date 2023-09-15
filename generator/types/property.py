from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.types.base import ComplexNode
from generator.types.items import PropertyItems
from generator.types.ref import Ref
from generator.utils import UNDEFINED, MaybeUndefined, is_defined, snake_case, camel_case, pascal_case

if TYPE_CHECKING:
    from generator.types import Type
    from generator.types.command import Command
    from generator.types.event import Event


@dataclass
class Property(ComplexNode):
    parent: 'Type' = field(
        init=False
    )

    name: str
    type: MaybeUndefined[str]
    ref: MaybeUndefined[Ref]
    items: MaybeUndefined['PropertyItems']
    description: MaybeUndefined[str]
    optional: MaybeUndefined[bool]
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @property
    def name_snake_cased(self):
        return snake_case(self.name)

    @property
    def name_camel_cased(self):
        return camel_case(self.name)

    @property
    def name_pascal_cased(self):
        return pascal_case(self.name)

    @classmethod
    def from_dict(cls, data):
        ref = data.get('$ref', UNDEFINED)

        if is_defined(ref):
            ref = Ref.from_str(ref)

        items = data.get('items', UNDEFINED)

        if is_defined(items):
            items = PropertyItems.from_dict(items)

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

    def get_refs(self):
        if is_defined(self.ref):
            return [self.ref]
        else:
            return []


@dataclass
class CommandParameter(Property):
    parent: 'Command' = field(
        init=False
    )


@dataclass
class EventParameter(Property):
    parent: 'Event' = field(
        init=False
    )


@dataclass
class Return(Property):
    pass
