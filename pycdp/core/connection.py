import asyncio
import json
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

import websockets.client as websockets

from pycdp.core.events import EventStreamReader, EventStream
from pycdp import logging
from pycdp.exceptions import raise_invalid_rpc_response

_id = 0


def next_rpc_id():
    """
    Generates a new sequential id for rpc requests.
    """
    global _id
    _id += 1
    return _id


def validate_rpc_response(response: dict):
    """
    Validates the given rpc response and raises an exception if the response contains an error.
    """
    if 'error' in response and response['error']:
        raise_invalid_rpc_response(response)


@dataclass
class Connection:
    """
    Represents a websocket connection to a CDP target.
    """
    streams: defaultdict[str, list[EventStream]] = field(
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

    @property
    def is_connected(self):
        """
        Public readonly access to the connection status.
        """
        return self.ws is not None

    def __post_init__(self):
        self.streams = defaultdict(list)
        self.in_flight_futures = {}
        self.ws = None
        self.ws_connected = None
        self.ws_listener = None

    def _handle_event(self, event: dict):
        """
        Handles an event received from the websocket.
        """
        if logging.is_logging_enabled('connection.handle_event'):
            print(event)

        for stream in self.streams[event['method']]:
            stream.write(event)

    async def _handle_message(self, message: str):
        """
        Handles any message received from the websocket.
        """
        if logging.is_logging_enabled('connection.handle_message'):
            print(message)

        message = json.loads(message)

        if 'id' in message:
            return self._handle_response(
                message
            )

        else:
            return self._handle_event(
                message
            )

    def _handle_response(self, response: dict):
        """
        Handles a response received from the websocket.
        """
        if logging.is_logging_enabled('connection.handle_response'):
            print(response)

        future = self.in_flight_futures.pop(
            response['id'],
            None
        )

        if future is None:
            return

        try:
            validate_rpc_response(
                response
            )

            future.set_result(
                response['result']
            )

        except Exception as e:
            future.set_exception(e)

    async def _listen_async(self):
        """
        Listens for messages from the websocket.
        """
        async with websockets.connect(self.ws_url) as ws:
            self.ws = ws
            self.ws_connected.set_result(
                True
            )

            while True:
                message = await ws.recv()
                await self._handle_message(
                    message
                )

    def close_stream(
            self,
            stream: EventStream
    ):
        """
        Unsubscribes the given event stream from receiving events from the connection.
        """
        for event in stream.events_to_listen:
            self.streams[event].remove(stream)

    async def connect(self):
        """
        Connects to the websocket and starts the listener task.
        """
        if self.is_connected:
            return

        loop = asyncio.get_event_loop()

        self.ws_connected = loop.create_future()
        self.ws_listener = loop.create_task(self._listen_async())

        await self.ws_connected

    async def disconnect(self):
        """
        Disconnects from the websocket and cancels the listener task.
        """
        if not self.is_connected:
            return

        await self.ws.close()
        self.ws_listener.cancel()

    def is_stream_closed(self, stream: EventStream):
        """
        Checks if the given stream is closed.
        """
        for event in stream.events_to_listen:
            if stream in self.streams[event]:
                return False

        return True

    def open_stream(
            self,
            events: list[str]
    ) -> EventStreamReader:
        """
        Opens a new event stream for the given events.
        """
        stream = EventStream.create(
            self,
            events
        )

        for event in events:
            self.streams[event].append(
                stream
            )

        return stream.get_reader()

    async def send(
            self,
            method: str,
            params: dict
    ):
        """
        Sends a message to the websocket.
        """
        loop = asyncio.get_event_loop()

        request_id = next_rpc_id()
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
