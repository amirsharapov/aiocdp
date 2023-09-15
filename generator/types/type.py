from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator import type_registry
from generator.types.base import ComplexNode
from generator.types.items import TypeItems
from generator.types.property import Property
from generator.utils import UNDEFINED, MaybeUndefined, snake_case

if TYPE_CHECKING:
    from generator.types.domain import Domain


@dataclass
class Type(ComplexNode):
    parent: 'Domain' = field(
        init=False
    )

    id: str
    type: str
    description: MaybeUndefined[str]
    properties: list['Property']
    enum: list[str]
    items: MaybeUndefined['TypeItems']
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @classmethod
    def from_dict(cls, data):
        items = data.get('items', UNDEFINED)

        if items:
            items = TypeItems.from_dict(items)

        return cls(
            id=data['id'],
            type=data['type'],
            description=data.get('description', UNDEFINED),
            properties=[Property.from_dict(property_) for property_ in data.get('properties', [])],
            enum=data.get('enum', []),
            items=items,
            experimental=data.get('experimental', UNDEFINED),
            deprecated=data.get('deprecated', UNDEFINED)
        )

    @property
    def id_snake_case(self):
        return snake_case(self.id)

    @property
    def inferred_domain(self):
        return self.parent.domain

    def get_refs(self):
        refs = []

        for property_ in self.properties:
            refs += property_.get_refs()

        return refs
