from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from cdp.connection.connection import Connection
from cdp.connection.stream import EventStream

if TYPE_CHECKING:
    from cdp.chrome import Chrome


@dataclass
class TargetInfo:
    id: str
    title: str
    description: str
    url: str
    type: str
    web_socket_debugger_url: str
    parent_id: str = None
    favicon_url: str = None


@dataclass
class Target:
    _connection: Connection = field(
        init=False,
        repr=False
    )
    _session_id: str | None = field(
        init=False,
        repr=False
    )

    chrome: 'Chrome'
    info: TargetInfo

    @property
    def ws_url(self):
        return f'ws://{self.chrome.host}:{self.chrome.port}/devtools/page/{self.info.id}'

    def __post_init__(self):
        self._connection = Connection(self.ws_url)
        self._session_id = None

    async def close_stream(self, stream: EventStream):
        return await self._connection.close_stream(stream)

    async def connect(self):
        return await self._connection.connect()

    async def open_stream(self, events: list[str]):
        return await self._connection.open_stream(events)

    async def send(self, method: str, params: dict = None):
        params = params or {}

        return await self._connection.send(
            method,
            {
                'sessionId': self._session_id,
                **params,
            }
        )

    async def start_session(self):
        method = 'Target.attachToTarget'
        params = {
            'targetId': self.info.id
        }

        result = await self._connection.send(
            method,
            params
        )
        result = await result

        self._session_id = result['sessionId']
