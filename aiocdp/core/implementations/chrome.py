import subprocess
from dataclasses import dataclass
from typing import Callable, Any

import requests

from aiocdp.core.implementations.target import Target, TargetInfo
from aiocdp.core.interfaces.chrome import IChrome
from aiocdp.core.interfaces.target import ITarget, ITargetInfo
from aiocdp.exceptions import NoTargetFoundMatchingCondition
from aiocdp.ioc import get_class
from aiocdp.utils import UNDEFINED


@dataclass
class Chrome(IChrome):
    """
    Represents a chrome instance.
    """

    """
    The host of the chrome instance.
    """
    host: str = '127.0.0.1'

    """
    The port of the chrome instance.
    """
    port: int = 9222

    """
    The command to start chrome. This can be coupled to the underlying OS.
    """
    start_chrome_command: str = 'start chrome'

    """
    The list of allowed origins that can connect to the chrome instance.
    """
    allow_origins: str = '*'

    @classmethod
    def init(
            cls,
            host: str = '127.0.0.1',
            port: int = 9222,
            allow_origins: str = '*',
            start_chrome_command: str = 'start chrome'
    ):
        """
        Initializer method for the Chrome classes
        """
        return cls(
            host=host,
            port=port,
            allow_origins=allow_origins,
            start_chrome_command=start_chrome_command
        )

    def _init_target(self, target: dict):
        """
        Initializes an instance of the target using the registered implementations.
        """
        target_info_cls = get_class(
            ITargetInfo,
            TargetInfo
        )

        target_cls = get_class(
            ITarget,
            Target
        )

        target_info = target_info_cls.init(
            id_=target['id'],
            title=target['title'],
            description=target['description'],
            url=target['url'],
            type_=target['type'],
            web_socket_debugger_url=target['webSocketDebuggerUrl']
        )

        target = target_cls.init(
            chrome=self,
            info=target_info
        )

        return target

    def start(self, extra_cli_args: list[str] = None, popen_kwargs: dict = None):
        """
        Starts chrome through the command line. Returns subprocess.Popen object.
        """
        commands = [
            self.start_chrome_command,
            f'--remote-debugging-port={self.port}',
            f'--remote-allow-origins={self.allow_origins}',
            *(extra_cli_args or [])
        ]

        command = ' '.join(commands)

        return subprocess.Popen(
            command,
            **(popen_kwargs or {})
        )

    def close_tab(self, target_id: str):
        """
        Closes the tab with the given target id.
        """
        url = f'http://{self.host}:{self.port}/json/close/{target_id}'

        response = requests.get(url)
        response.raise_for_status()

    def get_first_target(
            self,
            condition: Callable[[ITarget], bool] = None,
            default: Any = UNDEFINED
    ) -> ITarget:
        """
        Fetches and returns the first target.
        Raises an exception if no target is found and no default is supplied.
        """
        for target in self.iterate_targets():
            if not condition:
                return target

            if condition(target):
                return target

        if default is not UNDEFINED:
            return default

        raise NoTargetFoundMatchingCondition(
            condition
        )

    def get_host(self) -> str:
        """
        Returns the host of the chrome instance
        """
        return self.host

    def get_port(self) -> int:
        """
        Returns the port of the chrome instance
        """
        return self.port

    def get_targets(self) -> list[ITarget]:
        """
        Fetches a list of all the targets.
        """
        return list(
            self.iterate_targets()
        )

    def iterate_targets(self):
        """
        Returns a generator that fetches and iterates over all the targets.
        """
        url = f'http://{self.host}:{self.port}/json/list'

        response = requests.get(url)
        response.raise_for_status()

        for target in response.json():
            yield self._init_target(target)

    def open_tab(self, url: str = None) -> ITarget:
        """
        Opens a new tab.
        """
        url_ = f'http://{self.host}:{self.port}/json/new'

        if url:
            url_ += f'?{url}'

        response = requests.put(url_)
        response.raise_for_status()

        target = response.json()

        return self._init_target(target)
