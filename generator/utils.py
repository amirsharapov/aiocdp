from typing import TypeVar, Iterable

import inflection

T = TypeVar('T')

class _Undefined:
    def __repr__(self):
        return 'UNDEFINED'

    def __getattr__(self, item):
        return self


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


def snake_case(value):
    return inflection.underscore(value)


def concat_lines(args: Iterable[str]) -> str:
    return '\n'.join(args)


def split_ref(type_: str) -> tuple[str, str] | tuple[None, str]:
    split = type_.split('.')

    if len(split) == 1:
        return None, split[0]

    return split[0], split[1]


def indent(s: str, n: int):
    return ' ' * n + s if s else ''


def indent_lines(s: str, n: int):
    lines = s.split('\n')
    lines = [indent(line, n) for line in lines]
    return '\n'.join(lines)


def create_vertical_comma_separated_list(
    items: list[str],
    indent_size: int = 0,
    trailing_comma: bool = False
) -> str:
    if not items:
        return ''

    result = ',\n'.join(items)

    if trailing_comma:
        result += ','

    return indent_lines(
        result,
        indent_size
    )
