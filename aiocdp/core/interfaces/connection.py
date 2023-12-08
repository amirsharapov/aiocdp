from abc import ABC, abstractmethod
from typing import Coroutine, Any

from aiocdp.core.interfaces.stream import IEventStream, IEventStreamReader


class IConnection(ABC):
    """
    Represents a connection to a CDP target.
    """

    @classmethod
    @abstractmethod
    def init(cls, ws_url: str) -> 'IConnection':
        """
        Initializer method for the IConnection class
        """
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        """
        Returns whether the connection is closed.
        """
        pass

    def close_stream(self, stream: 'IEventStream'):
        """
        Unsubscribes the given event stream from receiving events from the connection.
        """
        pass

    def connect(self) -> Coroutine[Any, None, None]:
        """
        Connects to the websocket and starts the listener task. Returns a future that resolves when the connection is
        established.
        """
        pass

    def disconnect(self) -> Coroutine[Any, None, None]:
        """
        Disconnects from the websocket and cancels the listener task. Returns a future that resolves when the
        connection is closed.
        """
        pass

    def is_stream_closed(self, stream: 'IEventStream') -> bool:
        """
        Checks if the given stream is closed.
        """
        pass

    def open_stream(self, events: list[str]) -> 'IEventStreamReader':
        """
        Opens a new event stream for the given events and returns a reader for it.
        """
        pass

    def send(self, method: str, params: dict) -> Coroutine[Any, None, None]:
        """
        Sends a message to the websocket. Returns a future that resolves when the message is sent.
        """
        pass
