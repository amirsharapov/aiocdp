from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain
    from generator.parser.types.type import Type

registry = defaultdict(dict)


def add_type(type_: 'Type'):
    key = (type_.actual_domain.domain, type_.id)

    if key in registry['types']:
        raise ValueError(f'Type {key} already exists')

    registry['types'][key] = type_


def get_type(domain, id_) -> 'Type':
    key = (domain, id_)
    return registry['types'][key]


def add_domain(domain: 'Domain'):
    key = domain.domain

    if key in registry['domains']:
        raise ValueError(f'Domain {key} already exists')

    registry['domains'][key] = domain


def get_domain(domain: str) -> 'Domain':
    key = domain
    return registry['domains'][key]
