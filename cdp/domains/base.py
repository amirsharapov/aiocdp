from abc import ABC
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cdp.target import Target


@dataclass
class BaseDomain(ABC):
    target: 'Target'

    def _send_command(self, method: str, params: dict = None):
        params = params or {}

        return self.target.send_command(
            method,
            params
        )
