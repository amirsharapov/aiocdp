from typing import TypeVar

T = TypeVar('T')

class _Undefined:
    pass


UNDEFINED = _Undefined()
Undefinable = T | _Undefined


def is_undefined(value):
    return isinstance(value, _Undefined)


def is_defined(value):
    return not is_undefined(value)
