import os
from dataclasses import dataclass

import requests

from pycdp.core.target import Target, TargetInfo


@dataclass
class Chrome:
    host: str
    port: int

    @classmethod
    def create(cls, host: str = '127.0.0.1', port: int = 9222):
        return cls(
            host=host,
            port=port
        )

    def start(self, cli_args: list[str] = None):
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
        url = f'http://{self.host}:{self.port}/json/close/{target_id}'

        response = requests.get(url)
        response.raise_for_status()

    def get_targets(self) -> list[Target]:
        url = f'http://{self.host}:{self.port}/json/list'

        targets = []

        response = requests.get(url)
        response.raise_for_status()

        for target in response.json():
            target_ = Target(
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

            targets.append(target_)

        return targets

    def open_tab(self, tab_url: str = None) -> Target:
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
