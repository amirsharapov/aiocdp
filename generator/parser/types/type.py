from dataclasses import (
    dataclass,
    field
)
from typing import (
    TYPE_CHECKING
)

from generator.parser import registry
from generator.parser.types.datatype import DataType
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
    order_by_required_flag
)
from generator.utils import (
    UNDEFINED,
    MaybeUndefined
)

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain


@dataclass
class Type(Node):
    parent: 'Domain' = field(
        init=False,
        repr=False
    )

    id: 'ExtendedString' = field(
        init=False,
    )
    type: DataType = field(
        init=False,
    )
    description: MaybeUndefined[str] = field(
        init=False,
    )
    properties: list['TypeProperty'] = field(
        init=False,
    )
    enum: list[str] = field(
        init=False,
    )
    items: MaybeUndefined['Items'] = field(
        init=False,
    )
    experimental: MaybeUndefined[bool] = field(
        init=False,
    )
    deprecated: MaybeUndefined[bool] = field(
        init=False,
    )

    @property
    def domain(self) -> 'Domain':
        return self.parent

    def __post_init__(self):
        self.id = ExtendedString(
            self.raw.get(
                'id',
                UNDEFINED
            )
        )

        self.type = DataType.from_maybe_undefined(
            self.raw.get(
                'type',
                UNDEFINED
            )
        )

        self.description = self.raw.get(
            'description',
            UNDEFINED
        )

        self.properties = order_by_required_flag([
            TypeProperty(property_) for
            property_ in
            self.raw.get(
                'properties',
                []
            )
        ])

        self.enum = self.raw.get(
            'enum',
            UNDEFINED
        )

        self.items = Items.from_maybe_undefined(
            self.raw.get(
                'items',
                UNDEFINED
            )
        )

        self.experimental = self.raw.get(
            'experimental',
            UNDEFINED
        )
        self.deprecated = self.raw.get(
            'deprecated',
            UNDEFINED
        )

        registry.add_type(self)
