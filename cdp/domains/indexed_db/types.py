from dataclasses import (
    dataclass
)
from typing import (
    Literal
)


@dataclass
class DataEntry:
    key: RemoteObject
    primaryKey: RemoteObject
    value: RemoteObject


@dataclass
class DatabaseWithObjectStores:
    name: str
    version: float
    objectStores: list


@dataclass
class Key:
    type: str
    number: float
    string: str
    date: float
    array: list


@dataclass
class KeyPath:
    type: str
    string: str
    array: list


@dataclass
class KeyRange:
    lower: Key
    upper: Key
    lowerOpen: bool
    upperOpen: bool


@dataclass
class ObjectStore:
    name: str
    keyPath: KeyPath
    autoIncrement: bool
    indexes: list


@dataclass
class ObjectStoreIndex:
    name: str
    keyPath: KeyPath
    unique: bool
    multiEntry: bool
