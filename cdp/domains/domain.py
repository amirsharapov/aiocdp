from dataclasses import dataclass
from typing import TYPE_CHECKING

from cdp.domains.base import BaseDomain

if TYPE_CHECKING:
    from cdp.domains.domains import Domains


@dataclass
class Domain(BaseDomain):
    name: str
    domains: 'Domains'

    def __getattr__(self, item: str):
        method = f'{self.name}.{item}'

        def wrapper(params: dict):
            return self._send_command(
                method,
                params
            )

        return wrapper
