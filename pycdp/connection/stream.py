import asyncio
from dataclasses import dataclass, field
from typing import Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from pycdp.connection.connection import Connection

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

    async def close(self):
        await self.connection.close_stream(self)

    async def publish(self, event: dict) -> None:
        await self.lock.acquire()
        self.events.append(event)
        self.next.set_result(event)
        self.next = asyncio.get_event_loop().create_future()
        self.lock.release()
