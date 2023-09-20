from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser.types.base import Node
from generator.parser.types.property import EventProperty
from generator.parser.utils import ExtendedString
from generator.utils import UNDEFINED, MaybeUndefined

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain


@dataclass
class Event(Node):
    parent: 'Domain' = field(
        init=False,
        repr=False
    )

    name: ExtendedString = field(
        init=False
    )
    description: MaybeUndefined[str] = field(
        init=False
    )
    parameters: list['EventProperty'] = field(
        init=False
    )
    experimental: MaybeUndefined[bool] = field(
        init=False
    )
    deprecated: MaybeUndefined[bool] = field(
        init=False
    )

    def resolve(self, parent: 'Domain'):
        self.name = ExtendedString(
            self.raw['name']
        )

        self.description = self.raw.get(
            'description',
            UNDEFINED
        )

        self.parameters = [
            EventProperty(parameter) for
            parameter in
            self.raw.get(
                'parameters',
                []
            )
        ]

        self.experimental = self.raw.get(
            'experimental',
            UNDEFINED
        )

        self.deprecated = self.raw.get(
            'deprecated',
            UNDEFINED
        )

        for parameter in self.parameters:
            parameter.resolve(self)

    @property
    def domain(self):
        return self.parent
