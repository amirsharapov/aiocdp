from dataclasses import dataclass

from cdp.target import Target


@dataclass
class Domains:
    target: 'Target'
