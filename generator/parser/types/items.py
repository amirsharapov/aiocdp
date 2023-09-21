from abc import ABC
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser.types.base import Node
from generator.parser.types.datatype import DataType
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

    type: MaybeUndefined[DataType] = field(
        init=False
    )
    ref: MaybeUndefined[ItemsRef] = field(
        init=False
    )

    @classmethod
    def from_maybe_undefined(cls, raw: MaybeUndefined[dict]) -> MaybeUndefined['Items']:
        if raw is UNDEFINED:
            return UNDEFINED

        return cls(raw)

    @property
    def domain(self):
        return self.parent.domain

    def __post_init__(self):
        self.type = DataType.from_maybe_undefined(
            self.raw.get(
                'type',
                UNDEFINED
            )
        )

        self.ref = ItemsRef.from_maybe_undefined(
            self.raw.get(
                '$ref',
                UNDEFINED
            )
        )
