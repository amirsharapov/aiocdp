from abc import ABC, abstractmethod
from typing import Callable, Any

from src.aiocdp.core.interfaces.target import ITarget
from src.aiocdp.utils import UNDEFINED


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
    ):
        """
        Initializer method for the Chrome classes
        """
        pass

    @abstractmethod
    def start(self):
        """
        Starts the chrome instance
        """
        pass

    def close_tab(self, target_id: str):
        """
        Closes the tab with the given target id.
        """
        pass

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

    def get_targets(self) -> list[ITarget]:
        """
        Fetches a list of all the targets.
        """
        pass

    def iterate_targets(self):
        """
        Returns a generator that fetches and iterates over all the targets.
        """
        pass

    def open_tab(self, tab_url: str = None) -> ITarget:
        """
        Opens a new tab.
        """
        pass
