import os
from dataclasses import dataclass

import requests

from cdp.target import Target


@dataclass
class Chrome:
    host: str
    port: int

    @classmethod
    def start(cls, host: str = '127.0.0.1', port: int = 9222):
        os.system(
            f'start chrome '
            f'--remote-debugging-port={port}'
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

        return [Target() for _ in response.json()]
