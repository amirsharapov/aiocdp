from dataclasses import field, dataclass

from cdp.domains.domain import Domain
from cdp.target import Target


@dataclass
class Domains:
    ws_target: 'Target'

    _cache: dict = field(
        init=False,
        repr=False
    )

    def __post_init__(self):
        self._cache = {}

    def __getattr__(self, item: str):
        if item not in self._cache:
            self._cache[item] = Domain(
                self,
                item
            )

        return self._cache[item]
