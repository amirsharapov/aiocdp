from abc import ABC, abstractmethod
from typing import Any, Coroutine, TYPE_CHECKING

from aiocdp.core.interfaces.stream import IEventStream, IEventStreamReader

if TYPE_CHECKING:
    from aiocdp.core.interfaces.target import ITarget


class ISession(ABC):
    """
    Represents a session with a target.
    """

    @classmethod
    @abstractmethod
    def init(
        cls,
        target: 'ITarget'
    ):
        """
        Initializer method for the ISession class
        """
        pass

    @abstractmethod
    def __aenter__(self):
        """
        Allows this object to be used as an async context manager.
        """
        pass

    @abstractmethod
    def __aexit__(self, exc_type, exc_value, traceback):
        """
        Closes this session when used as an async context manager.
        """
        pass

    @abstractmethod
    def close(self) -> Coroutine[None, None, Any]:
        """
        Closes the session by detaching from the target.
        """
        pass

    @abstractmethod
    def close_stream(self, stream: IEventStream):
        """
        Closes the stream. Calls `Target.close_stream`.
        """
        pass

    @abstractmethod
    def open(self) -> Coroutine[None, None, Any]:
        """
        Opens the session by attaching to the target.
        """
        pass

    @abstractmethod
    def open_stream(self, events: list[str]) -> IEventStreamReader:
        """
        Opens a stream. Calls `self.target.open_stream` method on the target.
        """
        pass

    @abstractmethod
    def send(self, method: str, params: dict = None) -> Coroutine[None, None, Any]:
        """
        Sends a message to the target. Calls `self.target.send`.
        """
        pass

    @abstractmethod
    def send_and_await_response(self, method: str, params: dict = None) -> Coroutine[None, None, Any]:
        """
        Sends a message to the target and awaits a response. Calls `self.target.send_and_await_response`
        """
        pass
