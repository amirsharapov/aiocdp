import asyncio
from dataclasses import dataclass, field
from typing import Generic, TypeVar, AsyncGenerator

_T = TypeVar('_T')


@dataclass
class AsyncioStream(Generic[_T]):
    events: list[_T] = field(
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

    def __post_init__(self):
        self.events = []
        self.next = asyncio.get_event_loop().create_future()
        self.lock = asyncio.Lock()

    async def iterate_events(self) -> AsyncGenerator[_T, None]:
        for event in self.events:
            yield event

        while True:
            yield await self.next

    def publish(self, event: _T) -> None:
        self.events.append(event)
        self.next.set_result(event)
        self.next = asyncio.get_event_loop().create_future()
