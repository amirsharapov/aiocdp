from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from generator import type_registry
from generator.types.base import Node
from generator.utils import UNDEFINED, MaybeUndefined, snake_case, is_undefined

if TYPE_CHECKING:
    from generator.types import Property


@dataclass
class Ref(Node):
    parent: 'Property' = field(
        init=False,
        repr=False
    )
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
        return type_registry.get_type(
            self.inferred_domain,
            self.type
        )

    @property
    def domain_snake_case(self):
        return snake_case(self.inferred_domain)

    @property
    def inferred_domain(self):
        if is_undefined(self.domain):
            return self.parent.parent.parent.domain
        else:
            return self.domain
