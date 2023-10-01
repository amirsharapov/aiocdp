from typing import TypeVar

T = TypeVar('T')


class _Undefined:
    def __repr__(self):
        return 'UNDEFINED'

    def __getattr__(self, item):
        return self

    def __bool__(self):
        return False


UNDEFINED = _Undefined()
MaybeUndefined = T | _Undefined


def is_undefined(value):
    return isinstance(value, _Undefined)


def is_defined(value):
    return not is_undefined(value)
