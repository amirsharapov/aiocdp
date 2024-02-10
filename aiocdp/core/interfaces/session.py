from abc import ABC, abstractmethod
from typing import Any, TYPE_CHECKING

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
    async def __aenter__(self):
        """
        Allows this object to be used as an async context manager.
        """
        pass

    @abstractmethod
    async def __aexit__(self, exc_type, exc_value, traceback):
        """
        Closes this session when used as an async context manager.
        """
        pass

    @abstractmethod
    async def close(self) -> None:
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
    async def open(self):
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
    async def send(self, method: str, params: dict = None) -> Any:
        """
        Sends a message to the target. Calls `self.target.send`.
        """
        pass

    @abstractmethod
    async def send_and_await_response(self, method: str, params: dict = None) -> dict:
        """
        Sends a message to the target and awaits a response. Calls `self.target.send_and_await_response`
        """
        pass
