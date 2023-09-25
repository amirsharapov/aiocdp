import asyncio
import json
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

import websockets.client as websockets

from pycdp.connection.stream import EventStream

_id = 0


def _next_rpc_id():
    global _id
    _id += 1
    return _id


def _validate_response(response: dict):
    if 'error' in response and response['error']:
        error = response['error']
        raise Exception(
            'Received the following error: '
            f'Err Code: {error["code"]}, '
            f'Err Message: {error["message"]}, '
            f'Raw Message: {response}'
        )


@dataclass
class Connection:
    event_streams: defaultdict[str, list[EventStream]] = field(
        init=False,
        repr=False
    )
    in_flight_futures: dict[int, asyncio.Future] = field(
        init=False,
        repr=False
    )
    ws: Optional[websockets.WebSocketClientProtocol] = field(
        init=False,
        repr=False
    )
    ws_listener: Optional[asyncio.Task] = field(
        init=False,
        repr=False
    )
    ws_connected: Optional[asyncio.Future] = field(
        init=False,
        repr=False
    )

    ws_url: str

    def __post_init__(self):
        self.event_streams = defaultdict(list)
        self.in_flight_futures = {}
        self.ws = None
        self.ws_connected = None
        self.ws_listener = None

    async def _handle_event(self, event: dict):
        for stream in self.event_streams[event['method']]:
            await stream.publish(
                event
            )

    async def _handle_message(self, message: str):
        message = json.loads(message)

        if 'id' in message:
            return await self._handle_response(
                message
            )

        else:
            return await self._handle_event(
                message
            )

    async def _handle_response(self, response: dict):
        future = self.in_flight_futures.pop(
            response['id'],
            None
        )

        if future is None:
            return

        try:
            _validate_response(
                response
            )

            future.set_result(
                response['result']
            )

        except Exception as e:
            future.set_exception(e)

    async def _listen_async(self):
        async with websockets.connect(self.ws_url) as ws:
            self.ws = ws
            self.ws_connected.set_result(
                None
            )

            while True:
                message = await ws.recv()
                await self._handle_message(
                    message
                )

    async def close_stream(
            self,
            stream: EventStream
    ):
        for event in stream.event_names:
            self.event_streams[event].remove(
                stream
            )

    async def connect(self):
        loop = asyncio.get_event_loop()

        self.ws_connected = loop.create_future()
        self.ws_listener = loop.create_task(self._listen_async())

        await self.ws_connected

    async def open_stream(
            self,
            events: list[str]
    ) -> EventStream:
        stream = EventStream(self, events)

        for event in events:
            self.event_streams[event].append(stream)

        return stream

    async def send(
            self,
            method: str,
            params: dict
    ):
        loop = asyncio.get_event_loop()

        request_id = _next_rpc_id()
        request = {
            'id': request_id,
            'method': method,
            'params': params
        }

        request = json.dumps(request)
        future = loop.create_future()

        self.in_flight_futures[request_id] = future

        try:
            await self.ws.send(request)

        except Exception as e:
            future.set_exception(e)

        return future
