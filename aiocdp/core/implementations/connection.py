import asyncio
import json
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

import websockets.client as websockets
from websockets import ConnectionClosedError

from aiocdp import logging
from aiocdp.core.interfaces.stream import IEventStream, IEventStreamReader
from aiocdp.core.interfaces.connection import IConnection
from aiocdp.core.implementations.stream import EventStream
from aiocdp.exceptions import raise_invalid_rpc_response
from aiocdp.ioc import get_class

_rpc_id = 0


def next_rpc_id():
    """
    Generates a new sequential id for rpc requests.

    Implementation Notes:
    - Thread safety was not implemented because this is used with asyncio context.
    """
    global _rpc_id
    _rpc_id += 1
    return _rpc_id


def validate_rpc_response(response: dict):
    """
    Validates the given rpc response and raises an exception if the response contains an error.
    """
    if 'error' in response and response['error']:
        raise_invalid_rpc_response(response)


@dataclass
class Connection(IConnection):
    """
    Represents a websocket connection to a CDP target.
    """

    """
    The url of the websocket connection.
    """
    ws_url: str

    """
    The futures that are currently waiting for a response to a request.
    """
    in_flight_futures: dict[int, asyncio.Future] = field(
        default_factory=dict,
        init=False
    )

    """
    The streams that are currently listening for events.
    """
    streams: defaultdict[str, list['IEventStream']] = field(
        default_factory=lambda: defaultdict(list),
        init=False
    )

    """
    The websocket connection instance.
    """
    ws: Optional[websockets.WebSocketClientProtocol] = field(
        default=None,
        init=False
    )

    """
    The asyncio task that is listening for messages from the websocket in the background.
    """
    ws_listener: Optional[asyncio.Task] = field(
        default=None,
        init=False
    )

    """
    The future that is set when the websocket connection is established.
    """
    ws_connected: Optional[asyncio.Future] = field(
        default=None,
        init=False
    )

    @classmethod
    def init(cls, ws_url: str):
        """
        Initializer method for the Connection class
        """
        return cls(ws_url)

    def is_connected(self):
        """
        Public readonly access to the connection status.
        """
        return self.ws is not None

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
            return self._handle_response(message)

        else:
            return self._handle_event(message)

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
            validate_rpc_response(response)
            future.set_result(response['result'])

        except Exception as e:
            future.set_exception(e)

    async def _listen_async(self, ws_connect_kwargs: dict = None):
        """
        Listens for messages from the websocket.
        """
        ws_connect_kwargs = ws_connect_kwargs or {}

        async with websockets.connect(self.ws_url, **ws_connect_kwargs) as ws:
            self.ws = ws
            self.ws_connected.set_result(True)

            while True:
                try:
                    message = await ws.recv()

                except ConnectionClosedError as e:
                    print(f'Connection closed. Exception: {str(e)}')
                    break

                await self._handle_message(message)

    def close_stream(
            self,
            stream: 'IEventStream'
    ):
        """
        Unsubscribes the given event stream from receiving events from the connection.
        """
        for event in stream.get_events_to_listen():
            self.streams[event].remove(stream)

    async def connect(self, ws_connect_kwargs: dict = None):
        """
        Connects to the websocket and starts the listener task.
        """
        if self.is_connected():
            return

        loop = asyncio.get_event_loop()

        self.ws_connected = loop.create_future()
        self.ws_listener = loop.create_task(
            self._listen_async(
                ws_connect_kwargs=ws_connect_kwargs
            )
        )

        await self.ws_connected

    async def disconnect(self):
        """
        Disconnects from the websocket and cancels the listener task.
        """
        if not self.is_connected():
            return

        await self.ws.close()
        self.ws_listener.cancel()

    def is_stream_closed(self, stream: 'IEventStream'):
        """
        Checks if the given stream is closed.
        """
        for event in stream.get_events_to_listen():
            if stream in self.streams[event]:
                return False

        return True

    def open_stream(
            self,
            events: list[str]
    ) -> IEventStreamReader:
        """
        Opens a new event stream for the given events and returns a reader for it.
        """
        stream_class = get_class(
            IEventStream,
            EventStream
        )

        stream = stream_class.init(
            connection=self,
            events_to_listen=events
        )

        for event in events:
            self.streams[event].append(stream)

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
