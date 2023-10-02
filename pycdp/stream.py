import asyncio
from dataclasses import dataclass
from typing import Generic, TypeVar, AsyncGenerator

_T = TypeVar('_T')


@dataclass
class Stream(Generic[_T]):
    items: list[_T]
    next: asyncio.Future

    @classmethod
    def create(cls):
        return cls(
            items=[],
            next=asyncio.get_event_loop().create_future(),
        )

    def get_reader(self):
        return StreamReader(self)

    async def read(self) -> AsyncGenerator[_T, None]:
        for item in self.items:
            yield item

        while True:
            yield await self.next

    def write(self, item: _T):
        self.items.append(item)
        self.next.set_result(item)
        self.next = asyncio.get_event_loop().create_future()


@dataclass
class StreamReader(Generic[_T]):
    stream: Stream[_T]

    async def read(self) -> AsyncGenerator[_T, None]:
        async for item in self.stream.read():
            yield item
