from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class CallArgument:
    value: Any
    unserializableValue: UnserializableValue
    objectId: RemoteObjectId


@dataclass
class CallFrame:
    functionName: str
    scriptId: ScriptId
    url: str
    lineNumber: int
    columnNumber: int


@dataclass
class CustomPreview:
    header: str
    bodyGetterId: RemoteObjectId


@dataclass
class EntryPreview:
    key: ObjectPreview
    value: ObjectPreview


@dataclass
class ExceptionDetails:
    exceptionId: int
    text: str
    lineNumber: int
    columnNumber: int
    scriptId: ScriptId
    url: str
    stackTrace: StackTrace
    exception: RemoteObject
    executionContextId: ExecutionContextId


@dataclass
class ExecutionContextDescription:
    id: ExecutionContextId
    origin: str
    name: str
    auxData: object


@dataclass
class InternalPropertyDescriptor:
    name: str
    value: RemoteObject


@dataclass
class ObjectPreview:
    type: str
    subtype: str
    description: str
    overflow: bool
    properties: list
    entries: list


@dataclass
class PrivatePropertyDescriptor:
    name: str
    value: RemoteObject


@dataclass
class PropertyDescriptor:
    name: str
    value: RemoteObject
    writable: bool
    get: RemoteObject
    set: RemoteObject
    configurable: bool
    enumerable: bool
    wasThrown: bool
    isOwn: bool
    symbol: RemoteObject


@dataclass
class PropertyPreview:
    name: str
    type: str
    value: str
    valuePreview: ObjectPreview
    subtype: str


@dataclass
class RemoteObject:
    type: str
    subtype: str
    className: str
    value: Any
    unserializableValue: UnserializableValue
    description: str
    objectId: RemoteObjectId
    preview: ObjectPreview
    customPreview: CustomPreview


@dataclass
class StackTrace:
    description: str
    callFrames: list
    parent: StackTrace
    parentId: StackTraceId


@dataclass
class StackTraceId:
    id: str
    debuggerId: UniqueDebuggerId
