from abc import ABC, abstractmethod

from aiocdp.core.interfaces.chrome import IChrome
from aiocdp.core.interfaces.stream import IEventStream


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
    def close_stream(self, stream: 'IEventStream'):
        """
        Closes the given stream.
        """
        pass

    @abstractmethod
    def get_info(self):
        """
        Returns the associated ITargetInfo implementation
        """
        pass

    @abstractmethod
    def open_stream(self, events):
        """
        Opens a stream for the given events.
        """
        pass

    @abstractmethod
    def send(self, method, params):
        """
        Sends a message to the target.
        """
        pass

    @abstractmethod
    def send_and_await_response(self, method, params):
        """
        Sends a message to the target and awaits a response.
        """
        pass
