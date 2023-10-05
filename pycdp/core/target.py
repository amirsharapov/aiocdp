from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from pycdp.core.connection import Connection
from pycdp.core.session import TargetSession
from pycdp.core.events import EventStream

if TYPE_CHECKING:
    from pycdp.core.chrome import Chrome


@dataclass
class TargetInfo:
    """
    Represents information about a target.
    """
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
    """
    Represents a CDP target.
    """
    _connection: Connection = field(
        init=False,
        repr=False
    )

    chrome: 'Chrome'
    info: TargetInfo

    @property
    def is_connected(self):
        """
        Public readonly access to the connection status.
        """
        return self._connection.is_connected

    @property
    def ws_url(self):
        """
        A readonly property Web socket url.
        """
        return f'ws://{self.chrome.host}:{self.chrome.port}/devtools/page/{self.info.id}'

    def __post_init__(self):
        """
        Assigns the connection to the target.
        """
        self._connection = Connection(self.ws_url)

    async def close_session(self, session: 'TargetSession'):
        """
        Closes the session. Calls `TargetSession.close`.
        """
        await session.close()

    def close_stream(self, stream: EventStream):
        """
        Closes the stream. Calls `Connection.close_stream`.
        """
        return self._connection.close_stream(stream)

    async def connect(self):
        """
        Connects to the target. Calls `Connection.connect`.
        """
        return await self._connection.connect()

    async def disconnect(self):
        """
        Disconnects from the target. Calls `Connection.disconnect`.
        """
        return await self._connection.disconnect()

    def open_stream(self, events: list[str]):
        """
        Opens a stream. Calls `Connection.open_stream`.
        """
        return self._connection.open_stream(events)

    async def open_session(self):
        """
        Opens a session with the target.
        """
        session = TargetSession.create(self)
        await session.open()

        return session

    async def send(self, method: str, params: dict = None):
        """
        Sends a message to the target. Calls `Connection.send`.
        """
        return await self._connection.send(
            method,
            params or {}
        )

    async def send_and_await_response(self, method: str, params: dict = None):
        """
        Sends a message to the target and awaits a response. Calls `Connection.send_and_await_response`
        """
        return await (await self.send(
            method,
            params
        ))
