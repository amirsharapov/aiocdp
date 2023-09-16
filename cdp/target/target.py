from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional

from cdp.domains.domains import Domains
from cdp.target.connection import Connection

if TYPE_CHECKING:
    from cdp.chrome import Chrome


@dataclass
class Target:
    domains: Domains = field(
        init=False,
        repr=False
    )
    connection: 'Connection' = field(
        init=False,
        repr=False
    )
    active_session_id: Optional[str] = field(
        init=False
    )

    chrome: 'Chrome'
    id: str

    def __post_init__(self):
        self.domains = Domains(self)
        self.connection = Connection(
            f'ws://{self.chrome.host}:{self.chrome.port}/devtools/page/{self.id}'
        )
        self.active_session_id = None

    def connect(self):
        self.connection.connect()

    def open_session(self):
        result = self.domains.target.attach_to_target(self.id)
        result = result.get()

        self.active_session_id = result.session_id

    def send_command(self, method: str, params: dict, expect_response: bool):
        if self.active_session_id:
            params['sessionId'] = self.active_session_id

        return self.connection.send(
            method,
            params,
            expect_response
        )
