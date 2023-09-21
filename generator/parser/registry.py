from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain
    from generator.parser.types.type import Type

registry = defaultdict(dict)
is_registry_loaded = False

_types = []
_domains = []


def _load_registry():
    for type_ in _types:
        registry['types'][(type_.domain.domain, type_.id)] = type_

    for domain in _domains:
        registry['domains'][domain.domain] = domain

    global is_registry_loaded
    is_registry_loaded = True


def add_type(type_: 'Type'):
    _types.append(type_)


def get_type(domain, id_) -> 'Type':
    if not is_registry_loaded:
        _load_registry()

    key = (domain, id_)
    return registry['types'][key]


def add_domain(domain: 'Domain'):
    _domains.append(domain)


def get_domain(domain: str) -> 'Domain':
    if not is_registry_loaded:
        _load_registry()

    key = domain
    return registry['domains'][key]
