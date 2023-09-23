import asyncio
import json
from asyncio import Future
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

import websockets.client as websockets

from cdp.connection.response import PendingResponse
from cdp.connection.stream import EventStream


class JSONRPCRequestID:
    next_id = 0

    @classmethod
    def get(cls):
        cls.next_id += 1
        return cls.next_id


@dataclass
class Connection:
    event_streams: defaultdict[str, list[EventStream]] = field(
        init=False,
        repr=False
    )
    in_flight_futures: dict = field(
        init=False,
        repr=False
    )
    ws: Optional['websockets.WebSocketClientProtocol'] = field(
        init=False,
        repr=False
    )
    ws_receiver: Optional[asyncio.Task] = field(
        init=False,
        repr=False
    )
    ws_connected: Optional[Future] = field(
        init=False,
        repr=False
    )

    url: str

    def __post_init__(self):
        self.event_streams = defaultdict(list)
        self.in_flight_futures = {}
        self.ws = None
        self.ws_connected = None
        self.ws_receiver = None

    async def _run_async(self):
        async with websockets.connect(self.url) as ws:
            self.ws = ws
            self.ws_connected.set_result(None)

            while True:
                message = await ws.recv()
                self._on_message(message)

    def _on_message(self, message: str):
        message = json.loads(message)

        if 'id' in message:
            future = self.in_flight_futures[message['id']]

            if 'error' in message and message['error']:
                error = message['error']
                raise Exception(
                    'Received the following error: '
                    f'Err Code: {error["code"]}, '
                    f'Err Message: {error["message"]}, '
                    f'Raw Message: {message}'
                )

            try:
                future.set_result(message)

            except Exception as e:
                future.set_exception(e)

        else:
            for stream in self.event_streams[message['method']]:
                stream.publish(message)

    def connect(self):
        loop = asyncio.get_event_loop()

        self.ws_connected = loop.create_future()
        self.ws_receiver = loop.create_task(
            self._run_async()
        )

        loop.run_until_complete(
            self.ws_connected
        )

    def open_stream(
            self,
            events: list[str]
    ) -> EventStream:
        stream = EventStream(
            self,
            events
        )

        for event in events:
            self.event_streams[event].append(
                stream
            )

        return stream

    def send_request(
            self,
            method: str,
            params: dict,
            response_middlewares: list[callable] = None
    ) -> PendingResponse:
        loop = asyncio.get_event_loop()

        request_id = JSONRPCRequestID.get()
        request = {
            'id': request_id,
            'method': method,
            'params': params
        }

        request = json.dumps(request)

        future = loop.create_future()

        self.in_flight_futures[request_id] = future

        try:
            coroutine = self.ws.send(request)
            loop.run_until_complete(coroutine)

        except Exception as e:
            future.set_exception(e)

        return PendingResponse(
            future,
            response_middlewares or []
        )
