import asyncio
import base64
from dataclasses import dataclass, field
from typing import Callable

from pycdp import Target, EventStreamReader
from pycdp.stream import Stream


@dataclass
class HTTPRequest:
    lifecycle_manager: 'HTTPLifecycleListener'

    id: str
    data: dict


@dataclass
class HTTPResponse:
    lifecycle_manager: 'HTTPLifecycleListener'

    id: str
    data: dict

    async def get_body(self) -> str:
        result = await self.lifecycle_manager.target.send_and_await_response(
            'Network.getResponseBody',
            {
                'requestId': self.id
            }
        )

        body = result['body']
        base_64_encoded = result['base64Encoded']

        if base_64_encoded:
            body = base64.b64decode(body)

        return body


@dataclass
class HTTPLifecycle:
    request: HTTPRequest
    response: HTTPResponse | None


@dataclass
class HTTPLifecycleStream(Stream[HTTPLifecycle]):
    ...


@dataclass
class HTTPLifecycleListener:
    event_stream_reader: EventStreamReader = field(
        init=False,
        repr=False
    )
    event_stream_listener: asyncio.Task | None = field(
        init=False,
        repr=False
    )
    in_flight_requests: dict[str, HTTPRequest] = field(
        init=False,
        repr=False
    )
    open_streams: list[tuple[Callable, HTTPLifecycleStream]] = field(
        init=False,
        repr=False
    )

    target: Target

    def __post_init__(self):
        self.event_stream_reader = self.target.open_stream([
            'Network.requestWillBeSent',
            'Network.responseReceived'
        ])
        self.event_stream_listener = None
        self.in_flight_requests = {}
        self.open_streams = []

    async def _listen_async(self):
        async for event in self.event_stream_reader.read():
            if event['method'] == 'Network.requestWillBeSent':
                request = HTTPRequest(
                    lifecycle_manager=self,
                    id=event['params']['requestId'],
                    data=event['params']['request']
                )

                self.in_flight_requests[request.id] = request

            elif event['method'] == 'Network.responseReceived':
                request = self.in_flight_requests.pop(
                    event['params']['requestId'],
                    None
                )

                if request is None:
                    continue

                response = HTTPResponse(
                    lifecycle_manager=self,
                    id=event['params']['requestId'],
                    data=event['params']['response']
                )

                lifecycle = HTTPLifecycle(
                    request=request,
                    response=response
                )

                for condition, stream in self.open_streams:
                    if condition(lifecycle):
                        stream.write(lifecycle)

    async def start(self):
        await self.target.connect()
        await self.target.start_session()
        await self.target.send_and_await_response(
            'Network.enable'
        )

        self.event_stream_listener = asyncio.create_task(
            self._listen_async()
        )

    async def open_stream(self, condition: Callable) -> HTTPLifecycleStream:
        stream = HTTPLifecycleStream.create()

        self.open_streams.append(
            (
                condition,
                stream
            )
        )

        return stream.create_reader()
