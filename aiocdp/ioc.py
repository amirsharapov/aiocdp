from typing import TypeVar

from aiocdp.core.interfaces.chrome import IChrome
from aiocdp.core.interfaces.target import ITarget, ITargetInfo
from aiocdp.utils import UNDEFINED

_T = TypeVar('_T')
_lookup = {}


def get_class(interface: type[_T], default: type = UNDEFINED) -> type[_T]:
    if interface in _lookup:
        return _lookup[interface]

    if default is UNDEFINED:
        raise RuntimeError(
            f'No implementation registered for interface: {interface}'
        )

    assert issubclass(
        default,
        interface
    )

    return default


def set_class(interface: type, implementation: type):
    assert issubclass(
        interface,
        implementation
    )

    _lookup[interface] = implementation


def set_chrome_class(implementation: type[IChrome]):
    set_class(
        IChrome,
        implementation
    )


def set_target_class(implementation: type[ITarget]):
    set_class(
        ITarget,
        implementation
    )


def set_target_info_class(implementation: type[ITargetInfo]):
    set_class(
        ITargetInfo,
        implementation
    )
