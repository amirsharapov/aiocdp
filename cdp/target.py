from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional

from cdp.connection.connection import Connection

if TYPE_CHECKING:
    from cdp.chrome import Chrome

@dataclass
class Target:
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
        self.connection = Connection(self.ws_url)
        self.active_session_id = None

    async def connect(self):
        return await self.connection.connect()

    async def open_session(self):
        result = await self.send(
            'Target.attachToTarget',
            {
                'targetId': self.id,
                'flatten': True
            }
        )

        self.active_session_id = result['sessionId']

    async def send(
            self,
            method: str,
            params: dict,
            expect_response: bool = True,
    ) -> dict:
        if self.active_session_id:
            params['sessionId'] = self.active_session_id

        return await self.connection.send_request(
            method,
            params,
            expect_response,
        )
