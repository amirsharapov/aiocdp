import asyncio
import json
import threading
from abc import ABC, abstractmethod
from asyncio import Future
from dataclasses import dataclass, field
from typing import Optional, TypeVar, Generic, Callable

import websockets.client as websockets

_T = TypeVar('_T')


class JSONRPCRequestID:
    next_id = 0
    lock = threading.Lock()

    @classmethod
    def get(cls):
        with cls.lock:
            cls.next_id += 1
            return cls.next_id


@dataclass
class IFutureResponse(ABC, Generic[_T]):
    value: _T

    @abstractmethod
    def get(self) -> _T:
        ...


@dataclass
class IEventStream(ABC, Generic[_T]):
    events: list[_T]

    @abstractmethod
    def get_next(self) -> _T:
        ...

    @abstractmethod
    def close(self) -> None:
        ...


@dataclass
class IConnection(ABC):
    @abstractmethod
    def send_request(
            self,
            method: str,
            params: dict,
            expect_response: bool,
            response_hook: Callable
    ) -> IFutureResponse:
        ...

    @abstractmethod
    def capture_events(
            self,
            events: list[type]
    ) -> IEventStream:
        ...


@dataclass
class FutureResponse(IFutureResponse[_T]):
    future: Optional[asyncio.Future]

    async def _get(self, timeout: int = 10):
        try:
            return await asyncio.wait_for(
                fut=self.future,
                timeout=timeout
            )

        except asyncio.TimeoutError as e:
            message = 'Timed out waiting for response'
            raise TimeoutError(message) from e

    def get(self) -> _T:
        if self.future is None:
            return self.value

        if self.future.done():
            return self.future.result()

        event_loop = asyncio.get_event_loop()

        self.value = event_loop.run_until_complete(
            self._get()
        )

        return self.value


@dataclass
class Connection(IConnection):
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
        print(
            'Message with context: '
            f'Message: {message}'
        )

        message = json.loads(message)

        if 'id' in message:
            future_context = self.in_flight_futures[message['id']]

            future = future_context['future']

            if 'error' in message and message['error']:
                error = message['error']

                future.set_exception(
                    Exception(
                        'Received the following error: '
                        f'Err Code: {error["code"]}, '
                        f'Err Message: {error["message"]}, '
                        f'Raw Message: {message}'
                    )
                )
                return

            response_hook = future_context['response_hook']

            if response_hook:
                message = response_hook(message['result'])

            future.set_result(
                message
            )

    def connect(self):
        loop = asyncio.get_event_loop()

        self.ws_connected = loop.create_future()
        self.ws_receiver = loop.create_task(
            self._run_async()
        )

        loop.run_until_complete(
            self.ws_connected
        )

    def send_request(
            self,
            method: str,
            params: dict,
            expect_response: bool,
            response_hook: Callable = None
    ) -> FutureResponse:
        event_loop = asyncio.get_event_loop()

        request_id = JSONRPCRequestID.get()
        request = {
            'id': request_id,
            'method': method,
            'params': params
        }

        request = json.dumps(request)

        future = event_loop.create_future()
        result = FutureResponse(
            None,
            future
        )

        if expect_response:
            self.in_flight_futures[request_id] = {
                'future': future,
                'response_hook': response_hook
            }

        else:
            future.set_result(
                None
            )

        try:
            event_loop.run_until_complete(
                self.ws.send(request)
            )

        except Exception as e:
            future.set_exception(e)

        return result

    def capture_events(
            self,
            events: list[type]
    ) -> IEventStream:
        raise NotImplemented
