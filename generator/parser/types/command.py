from typing import TYPE_CHECKING
from dataclasses import dataclass, field

from generator.parser.utils import ExtendedString
from generator.parser.types.base import Node
from generator.parser.types.property import CommandParameter, CommandReturnProperty
from generator.utils import UNDEFINED, MaybeUndefined, snake_case, pascal_case

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain


@dataclass
class Command(Node):
    parent: 'Domain' = field(
        init=False,
        repr=False
    )

    name: 'ExtendedString' = field(
        init=False
    )
    description: MaybeUndefined[str] = field(
        init=False
    )
    parameters: list['CommandParameter'] = field(
        init=False
    )
    returns: list['CommandReturnProperty'] = field(
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
        return self.parent

    def resolve(self, parent: 'Domain'):
        self.name = ExtendedString(
            self.raw['name']
        )

        self.description = self.raw.get(
            'description',
            UNDEFINED
        )

        self.parameters = [
            CommandParameter(parameter) for
            parameter in
            self.raw.get(
                'parameters',
                []
            )
        ]

        self.returns = [
            CommandReturnProperty(return_) for
            return_ in
            self.raw.get(
                'returns',
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

        for return_ in self.returns:
            return_.resolve(self)
