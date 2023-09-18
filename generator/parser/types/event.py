from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser.types.base import ComplexNode
from generator.parser.types.property import EventProperty
from generator.utils import UNDEFINED, MaybeUndefined

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain


@dataclass
class Event(ComplexNode):
    parent: 'Domain' = field(
        init=False,
        repr=False
    )

    name: str
    description: MaybeUndefined[str]
    parameters: list['EventProperty']
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            description=data.get('description', UNDEFINED),
            parameters=[
                EventProperty.from_dict(parameter)
                for parameter in data.get('parameters', [])
            ],
            experimental=data.get('experimental', UNDEFINED),
            deprecated=data.get('deprecated', UNDEFINED)
        )

    @property
    def actual_domain(self):
        return self.parent

    def get_refs(self):
        refs = []

        for parameter in self.parameters:
            refs += parameter.get_refs()

        return refs
