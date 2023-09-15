from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generator.types.type import Type

registry = defaultdict(dict)


def add_type(type_: 'Type'):
    key = (type_.inferred_domain, type_.id)

    if key in registry['types']:
        raise ValueError(f'Type {key} already exists')

    registry['types'][key] = type_


def get_type(domain, id_) -> 'Type':
    key = (domain, id_)
    return registry['types'][key]
