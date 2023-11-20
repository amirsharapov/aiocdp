from aiocdp.core.interfaces.chrome import IChrome
from aiocdp.core.interfaces.target import ITarget

_lookup = {}


def get_factory(interface):
    return _lookup[interface]


def set_factory(interface: type, implementation: type):
    assert issubclass(interface, implementation)
    _lookup[interface] = implementation


def set_chrome_factory(implementation: type[IChrome]):
    set_factory(
        IChrome,
        implementation
    )
