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
    def get_reader(self) -> 'IEventStreamReader':
        """
        Returns a read only interface to this event stream
        """
        ...


class IEventStreamReader(ABC):
    pass
