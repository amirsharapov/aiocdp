from abc import ABC, abstractmethod

from aiocdp.core.interfaces.stream import IEventStream


class ITargetInfo(ABC):
    """
    Represents information about a CDP target.
    """

    @classmethod
    @abstractmethod
    def create(
        cls,
        id,
        title,
        description,
        url,
        type,
        web_socket_debugger_url
    ):
        """
        Initializer method for the ITargetInfo class
        """
        ...


class ITarget(ABC):
    """
    Represents a CDP target.
    """

    @classmethod
    @abstractmethod
    def create(
        cls,
        chrome,
        info: ITargetInfo
    ):
        """
        Initializer method for the ITarget class
        """
        ...

    @abstractmethod
    def close_stream(self, stream: IEventStream):
        """
        Closes the given stream.
        """
        ...

    def get_info(self):
        """
        Returns the associated ITargetInfo implementation
        """
        ...

    def open_stream(self, events):
        """
        Opens a stream for the given events.
        """
        pass

    def send(self, method, params):
        """
        Sends a message to the target.
        """
        pass

    def send_and_await_response(self, method, params):
        """
        Sends a message to the target and awaits a response.
        """
        pass
