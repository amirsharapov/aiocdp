from abc import ABC
from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from cdp.target import Target


@dataclass
class BaseDomain(ABC):
    target: 'Target'

    def _send_command(
            self,
            method: str,
            params: dict,
            expect_response: bool,
            response_hook: Callable = None
    ):
        return self.target.send_command(
            method,
            params,
            expect_response,
            response_hook
        )
