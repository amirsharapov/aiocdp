from abc import ABC
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser import registry
from generator.parser.types.base import ComplexNode
from generator.utils import MaybeUndefined, UNDEFINED
from generator.parser.types.ref import ItemsRef

if TYPE_CHECKING:
    from generator.parser.types.property import Property


@dataclass
class Items(ComplexNode, ABC):
    parent: 'Property' = field(
        init=False,
        repr=False
    )

    type: MaybeUndefined[str]
    ref: MaybeUndefined[ItemsRef]

    @classmethod
    def from_dict(cls, data):
        ref = data.get('$ref', UNDEFINED)

        if ref:
            ref = ItemsRef.from_str(ref)

        return cls(
            type=data.get('type', UNDEFINED),
            ref=ref
        )

    @property
    def actual_domain(self):
        return self.parent.actual_domain
