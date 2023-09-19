from dataclasses import dataclass
from typing import TypedDict, Literal, overload

from cdp.domains.domain import Domain


_accessibility_AXNodeId = str
_accessibility_AXValueType = Literal[
    'boolean',
    'tristate',
    'booleanOrUndefined',
]
_accessibility_AXValueSourceType = Literal[
    'attribute',
    'implicit',
]
_accessibility_AXValueNativeSourceType = Literal[
    'figcaption',
    'label',
    'labelfor',
    'labelwrapped',
    'legend',
    'tablecaption',
    'title',
    'other',
]


class _AXValueSource(TypedDict):
    type: '_accessibility_AXValueSourceType'
    value: str


class _accessibility__some_method__ReturnT(TypedDict):
    value: _AXValueSource
    valid: bool


class ParamsT(TypedDict):
    node_id: str


@dataclass
class Accessibility:
    @overload
    def some_method(
            self,
            params: ParamsT
    ) -> _accessibility__some_method__ReturnT:
        ...

    @overload
    def some_method(
            self,
            node_id: str
    ) -> _accessibility__some_method__ReturnT:
        ...


@dataclass
class Animation(Domain):
    pass


@dataclass
class ApplicationCache(Domain):
    pass


class Domains:
    accessibility: Accessibility = ...
    animation: Animation = ...
    application_cache: ApplicationCache = ...
