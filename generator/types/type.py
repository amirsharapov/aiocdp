from dataclasses import dataclass

from generator.types.base import ComplexNode
from generator.types.property import Property
from generator.utils import MaybeUndefined, UNDEFINED


@dataclass
class Type(ComplexNode):
    id: str
    type: str
    description: MaybeUndefined[str]
    properties: list['Property']
    enum: list[str]
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            type=data['type'],
            description=data.get('description', UNDEFINED),
            properties=[Property.from_dict(property_) for property_ in data.get('properties', [])],
            enum=data.get('enum', []),
            experimental=data.get('experimental', UNDEFINED),
            deprecated=data.get('deprecated', UNDEFINED)
        )

    def get_refs(self):
        refs = []

        for property_ in self.properties:
            refs += property_.get_refs()

        return refs
