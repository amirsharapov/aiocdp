# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from typing import (
    Any,
    TypedDict
)

ScriptId = str

RemoteObjectId = str

UnserializableValue = str

ExecutionContextId = int

Timestamp = float

TimeDelta = float

UniqueDebuggerId = str


class RemoteObject(TypedDict):
    type: str
    subtype: str
    class_name: str
    value: Any
    unserializable_value: 'UnserializableValue'
    description: str
    object_id: 'RemoteObjectId'
    preview: 'ObjectPreview'
    custom_preview: 'CustomPreview'


class CustomPreview(TypedDict):
    header: str
    body_getter_id: 'RemoteObjectId'


class ObjectPreview(TypedDict):
    type: str
    overflow: bool
    properties: list
    subtype: str
    description: str
    entries: list


class PropertyPreview(TypedDict):
    name: str
    type: str
    value: str
    value_preview: 'ObjectPreview'
    subtype: str


class EntryPreview(TypedDict):
    value: 'ObjectPreview'
    key: 'ObjectPreview'


class PropertyDescriptor(TypedDict):
    name: str
    configurable: bool
    enumerable: bool
    value: 'RemoteObject'
    writable: bool
    get: 'RemoteObject'
    set: 'RemoteObject'
    was_thrown: bool
    is_own: bool
    symbol: 'RemoteObject'


class InternalPropertyDescriptor(TypedDict):
    name: str
    value: 'RemoteObject'


class PrivatePropertyDescriptor(TypedDict):
    name: str
    value: 'RemoteObject'


class CallArgument(TypedDict):
    value: Any
    unserializable_value: 'UnserializableValue'
    object_id: 'RemoteObjectId'


class ExecutionContextDescription(TypedDict):
    id: 'ExecutionContextId'
    origin: str
    name: str
    aux_data: dict


class ExceptionDetails(TypedDict):
    exception_id: int
    text: str
    line_number: int
    column_number: int
    script_id: 'ScriptId'
    url: str
    stack_trace: 'StackTrace'
    exception: 'RemoteObject'
    execution_context_id: 'ExecutionContextId'


class CallFrame(TypedDict):
    function_name: str
    script_id: 'ScriptId'
    url: str
    line_number: int
    column_number: int


class StackTrace(TypedDict):
    call_frames: list
    description: str
    parent: 'StackTrace'
    parent_id: 'StackTraceId'


class StackTraceId(TypedDict):
    id: str
    debugger_id: 'UniqueDebuggerId'