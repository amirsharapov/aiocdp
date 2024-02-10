from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

from aiocdp.core.interfaces.session import ISession
from aiocdp.core.interfaces.stream import IEventStream, IEventStreamReader

if TYPE_CHECKING:
    from aiocdp.core.interfaces.chrome import IChrome


class ITargetInfo(ABC):
    """
    Represents information about a CDP target.
    """

    @classmethod
    @abstractmethod
    def init(
        cls,
        id_: str,
        title: str,
        description: str,
        url: str,
        type_: str,
        web_socket_debugger_url: str
    ):
        """
        Initializer method for ITargetInfo subclasses
        """
        pass

    @abstractmethod
    def get_id(self) -> str:
        """
        Returns the id of the target.
        """
        pass

    @abstractmethod
    def get_title(self) -> str:
        """
        Returns the title of the target.
        """
        pass

    @abstractmethod
    def get_description(self) -> str:
        """
        Returns the description of the target.
        """
        pass

    @abstractmethod
    def get_url(self) -> str:
        """
        Returns the url of the target.
        """
        pass

    @abstractmethod
    def get_type(self) -> str:
        """
        Returns the type of the target.
        """
        pass

    @abstractmethod
    def get_web_socket_debugger_url(self) -> str:
        """
        Returns the web socket debugger url of the target.
        """
        pass


class ITarget(ABC):
    """
    Represents a CDP target.
    """

    @classmethod
    @abstractmethod
    def init(
        cls,
        chrome: 'IChrome',
        info: 'ITargetInfo'
    ):
        """
        Initializer method for ITarget subclasses
        """
        pass

    @abstractmethod
    def __aenter__(self):
        """
        Allows this object to be used as a context manager.
        """
        pass

    @abstractmethod
    def __aexit__(self, exc_type, exc_value, traceback):
        """
        Closes this target when used as a context manager.
        """
        pass

    @abstractmethod
    async def close_session(self, session: 'ISession'):
        """
        Closes the given session.
        """
        pass

    @abstractmethod
    def close_stream(self, stream: 'IEventStream') -> None:
        """
        Closes the given stream.
        """
        pass

    @abstractmethod
    async def connect(self) -> None:
        """
        Connects to the target.
        """
        pass

    @abstractmethod
    async def disconnect(self) -> None:
        """
        Disconnects from the target.
        """
        pass

    @abstractmethod
    def get_info(self) -> 'ITargetInfo':
        """
        Returns the associated ITargetInfo implementation
        """
        pass

    @abstractmethod
    def get_ws_url(self) -> str:
        """
        Returns the websocket url of the target.
        """
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        """
        Returns whether the target is connected.
        """
        pass

    @abstractmethod
    def open_stream(self, events) -> IEventStreamReader:
        """
        Opens a stream for the given events.
        """
        pass

    @abstractmethod
    async def open_session(self) -> 'ISession':
        """
        Opens a session for the target.
        """
        pass

    @abstractmethod
    async def send(self, method, params) -> Any:
        """
        Sends a message to the target.
        """
        pass

    @abstractmethod
    async def send_and_await_response(self, method, params) -> dict:
        """
        Sends a message to the target and awaits a response.
        """
        pass
