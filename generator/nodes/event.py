from dataclasses import dataclass

from generator.nodes.base import Node
from generator.nodes.property import Parameter
from generator.utils import MaybeUndefined, UNDEFINED


@dataclass
class Event(Node):
    name: str
    description: MaybeUndefined[str]
    parameters: list['Parameter']
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            description=data.get('description', UNDEFINED),
            parameters=[Parameter.from_dict(parameter) for parameter in data.get('parameters', [])],
            experimental=data.get('experimental', UNDEFINED),
            deprecated=data.get('deprecated', UNDEFINED)
        )

    def get_refs(self):
        refs = []

        for parameter in self.parameters:
            refs += parameter.get_refs()

        return refs
