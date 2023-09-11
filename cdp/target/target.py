from dataclasses import dataclass, field
from typing import Optional

from websocket import WebSocket

from cdp.domains.domains import Domains


@dataclass
class Target:
    domains: Domains = field(init=False)
    connection: Optional['WebSocket'] = field(init=False)

    def __post_init__(self):
        self.domains = Domains(self)
        self.connection = None

    def send_command(self, method: str, params: dict = None):
        raise NotImplementedError
