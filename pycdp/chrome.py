import os
from dataclasses import dataclass

import requests

from pycdp.target import Target, TargetInfo


@dataclass
class Chrome:
    host: str
    port: int

    @classmethod
    def start(cls, host: str = '127.0.0.1', port: int = 9222) -> 'Chrome':
        os.system(
            f'start chrome '
            f'--remote-debugging-port={port} '
            f'--remote-allow-origins=*'
        )

        self = cls(
            host=host,
            port=port
        )

        return self

    def close_tab(self, target_id: str):
        url = f'http://{self.host}:{self.port}/json/close/{target_id}'

        response = requests.get(url)
        response.raise_for_status()

    def get_targets(self) -> list[Target]:
        url = f'http://{self.host}:{self.port}/json/list'

        response = requests.get(url)
        response.raise_for_status()

        targets = []

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

    def open_tab(self, tab_url: str) -> Target:
        url = f'http://{self.host}:{self.port}/json/new?{tab_url}'
        params = {}

        if tab_url:
            params['url'] = tab_url

        response = requests.put(
            url=url,
            params=params
        )
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
