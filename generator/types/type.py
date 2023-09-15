from dataclasses import dataclass

from generator.types.base import ComplexNode
from generator.types.items import Items
from generator.types.property import Property
from generator.utils import UNDEFINED, MaybeUndefined, snake_case


@dataclass
class Type(ComplexNode):
    id: str
    type: str
    description: MaybeUndefined[str]
    properties: list['Property']
    enum: list[str]
    items: MaybeUndefined['Items']
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @classmethod
    def from_dict(cls, data):
        items = data.get('items', UNDEFINED)

        if items:
            items = Items.from_dict(items)

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

    def get_refs(self):
        refs = []

        for property_ in self.properties:
            refs += property_.get_refs()

        return refs
