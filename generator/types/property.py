from dataclasses import dataclass

from generator.types.base import ComplexNode
from generator.types.items import Items
from generator.types.ref import Ref
from generator.utils import UNDEFINED, MaybeUndefined, is_defined, snake_case, camel_case, pascal_case


@dataclass
class Property(ComplexNode):
    name: str
    type: MaybeUndefined[str]
    ref: MaybeUndefined[Ref]
    items: MaybeUndefined['Items']
    description: MaybeUndefined[str]
    optional: MaybeUndefined[bool]
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @property
    def name_snake_cased(self):
        return snake_case(self.name)

    @property
    def name_camel_cased(self):
        return camel_case(self.name)

    @property
    def name_pascal_cased(self):
        return pascal_case(self.name)

    @classmethod
    def from_dict(cls, data):
        ref = data.get('$ref', UNDEFINED)

        if is_defined(ref):
            ref = Ref.from_str(ref)

        items = data.get('items', UNDEFINED)

        if is_defined(items):
            items = Items.from_dict(items)

        return cls(
            name=data['name'],
            type=data.get('type', UNDEFINED),
            ref=ref,
            items=items,
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
