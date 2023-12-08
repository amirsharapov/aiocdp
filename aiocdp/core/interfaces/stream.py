from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, TYPE_CHECKING, AsyncIterator

if TYPE_CHECKING:
    from aiocdp.core.interfaces.connection import IConnection

_T = TypeVar('_T')


@dataclass
class IEventStream(ABC):
    """
    Represents an asynchronous stream of CDP events received from the connection.
    """

    @classmethod
    @abstractmethod
    def init(
        cls,
        connection: 'IConnection',
        events_to_listen: list[str]
    ) -> 'IEventStream':
        """
        Initializer method for the IEventStream class.
        """
        pass

    @abstractmethod
    def __enter__(self):
        """
        Allows this object to be used as a context manager.
        """
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes this stream when used as a context manager.
        """
        pass

    @abstractmethod
    def close(self):
        """
        Unsubscribes this stream from receiving events from the connection.
        """
        pass

    @abstractmethod
    def get_connection(self) -> 'IConnection':
        """
        Returns the connection this event stream is associated with.
        """
        pass

    @abstractmethod
    def get_events_to_listen(self) -> list[str]:
        """
        Returns a list of events to listen to.
        """
        pass

    @abstractmethod
    def get_reader(self) -> 'IEventStreamReader':
        """
        Returns a read only interface associated with this event stream.
        """
        pass

    @abstractmethod
    def is_closed(self) -> bool:
        """
        Returns whether the stream is closed.
        """
        pass

    @abstractmethod
    def iterate(self) -> AsyncIterator[_T]:
        """
        Returns an async iterator for all recorded events and new events as they are received.
        """
        pass

    @abstractmethod
    def write(self, event: '_T'):
        """
        Writes an event to the stream.
        """
        pass


class IEventStreamReader(ABC):
    """
    Read only interface to an event stream.
    """

    @abstractmethod
    def __enter__(self):
        """
        Allows this object to be used as a context manager.
        """
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes this stream when used as a context manager.
        """
        pass

    @abstractmethod
    def close(self):
        """
        Closes this stream.
        """
        pass

    @abstractmethod
    def get_connection(self) -> 'IConnection':
        """
        Returns the connection this event stream is associated with.
        """
        pass

    @abstractmethod
    def get_events_to_listen(self):
        """
        Returns a list of events to listen to.
        """
        pass

    @abstractmethod
    def is_closed(self) -> bool:
        """
        Returns whether the stream is closed.
        """
        pass

    @abstractmethod
    def iterate(self) -> AsyncIterator[_T]:
        """
        Returns an async iterator for all recorded events and new events as they are received.
        """
        pass
