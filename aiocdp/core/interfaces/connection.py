from abc import ABC, abstractmethod

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

    @property
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

    async def connect(self):
        """
        Connects to the websocket and starts the listener task.
        """
        pass

    async def disconnect(self):
        """
        Disconnects from the websocket and cancels the listener task.
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

    async def send(self, method: str, params: dict):
        """
        Sends a message to the websocket.
        """
        pass
