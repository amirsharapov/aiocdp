from typing import TYPE_CHECKING
from dataclasses import dataclass, field

from generator.parser.extensions import ExtendedString
from generator.parser.types.base import ComplexNode
from generator.parser.types.property import CommandParameter, CommandReturnProperty
from generator.utils import UNDEFINED, MaybeUndefined, snake_case, pascal_case

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain
    from generator.parser.types.ref import Ref


@dataclass
class Command(ComplexNode):
    parent: 'Domain' = field(
        init=False,
        repr=False
    )

    name: str
    description: MaybeUndefined[str]
    parameters: list['CommandParameter']
    returns: list['CommandReturnProperty']
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            description=data.get('description', UNDEFINED),
            parameters=[
                CommandParameter.from_dict(parameter)
                for parameter in data.get('parameters', [])
            ],
            returns=[
                CommandReturnProperty.from_dict(return_)
                for return_ in data.get('returns', [])
            ],
            experimental=data.get('experimental', UNDEFINED),
            deprecated=data.get('deprecated', UNDEFINED)
        )

    @property
    def actual_domain(self):
        return self.parent

    @property
    def name_(self):
        return ExtendedString(self.name)

    @property
    def return_type_name(self):
        if self.returns:
            return self.name_.pascal_case + 'ReturnType'

    def get_refs(self) -> list['Ref']:
        refs = []

        for parameter in self.parameters:
            refs += parameter.get_refs()

        for return_ in self.returns:
            refs += return_.get_refs()

        return refs
