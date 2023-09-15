from typing import TYPE_CHECKING
from dataclasses import dataclass, field

from generator.types.base import ComplexNode
from generator.types.property import CommandParameter, Return
from generator.utils import UNDEFINED, MaybeUndefined, snake_case, pascal_case

if TYPE_CHECKING:
    from generator.types.domain import Domain


@dataclass
class Command(ComplexNode):
    parent: 'Domain' = field(
        init=False
    )

    name: str
    description: MaybeUndefined[str]
    parameters: list['CommandParameter']
    returns: list['Return']
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            description=data.get('description', UNDEFINED),
            parameters=[CommandParameter.from_dict(parameter) for parameter in data.get('parameters', [])],
            returns=[Return.from_dict(return_) for return_ in data.get('returns', [])],
            experimental=data.get('experimental', UNDEFINED),
            deprecated=data.get('deprecated', UNDEFINED)
        )

    @property
    def name_snake_case(self):
        return snake_case(self.name)

    @property
    def name_pascal_case(self):
        return pascal_case(self.name)

    def get_refs(self):
        refs = []

        for parameter in self.parameters:
            refs += parameter.get_refs()

        for return_ in self.returns:
            refs += return_.get_refs()

        return refs
