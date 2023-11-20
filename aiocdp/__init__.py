from .core.implementations import (
    Chrome,
    Target,
    TargetSession,
    Connection,
    EventStream,
    EventStreamReader
)
from .core.interfaces import (
    IChrome,
    ITarget,
    ITargetSession,
    IConnection,
    IEventStream,
    IEventStreamReader
)
from .exceptions import (
    AIOCDPException,
    InvalidRPCResponse,
    NoTargetFound,
    NoTargetFoundMatchingCondition
)
from .ioc import set_class


def set_default_factories():
    defaults = {
        IChrome: Chrome,
        ITarget: Target,
        ITargetSession: TargetSession,
        IConnection: Connection,
        IEventStream: EventStream,
        IEventStreamReader: EventStreamReader
    }

    for interface, implementation in defaults.items():
        set_class(
            interface,
            implementation
        )
