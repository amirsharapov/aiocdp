from abc import ABC
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.types.base import ComplexNode
from generator.utils import MaybeUndefined, UNDEFINED
from generator.types.ref import Ref

if TYPE_CHECKING:
    from generator.types.property import Property
    from generator.types.type import Type


@dataclass
class Items(ComplexNode, ABC):
    type: MaybeUndefined[str]
    ref: MaybeUndefined[Ref]

    @classmethod
    def from_dict(cls, data):
        ref = data.get('$ref', None)

        if ref:
            ref = Ref.from_str(ref)

        return cls(
            type=data.get('type', UNDEFINED),
            ref=ref
        )

    @property
    def actual_ref(self) -> 'Ref':
        if self.ref:
            return self.ref


@dataclass
class PropertyItems(Items):
    parent: 'Property' = field(
        init=False
    )

    @property
    def inferred_domain(self):
        return self.parent.parent.parent.domain

    def register(self):
        pass


@dataclass
class TypeItems(Items):
    parent: 'Type' = field(
        init=False
    )

    @property
    def inferred_domain(self):
        return self.parent.parent.domain

    def register(self):
        pass
