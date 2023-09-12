from abc import ABC
from dataclasses import dataclass


@dataclass
class Domain:
    def send_command(
            self,
            method: str,
            params: dict
    ):
        pass


@dataclass
class ComplexType(ABC):
    pass
