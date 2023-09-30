from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from pycdp.connection.connection import Connection
from pycdp.connection.stream import EventStream

if TYPE_CHECKING:
    from pycdp.chrome import Chrome


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
    def is_connected(self):
        return self._connection is not None

    @property
    def is_session_started(self):
        return self._session_id is not None

    @property
    def ws_url(self):
        return f'ws://{self.chrome.host}:{self.chrome.port}/devtools/page/{self.info.id}'

    def __post_init__(self):
        self._connection = Connection(self.ws_url)
        self._session_id = None

    async def close_session(self):
        await self._connection.send(
            'Target.detachFromTarget',
            {
                'sessionId': self._session_id
            }
        )

    def close_stream(self, stream: EventStream):
        return self._connection.close_stream(stream)

    async def connect(self, skip_if_already_connected: bool = True):
        if (
            skip_if_already_connected and
            self.is_connected
        ):
            return

        return await self._connection.connect()

    def open_stream(self, events: list[str]):
        return self._connection.open_stream(events)

    async def send(self, method: str, params: dict = None):
        params = params or {}

        return await self._connection.send(
            method,
            {
                'sessionId': self._session_id,
                **params,
            }
        )

    async def send_and_await_response(self, method: str, params: dict = None):
        return await (await self.send(
            method,
            params
        ))

    async def start_session(self, skip_if_session_already_started: bool = True):
        if (
            skip_if_session_already_started and
            self.is_session_started
        ):
            return

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
