from dataclasses import dataclass

from generator.types.base import ComplexNode
from generator.types.property import Parameter, Return
from generator.utils import MaybeUndefined, UNDEFINED


@dataclass
class Command(ComplexNode):
    name: str
    description: MaybeUndefined[str]
    parameters: list['Parameter']
    returns: list['Return']
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            description=data.get('description', UNDEFINED),
            parameters=[Parameter.from_dict(parameter) for parameter in data.get('parameters', [])],
            returns=[Return.from_dict(parameter) for parameter in data.get('returns', [])],
            experimental=data.get('experimental', UNDEFINED),
            deprecated=data.get('deprecated', UNDEFINED)
        )

    def get_refs(self):
        refs = []

        for parameter in self.parameters:
            refs += parameter.get_refs()

        for return_ in self.returns:
            refs += return_.get_refs()

        return refs
