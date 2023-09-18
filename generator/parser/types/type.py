from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser.extensions import ExtendedString
from generator.parser.types.base import ComplexNode
from generator.parser.types.items import Items
from generator.parser.types.property import (
    TypeProperty,
    split_properties_by_optional_flag
)
from generator.utils import UNDEFINED, MaybeUndefined

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain
    from generator.parser.types.ref import Ref


@dataclass
class Type(ComplexNode):
    parent: 'Domain' = field(
        init=False,
        repr=False
    )

    optional_properties: list['TypeProperty'] = field(
        init=False,
        repr=False
    )
    required_properties: list['TypeProperty'] = field(
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

    def __post_init__(self):
        required, optional = split_properties_by_optional_flag(
            self.properties
        )

        self.required_properties = required
        self.optional_properties = optional

    @property
    def actual_domain(self) -> 'Domain':
        return self.parent

    @property
    def id_(self):
        return ExtendedString(self.id)

    @property
    def properties_with_required_first(self):
        return self.required_properties + self.optional_properties

    def get_refs(self) -> list['Ref']:
        refs = []

        for property_ in self.properties:
            refs += property_.get_refs()

        return refs
