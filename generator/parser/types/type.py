from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser.types.base import ComplexNode
from generator.parser.types.items import Items
from generator.parser.types.property import TypeProperty
from generator.utils import UNDEFINED, MaybeUndefined, snake_case, pascal_case, is_builtin

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain
    from generator.parser.types.ref import Ref


@dataclass
class Type(ComplexNode):
    parent: 'Domain' = field(
        init=False,
        repr=False
    )

    id: str
    type: str
    description: MaybeUndefined[str]
    properties: list['TypeProperty']
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
            properties=[
                TypeProperty.from_dict(property_)
                for property_ in data.get('properties', [])
            ],
            enum=data.get('enum', []),
            items=items,
            experimental=data.get('experimental', UNDEFINED),
            deprecated=data.get('deprecated', UNDEFINED)
        )

    @property
    def actual_domain(self) -> 'Domain':
        return self.parent

    @property
    def id_snake_case(self):
        return snake_case(self.id)

    @property
    def id_snake_case_collision_safe(self):
        res = self.id_snake_case
        if is_builtin(res):
            res += '_'
        return res

    @property
    def id_pascal_case(self):
        return pascal_case(self.id)

    def get_refs(self) -> list['Ref']:
        refs = []

        for property_ in self.properties:
            refs += property_.get_refs()

        return refs
