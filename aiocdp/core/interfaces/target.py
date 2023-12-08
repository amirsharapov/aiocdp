from abc import ABC, abstractmethod
from asyncio import Future
from typing import TYPE_CHECKING, Any, Coroutine

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
    def close_session(self, session: 'ISession') -> Coroutine[None, None, Any]:
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
    def connect(self) -> Coroutine[None, None, Any]:
        """
        Connects to the target.
        """
        pass

    @abstractmethod
    def disconnect(self) -> Coroutine[None, None, Any]:
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
    def open_session(self) -> Coroutine[None, None, 'ISession']:
        """
        Opens a session for the target.
        """
        pass

    @abstractmethod
    def send(self, method, params) -> Coroutine[None, None, Any]:
        """
        Sends a message to the target.
        """
        pass

    @abstractmethod
    def send_and_await_response(self, method, params) -> Coroutine[None, None, Any]:
        """
        Sends a message to the target and awaits a response.
        """
        pass
