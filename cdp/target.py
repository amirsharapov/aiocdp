from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from cdp.connection.connection import Connection

if TYPE_CHECKING:
    from cdp.chrome import Chrome


@dataclass
class Target:
    connection: Connection = field(
        init=False,
        repr=False
    )
    session_id: str | None = field(
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
        self.connection = Connection(self.ws_url)
        self.session_id = None

    async def connect(self):
        return await self.connection.connect()

    async def open_events_stream(self, events: list[str]):
        return await self.connection.open_stream(events)

    async def send(self, method: str, params: dict = None):
        params = params or {}

        if self.session_id:
            params['sessionId'] = self.session_id

        return await self.connection.send(
            method,
            params
        )

    async def start_session(self):
        result = await self.connection.send(
            'Target.attachToTarget',
            {
                'targetId': self.id
            }
        )

        self.session_id = (await result)['sessionId']
