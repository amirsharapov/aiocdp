from typing import TypeVar, Callable

_KT = TypeVar('_KT')

mappers = {}


def get_mapper(key: _KT):
    return mappers[key]


def add_mapper(mapper: Callable, key: _KT):
    mappers[key] = mapper
