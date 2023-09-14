import builtins
from typing import TypeVar

import inflection


direct_python_type_map = {
    'string': 'str',
    'integer': 'int',
    'number': 'float',
    'boolean': 'bool',
    'any': 'Any',
    'array': 'list'
}


def snake_case(value):
    return inflection.underscore(value)


def cdp_to_python_type(value):
    return direct_python_type_map.get(value, value)


def is_builtin(name: str):
    try:
        getattr(builtins, name)
        return True

    except AttributeError:
        return False


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


def coalesce_undefined(args):
    for arg in args:
        if is_defined(arg):
            return arg

    return UNDEFINED


def first_non_none(args):
    for arg in args:
        if arg is not None:
            return arg

    return None
