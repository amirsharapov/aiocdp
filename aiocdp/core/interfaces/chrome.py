from abc import ABC, abstractmethod
from typing import Callable, Any, Generator, Iterator

from aiocdp.core.interfaces.target import ITarget
from aiocdp.utils import UNDEFINED


class IChrome(ABC):
    """
    Represents an instance of a Chrome Browser
    """

    @classmethod
    @abstractmethod
    def init(
        cls,
        host: str,
        port: int,
    ) -> 'IChrome':
        """
        Initializer method for the Chrome classes
        """
        pass

    @abstractmethod
    def start(self) -> None:
        """
        Starts the chrome instance
        """
        pass

    @abstractmethod
    def close_tab(self, target_id: str):
        """
        Closes the tab with the given target id.
        """
        pass

    @abstractmethod
    def get_first_target(
            self,
            condition: Callable[[ITarget], bool] = None,
            default: Any = UNDEFINED
    ) -> ITarget:
        """
        Fetches and returns the first target.
        Raises an exception if no target is found and no default is supplied.
        """
        pass

    @abstractmethod
    def get_host(self) -> str:
        """
        Returns the host of the chrome instance
        """
        pass

    @abstractmethod
    def get_port(self) -> int:
        """
        Returns the port of the chrome instance
        """
        pass

    @abstractmethod
    def get_targets(self) -> list[ITarget]:
        """
        Fetches a list of all the targets.
        """
        pass

    @abstractmethod
    def iterate_targets(self) -> Iterator[ITarget]:
        """
        Returns a generator that fetches and iterates over all the targets.
        """
        pass

    @abstractmethod
    def open_tab(self, url: str = None) -> ITarget:
        """
        Opens a new tab.
        """
        pass
