import asyncio
import base64
from dataclasses import dataclass, field
from typing import Callable

from pycdp import Target, AsyncioStream


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
class HTTPLifecycleStream(AsyncioStream[HTTPLifecycle]):
    ...


@dataclass
class HTTPLifecycleListener:
    in_flight_requests: dict[str, HTTPRequest] = field(
        init=False,
        repr=False
    )
    open_streams: list[tuple[Callable, AsyncioStream]] = field(
        init=False,
        repr=False
    )
    request_will_be_sent_stream: AsyncioStream = field(
        init=False,
        repr=False
    )
    request_will_be_sent_async_loop: asyncio.Task = field(
        init=False,
        repr=False
    )
    response_received_stream: AsyncioStream = field(
        init=False,
        repr=False
    )
    response_received_async_loop: asyncio.Task = field(
        init=False,
        repr=False
    )

    target: Target

    def __post_init__(self):
        self.in_flight_requests = {}
        self.open_streams = []

        self.request_will_be_sent_stream = self.target.open_stream([
            'Network.requestWillBeSent'
        ])
        self.response_received_stream = self.target.open_stream([
            'Network.responseReceived'
        ])

    async def _listen_for_requests_async(self):
        async for event in self.request_will_be_sent_stream.iterate_events():
            request = HTTPRequest(
                lifecycle_manager=self,
                id=event['params']['requestId'],
                data=event['params']['request']
            )

            self.in_flight_requests[request.id] = request

    async def _listen_for_responses_async(self):
        async for event in self.response_received_stream.iterate_events():
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
                    stream.publish(lifecycle)

    async def start(self):
        await self.target.connect()
        await self.target.start_session()

        await self.target.send_and_await_response(
            'Network.enable'
        )

        self.response_received_async_loop = asyncio.create_task(
            self._listen_for_responses_async()
        )

        self.request_will_be_sent_async_loop = asyncio.create_task(
            self._listen_for_requests_async()
        )

    async def open_stream(self, condition: Callable) -> HTTPLifecycleStream:
        stream = HTTPLifecycleStream()

        self.open_streams.append(
            (
                condition,
                stream
            )
        )

        return stream
