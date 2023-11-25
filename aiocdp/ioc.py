from typing import TypeVar

from aiocdp.core.interfaces.stream import IEventStreamReader, IEventStream
from aiocdp.core.interfaces.connection import IConnection
from aiocdp.core.interfaces.session import ISession
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
        implementation,
        interface
    ), f'Implementation {implementation} must be a subclass of interface {interface}'

    _lookup[interface] = implementation


def set_chrome_class(implementation: type[IChrome]):
    return set_class(
        IChrome,
        implementation
    )


def set_target_class(implementation: type[ITarget]):
    return set_class(
        ITarget,
        implementation
    )


def set_target_info_class(implementation: type[ITargetInfo]):
    return set_class(
        ITargetInfo,
        implementation
    )


def set_session_class(implementation: type[ISession]):
    return set_class(
        ISession,
        implementation
    )


def set_connection_class(implementation: type[IConnection]):
    return set_class(
        IConnection,
        implementation
    )


def set_event_stream_class(implementation: type[IEventStream]):
    return set_class(
        IEventStream,
        implementation
    )


def set_event_stream_reader_class(implementation: type[IEventStreamReader]):
    return set_class(
        IEventStreamReader,
        implementation
    )
