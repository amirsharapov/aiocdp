import os
from dataclasses import dataclass, field

import requests

from cdp.target import Target


@dataclass
class Chrome:
    host: str
    port: int

    _did_connect: bool = field(
        init=False
    )

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

        self.connect()

        return self

    @classmethod
    def get_targets(cls) -> list[Target]:
        pass

    def __post_init__(self):
        self._did_connect = False

    def connect(self, force: bool = False):
        if self._did_connect and not force:
            return

        response = requests.get('')
        response.raise_for_status()

        self._did_connect = True
