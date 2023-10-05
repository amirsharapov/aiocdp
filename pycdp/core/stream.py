import asyncio
from dataclasses import dataclass
from typing import TypeVar, AsyncGenerator, TYPE_CHECKING

if TYPE_CHECKING:
    from pycdp import Connection

_T = TypeVar('_T')


@dataclass
class EventStream:
    """
    Represents an asynchronous stream of CDP events received from the connection.
    """
    connection: 'Connection'
    events: list[_T]
    events_to_listen: list[str]
    reader: 'EventStreamReader | None'
    next: asyncio.Future

    @classmethod
    def create(cls, connection: 'Connection', events_to_listen: list[str]):
        """
        Creates a new instance of the event stream.
        """
        loop = asyncio.get_event_loop()

        return cls(
            connection=connection,
            events=[],
            events_to_listen=events_to_listen,
            reader=None,
            next=loop.create_future(),
        )

    def close(self):
        """
        Unsubscribes this stream from receiving events from the connection.
        """
        self.connection.close_stream(self)

    def get_reader(self):
        """
        Creates the reader for this stream.

        NOTES:
            - The reader returned will be the same instance for the lifetime of this stream.
        """

        if self.reader is None:
            self.reader = EventStreamReader(self)

        return self.reader

    async def iterate(self) -> AsyncGenerator[_T, None]:
        """
        Iterates over all the events in this stream and asynchronously yields new events as they are received.

        NOTES:
            - Should not be used by public API. Use `EventStreamReader.iterate` instead.
        """
        for item in self.events:
            yield item

        while True:
            yield await self.next

    def write(self, item: _T):
        """
        Writes an item to the stream. Responsible for resolving futures.
        """
        loop = asyncio.get_event_loop()

        self.events.append(item)
        self.next.set_result(item)
        self.next = loop.create_future()


@dataclass
class EventStreamReader:
    """
    Object that has read only access to an event stream.
    """
    stream: EventStream

    @property
    def events_to_listen(self) -> list[str]:
        """
        Public readonly access to the CDP events to listen for. Provided by the stream.
        """
        return self.stream.events_to_listen

    @property
    def connection(self):
        """
        Public readonly access to the `Connection` instance. Provided by the stream.
        """
        return self.stream.connection

    def close(self):
        """
        Closes this stream.
        """
        self.stream.close()

    async def iterate(self) -> AsyncGenerator[_T, None]:
        """
        Iterates over the events asynchronously in this stream.
        """
        async for item in self.stream.iterate():
            yield item
