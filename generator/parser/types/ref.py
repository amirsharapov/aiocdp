from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator.parser import registry
from generator.parser.types.base import Node
from generator.utils import UNDEFINED, MaybeUndefined

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain
    from generator.parser.types.items import Items
    from generator.parser.types.property import Property


@dataclass
class Ref(Node, ABC):
    domain: MaybeUndefined[str]
    type: str

    @classmethod
    def from_str(cls, s: str):
        if '.' in s:
            s = s.split('.')
            return cls(
                domain=s[0],
                type=s[1]
            )

        else:
            return cls(
                domain=UNDEFINED,
                type=s
            )

    @property
    def actual_type(self):
        return registry.get_type(
            self.domain or self.actual_domain.domain,
            self.type
        )

    @property
    @abstractmethod
    def actual_domain(self) -> 'Domain':
        ...


@dataclass
class PropertyRef(Ref):
    parent: 'Property' = field(
        init=False,
        repr=False
    )

    @property
    def actual_domain(self) -> 'Domain':
        return self.parent.actual_domain


@dataclass
class ItemsRef(Ref):
    parent: 'Items' = field(
        init=False,
        repr=False
    )

    @property
    def actual_domain(self) -> 'Domain':
        return self.parent.actual_domain
