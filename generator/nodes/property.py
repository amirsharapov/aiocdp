from dataclasses import dataclass

from generator.nodes.base import Node
from generator.utils import MaybeUndefined, UNDEFINED, is_defined


@dataclass
class Property(Node):
    name: str
    type: MaybeUndefined[str]
    ref: MaybeUndefined[str]
    description: MaybeUndefined[str]
    optional: MaybeUndefined[bool]
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            type=data.get('type', UNDEFINED),
            ref=data.get('$ref', UNDEFINED),
            description=data.get('description', UNDEFINED),
            optional=data.get('optional', UNDEFINED),
            experimental=data.get('experimental', UNDEFINED),
            deprecated=data.get('deprecated', UNDEFINED)
        )

    def get_refs(self):
        if is_defined(self.ref):
            return [self.ref]
        else:
            return []


@dataclass
class Parameter(Property):
    pass


@dataclass
class Return(Property):
    pass
