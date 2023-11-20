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
