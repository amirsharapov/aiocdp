# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.types import (
    dom,
    page,
    runtime
)
from typing import (
    Any,
    Literal,
    TypedDict
)

AXNodeId = str

AXValueType = Literal[
    'boolean',
    'tristate',
    'booleanOrUndefined',
    'idref',
    'idrefList',
    'integer',
    'node',
    'nodeList',
    'number',
    'string',
    'computedString',
    'token',
    'tokenList',
    'domRelation',
    'role',
    'internalRole',
    'valueUndefined'
]

AXValueSourceType = Literal[
    'attribute',
    'implicit',
    'style',
    'contents',
    'placeholder',
    'relatedElement'
]

AXValueNativeSourceType = Literal[
    'description',
    'figcaption',
    'label',
    'labelfor',
    'labelwrapped',
    'legend',
    'rubyannotation',
    'tablecaption',
    'title',
    'other'
]

AXPropertyName = Literal[
    'busy',
    'disabled',
    'editable',
    'focusable',
    'focused',
    'hidden',
    'hiddenRoot',
    'invalid',
    'keyshortcuts',
    'settable',
    'roledescription',
    'live',
    'atomic',
    'relevant',
    'root',
    'autocomplete',
    'hasPopup',
    'level',
    'multiselectable',
    'orientation',
    'multiline',
    'readonly',
    'required',
    'valuemin',
    'valuemax',
    'valuetext',
    'checked',
    'expanded',
    'modal',
    'pressed',
    'selected',
    'activedescendant',
    'controls',
    'describedby',
    'details',
    'errormessage',
    'flowto',
    'labelledby',
    'owns'
]


class AXValueSource(TypedDict):
    type: 'AXValueSourceType'
    value: 'AXValue'
    attribute: str
    attribute_value: 'AXValue'
    superseded: bool
    native_source: 'AXValueNativeSourceType'
    native_source_value: 'AXValue'
    invalid: bool
    invalid_reason: str


class AXRelatedNode(TypedDict):
    backend_dom_node_id: 'dom.BackendNodeId'
    idref: str
    text: str


class AXProperty(TypedDict):
    name: 'AXPropertyName'
    value: 'AXValue'


class AXValue(TypedDict):
    type: 'AXValueType'
    value: Any
    related_nodes: list
    sources: list


class AXNode(TypedDict):
    node_id: 'AXNodeId'
    ignored: bool
    ignored_reasons: list
    role: 'AXValue'
    chrome_role: 'AXValue'
    name: 'AXValue'
    description: 'AXValue'
    value: 'AXValue'
    properties: list
    parent_id: 'AXNodeId'
    child_ids: list
    backend_dom_node_id: 'dom.BackendNodeId'
    frame_id: 'page.FrameId'