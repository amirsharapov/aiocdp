from dataclasses import dataclass

from cdp.target import Target


@dataclass
class Chrome:
    host: str
    port: int

    @classmethod
    def connect(cls, host: str = '127.0.0.1', port: int = 9222):
        return cls(
            host,
            port
        )

    @classmethod
    def get_targets(cls) -> list[Target]:
        pass
