import os
from dataclasses import dataclass
from typing import Callable

import requests

from pycdp.core.target import Target, TargetInfo
from pycdp.exceptions import NoTargetFoundMatchingCondition


@dataclass
class Chrome:
    """
    Represents a Chrome instance.

    NOTES:
        - This class can be used as a singleton to manage a single instance of Chrome.
    """
    host: str
    port: int

    @classmethod
    def create(cls, host: str = '127.0.0.1', port: int = 9222):
        """
        Method to create a new instance of Chrome with default host and port.
        """
        return cls(
            host=host,
            port=port
        )

    def start(self, cli_args: list[str] = None):
        """
        Starts chrome through the command line.
        """
        commands = [
            f'start chrome',
            f'--remote-debugging-port={self.port}',
            f'--remote-allow-origins=*'
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

    def get_first_target_matching_condition(self, condition: Callable[[Target], bool]) -> Target:
        """
        Fetches and iterates over all the targets and returns the first that matches the given condition.
        Raises an exception if no target is found matching the condition.
        """
        for target in self.iterate_targets():
            if condition(target):
                return target

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
