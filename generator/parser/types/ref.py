from abc import ABC
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional

from generator.parser import registry
from generator.parser.types.base import Node
from generator.utils import UNDEFINED, MaybeUndefined

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain
    from generator.parser.types.items import Items
    from generator.parser.types import Type
    from generator.parser.types.property import Property


@dataclass
class Ref(Node, ABC):
    parent: 'Property | Items' = field(
        init=False,
        repr=False
    )

    type: Optional['Type'] = field(
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

    def __post_init__(self):
        self.type = None

    def resolve_type(self):
        split = self.raw.split('.')

        if len(split) == 1:
            self.type = registry.get_type(
                self.domain.domain,
                split[0]
            )

        elif len(split) == 2:
            self.type = registry.get_type(
                split[0],
                split[1]
            )

        else:
            raise ValueError(
                f'Invalid ref: {self.raw}'
            )


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
