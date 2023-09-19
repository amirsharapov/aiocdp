from abc import ABC
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cdp.domains.domains import Domains


@dataclass
class BaseDomain(ABC):
    domains: 'Domains'

    def _send_command(
            self,
            method: str,
            params: dict
    ):
        return self.domains.ws_target.send_command(
            method,
            params,
        )
