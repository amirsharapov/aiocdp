import os
from dataclasses import dataclass
from typing import Callable, Any

import requests

from pycdp.core.target import Target, TargetInfo
from pycdp.exceptions import NoTargetFoundMatchingCondition
from pycdp.utils import UNDEFINED


@dataclass
class Chrome:
    """
    Represents a Chrome instance on a given host and port.
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
    The origins allowed to remotely connect to the chrome instance.
    """
    allow_origins: str = '*'

    def start(self, cli_args: list[str] = None):
        """
        Starts chrome through the command line.
        """
        commands = [
            f'start chrome',
            f'--remote-debugging-port={self.port}',
            f'--remote-allow-origins={self.allow_origins}'
        ]

        commands.extend(cli_args or [])
        command = ' '.join(commands)

        os.system(command)

        return self

    def close_tab(self, target_id: str):
        """
        Closes the tab with the given target id.
        """
        url = f'http://{self.host}:{self.port}/json/close/{target_id}'

        response = requests.get(url)
        response.raise_for_status()

    def get_first_target(
            self,
            condition: Callable[[Target], bool] = None,
            default: Any = UNDEFINED
    ) -> Target:
        """
        Fetches and returns the first target. Raises an exception if no target is found and no default is supplied.

        Notes:
            Supply a condition to filter against each target.
            Supply a default to return a default if no target is found.
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

    def get_targets(self) -> list[Target]:
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
            yield Target(
                chrome=self,
                info=TargetInfo(
                    id=target['id'],
                    title=target['title'],
                    description=target['description'],
                    url=target['url'],
                    type=target['type'],
                    web_socket_debugger_url=target['webSocketDebuggerUrl']
                )
            )

    def open_tab(self, tab_url: str = None) -> Target:
        """
        Opens a new tab.
        """
        url = f'http://{self.host}:{self.port}/json/new'

        if tab_url:
            url += f'?{tab_url}'

        response = requests.put(url)
        response.raise_for_status()

        return Target(
            chrome=self,
            info=TargetInfo(
                id=response.json()['id'],
                title=response.json()['title'],
                description=response.json()['description'],
                url=response.json()['url'],
                type=response.json()['type'],
                web_socket_debugger_url=response.json()['webSocketDebuggerUrl']
            )
        )
