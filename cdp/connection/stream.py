import asyncio
from dataclasses import dataclass, field
from typing import Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from cdp.connection.connection import Connection

_T = TypeVar('_T')


@dataclass
class EventStream(Generic[_T]):
    events: list[dict] = field(
        init=False
    )
    next_future: asyncio.Future = field(
        init=False,
        repr=False
    )

    connection: 'Connection'
    event_names: list[str]

    def __post_init__(self):
        loop = asyncio.get_event_loop()

        self.events = []
        self.next_future = loop.create_future()

    async def publish(self, event: dict) -> None:
        loop = asyncio.get_event_loop()

        self.events.append(event)
        self.next_future.set_result(event)
        self.next_future = loop.create_future()

    async def wait(self) -> _T:
        loop = asyncio.get_event_loop()

        result = await self.next_future

        self.next_future = loop.create_future()

        return result

    async def close(self) -> None:
        for name in self.event_names:
            self.connection.event_streams[name].remove(
                self
            )
