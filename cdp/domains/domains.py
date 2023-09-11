from dataclasses import dataclass
from typing import TYPE_CHECKING

from cdp.domains.dynamic import DynamicDomain

if TYPE_CHECKING:
    from cdp.target import Target


@dataclass
class Domains:
    target: 'Target'

    def __post_init__(self):
        self._domains = {}

    def __getattr__(self, item: str):
        if item not in self._domains:
            self._domains[item] = DynamicDomain(
                item,
                self
            )

        return self._domains[item]
