import asyncio
from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Generic, TypeVar, AsyncGenerator, TYPE_CHECKING

if TYPE_CHECKING:
    from pycdp import Connection

_T = TypeVar('_T')


@dataclass
class Stream(Generic[_T], ABC):
    items: list[_T]
    next: asyncio.Future

    @classmethod
    def create(cls):
        return cls(
            items=[],
            next=asyncio.get_event_loop().create_future(),
        )

    @abstractmethod
    def create_reader(self):
        ...

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
class StreamReader(Generic[_T], ABC):
    stream: Stream[_T]

    async def read(self) -> AsyncGenerator[_T, None]:
        async for item in self.stream.read():
            yield item


@dataclass
class EventStream(Stream[dict]):
    connection: 'Connection'
    events: list[str]

    # noinspection PyMethodOverriding
    @classmethod
    def create(cls, connection: 'Connection', events: list[str]):
        return cls(
            items=[],
            next=asyncio.get_event_loop().create_future(),
            connection=connection,
            events=[]
        )

    def create_reader(self):
        return StreamReader(self)


@dataclass
class EventStreamReader(StreamReader):
    stream: EventStream

    @property
    def events(self):
        return self.stream.events

    @property
    def connection(self):
        return self.stream.connection

    def close(self):
        self.connection.close_stream(self)
