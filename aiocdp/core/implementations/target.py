from dataclasses import dataclass, field

from aiocdp.core.interfaces.connection import IConnection
from aiocdp.core.interfaces.target import ITarget
from aiocdp.core.interfaces.chrome import IChrome
from aiocdp.core.implementations.connection import Connection
from aiocdp.core.implementations.session import Session
from aiocdp.core.implementations.stream import EventStream

from aiocdp.core.interfaces import ITargetInfo


@dataclass
class TargetInfo(ITargetInfo):
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

    @classmethod
    def init(
            cls,
            id_: str,
            title: str,
            description: str,
            url: str,
            type_: str,
            web_socket_debugger_url: str,
            parent_id: str = None,
            favicon_url: str = None
    ):
        """
        Initializer method for the ITargetInfo class
        """
        return cls(
            id=id_,
            title=title,
            description=description,
            url=url,
            type=type_,
            web_socket_debugger_url=web_socket_debugger_url,
            parent_id=parent_id,
            favicon_url=favicon_url
        )


@dataclass
class Target(ITarget):
    """
    Represents a CDP target.
    """
    _connection: 'IConnection' = field(
        init=False,
        repr=False
    )

    """
    A reference to the parent chrome instance
    """
    chrome: 'IChrome'

    """
    A reference to the target info.
    """
    info: 'ITargetInfo'

    @classmethod
    def init(
        cls,
        chrome: IChrome,
        info: ITargetInfo
    ):
        """
        Initializer method for the ITarget class
        """
        return cls(
            chrome=chrome,
            info=info
        )

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

    def get_info(self):
        return self.info

    async def close_session(self, session: 'Session'):
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
        session = Session(self)
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
