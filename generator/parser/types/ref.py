from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser import registry
from generator.parser.types import Type
from generator.parser.types.base import Node
from generator.utils import UNDEFINED, MaybeUndefined

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain
    from generator.parser.types.items import Items
    from generator.parser.types.property import Property


@dataclass
class Ref(Node, ABC):
    parent: 'Property | Items' = field(
        init=False,
        repr=False
    )

    type: 'Type' = field(
        init=False
    )

    raw: str

    @classmethod
    def from_maybe_undefined(cls, raw: MaybeUndefined[str]) -> MaybeUndefined['Ref']:
        if raw is UNDEFINED:
            return UNDEFINED

        return cls(raw)

    @property
    def domain(self) -> 'Domain':
        return self.parent.domain

    def resolve(self):
        split = self.raw.split('.')

        if len(split) == 1:
            self.type = split[0]

        elif len(split) == 2:
            self.type = split[1]

        else:
            raise ValueError(f'Invalid ref: {self.raw}')


@dataclass
class PropertyRef(Ref):
    parent: 'Property' = field(
        init=False,
        repr=False
    )


@dataclass
class ItemsRef(Ref):
    parent: 'Items' = field(
        init=False,
        repr=False
    )
