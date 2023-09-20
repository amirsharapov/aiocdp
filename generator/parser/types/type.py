from dataclasses import (
    dataclass,
    field
)
from typing import (
    TYPE_CHECKING
)

from generator.parser.utils import (
    ExtendedString
)
from generator.parser.types.base import (
    Node
)
from generator.parser.types.items import (
    Items
)
from generator.parser.types.property import (
    TypeProperty,
    split_properties_by_optional_flag
)
from generator.utils import (
    UNDEFINED,
    MaybeUndefined
)

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain
    from generator.parser.types.ref import Ref


@dataclass
class Type(Node):
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

    id: 'ExtendedString' = field(
        init=False,
        repr=False
    )
    type: str = field(
        init=False,
        repr=False
    )
    description: MaybeUndefined[str] = field(
        init=False,
        repr=False
    )
    properties: list['TypeProperty'] = field(
        init=False,
        repr=False
    )
    enum: list[str] = field(
        init=False,
        repr=False
    )
    items: MaybeUndefined['Items'] = field(
        init=False,
        repr=False
    )
    experimental: MaybeUndefined[bool] = field(
        init=False,
        repr=False
    )
    deprecated: MaybeUndefined[bool] = field(
        init=False,
        repr=False
    )

    raw_data: dict

    def resolve_internal_references(self):
        self.id = ExtendedString(
            self.raw_data.get(
                'id',
                UNDEFINED
            )
        )

        self.type = self.raw_data.get(
            'type',
            UNDEFINED
        )

        self.description = self.raw_data.get(
            'description',
            UNDEFINED
        )

        self.properties = self.raw_data.get(
            'properties',
            UNDEFINED
        )

        if self.properties:
            for i, property_ in enumerate(self.properties):
                self.properties[i] = TypeProperty(property_)

            split = split_properties_by_optional_flag(self.properties)

            self.required_properties = split[0]
            self.optional_properties = split[1]

        self.enum = self.raw_data.get(
            'enum',
            UNDEFINED
        )
        self.items = self.raw_data.get(
            'items',
            UNDEFINED
        )

        if self.items:
            self.items = Items(self.items)

        self.experimental = self.raw_data.get(
            'experimental',
            UNDEFINED
        )
        self.deprecated = self.raw_data.get(
            'deprecated',
            UNDEFINED
        )

    @property
    def domain(self) -> 'Domain':
        return self.parent

    @property
    def properties_with_required_first(self):
        return self.required_properties + self.optional_properties

    def get_refs(self) -> list['Ref']:
        refs = []

        for property_ in self.properties:
            refs += property_.get_refs()

        return refs
