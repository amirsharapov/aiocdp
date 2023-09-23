from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional

from cdp.domains.domains import Domains
from cdp.target.connection import Connection, IFutureResponse

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
    title: str
    description: str
    url: str
    type: str
    web_socket_debugger_url: str

    parent_id: str = field(
        default=None
    )
    favicon_url: str = field(
        default=None
    )

    @property
    def ws_url(self):
        return f'ws://{self.chrome.host}:{self.chrome.port}/devtools/page/{self.id}'
    
    def __post_init__(self):
        self.domains = Domains(self)
        self.connection = Connection(self.ws_url)
        self.active_session_id = None

    def connect(self):
        self.connection.connect()

    def open_session(self):
        result = self.domains.target.attach_to_target({
            'target_id': self.id,
            'flatten': True
        })

        self.domains.target.attach_to_target(
            target_id=self.id,
        )

        self.active_session_id = result['session_id']

    def send_command(
            self,
            method: str,
            params: dict,
    ) -> IFutureResponse:
        if self.active_session_id:
            params['sessionId'] = self.active_session_id

        return self.connection.send_request(
            method,
            params,
        )
