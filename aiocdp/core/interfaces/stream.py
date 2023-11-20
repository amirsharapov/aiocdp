from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar

from aiocdp.core.interfaces.connection import IConnection

_T = TypeVar('_T')


@dataclass
class IEventStream(ABC):
    """
    Represents an asynchronous stream of CDP events received from the connection.
    """

    @classmethod
    @abstractmethod
    def create(
        cls,
        connection: IConnection,
        events_to_listen: list[str]
    ) -> 'IEventStream':
        """
        Initializer method for the IEventStream class
        """
        ...

    @abstractmethod
    def close(self):
        """
        Unsubscribes this stream from receiving events from the connection.
        """
        ...

    @abstractmethod
    def get_connection(self) -> 'IConnection':
        """
        Returns the connection this event stream is associated with
        """
        ...

    @abstractmethod
    def get_events_to_listen(self):
        """
        Returns a list of events to listen to
        """
        ...

    @abstractmethod
    def get_reader(self) -> 'IEventStreamReader':
        """
        Returns a read only interface to this event stream
        """
        ...

    @abstractmethod
    def write(self, event):
        """
        Writes an event to the stream
        """
        ...


class IEventStreamReader(ABC):
    pass
