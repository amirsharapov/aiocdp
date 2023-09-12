from typing import TypeVar, Iterable

import inflection

T = TypeVar('T')

class _Undefined:
    def __repr__(self):
        return 'UNDEFINED'


UNDEFINED = _Undefined()
MaybeUndefined = T | _Undefined


def is_undefined(value):
    return isinstance(value, _Undefined)


def is_defined(value):
    return not is_undefined(value)


def snake_case(value):
    return inflection.underscore(value)


def concat_lines(args: Iterable[str]) -> str:
    return '\n'.join(args)


def split_ref(type_: str) -> tuple[str, str] | tuple[None, str]:
    split = type_.split('.')

    if len(split) == 1:
        return None, split[0]

    return split[0], split[1]

