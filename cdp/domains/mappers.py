from typing import Callable

_KT = tuple | str

mappers = {}


def add_mapper(mapper: Callable, key: _KT) -> None:
    mappers[key] = mapper


def get_mapper(key: _KT) -> Callable:
    return mappers[key]
