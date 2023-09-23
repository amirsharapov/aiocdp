import os
from dataclasses import dataclass

import requests

from cdp.target import Target


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

    @property
    def http_url(self):
        return f'http://{self.host}:{self.port}'

    def get_targets(self) -> list[Target]:
        url = self.http_url + '/json/list'

        response = requests.get(url)
        response.raise_for_status()

        targets = []

        for target in response.json():
            target_ = Target(
                chrome=self,
                id=target['id'],
                title=target['title'],
                description=target['description'],
                url=target['url'],
                type=target['type'],
                web_socket_debugger_url=target['webSocketDebuggerUrl']
            )

            targets.append(target_)

        return targets
