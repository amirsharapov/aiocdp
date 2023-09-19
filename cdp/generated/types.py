from typing import TypedDict, Literal

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
