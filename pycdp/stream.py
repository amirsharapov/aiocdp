import asyncio
from dataclasses import dataclass, field
from typing import Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from pycdp.core.connection import Connection

_T = TypeVar('_T')


@dataclass
class EventStream(Generic[_T]):
    events: list[dict] = field(
        init=False
    )
    next: asyncio.Future = field(
        init=False,
        repr=False
    )
    lock: asyncio.Lock = field(
        init=False,
        repr=False
    )

    connection: 'Connection'
    event_names: list[str]

    def __post_init__(self):
        self.events = []
        self.next = asyncio.get_event_loop().create_future()
        self.lock = asyncio.Lock()

    def close(self):
        self.connection.close_stream(self)

    async def iterate_events(self):
        for event in self.events:
            yield event

        while True:
            yield await self.next

    def publish(self, event: dict) -> None:
        self.events.append(event)
        self.next.set_result(event)
        self.next = asyncio.get_event_loop().create_future()
