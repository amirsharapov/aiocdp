from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from cdp.connection.connection import Connection
from cdp.io import IO

if TYPE_CHECKING:
    from cdp.chrome import Chrome


@dataclass
class Target:
    io: IO = field(
        init=False,
        repr=False
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
        connection = Connection(self.ws_url)
        session_id = None

        self.io = IO(
            connection,
            session_id
        )

    async def connect(self):
        return await self.io.connection.connect()

    async def open_session(self):
        result = await self.io.send(
            'Target.attachToTarget',
            {
                'targetId': self.id
            }
        )

        self.io.session_id = result['sessionId']
