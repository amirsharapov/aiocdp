from typing import Any

from generator.utils import MaybeUndefined, is_defined, UNDEFINED


class DataType(str):
    @classmethod
    def from_maybe_undefined(cls, raw: MaybeUndefined[str]) -> MaybeUndefined['DataType']:
        if not is_defined(raw):
            return UNDEFINED
        return cls(raw)

    @property
    def python_type(self) -> type:
        return {
            'string': str,
            'integer': int,
            'number': float,
            'boolean': bool,
            'array': list,
            'object': dict,
            'any': Any,
        }[self]
