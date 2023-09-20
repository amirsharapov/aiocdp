from abc import ABC
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser.types.base import Node
from generator.utils import MaybeUndefined, UNDEFINED
from generator.parser.types.ref import ItemsRef

if TYPE_CHECKING:
    from generator.parser.types.property import Property


@dataclass
class Items(Node, ABC):
    parent: 'Property' = field(
        init=False,
        repr=False
    )

    type: MaybeUndefined[str] = field(
        init=False
    )
    ref: MaybeUndefined[ItemsRef] = field(
        init=False
    )

    def resolve(self):
        self.type = self.raw.get(
            'type',
            UNDEFINED
        )

        ref = self.raw.get(
            '$ref',
            UNDEFINED
        )

        if ref:
            ref = ItemsRef(
                ref
            )

        self.ref = ref

    @property
    def domain(self):
        return self.parent.domain
