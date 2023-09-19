from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from cdp.domains.domain import Domain

if TYPE_CHECKING:
    from cdp.target import Target


accessibility_AXNodeId = str

accessibility_AXValueType = Literal[
    'boolean',
    'tristate',
    'booleanOrUndefined',
]

@dataclass
class Accessibility(Domain):
    pass


@dataclass
class Animation(Domain):
    pass


@dataclass
class ApplicationCache(Domain):
    pass


@dataclass
class Domains:
    ws_target: 'Target'

    accessibility: 'Accessibility' = ...
    animation: 'Animation' = ...
    application_cache: 'ApplicationCache' = ...

