import asyncio
import json
import threading
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, TypeVar, Generic

from websocket import WebSocketApp

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
class IResult(ABC, Generic[_T]):
    value: _T

    @abstractmethod
    def get(self) -> _T:
        ...


@dataclass
class IConnection(ABC):
    @abstractmethod
    def send(self, method: str, params: dict, expect_response: bool) -> IResult[Optional[dict]]:
        ...


@dataclass
class Result(IResult[_T]):
    future: Optional[asyncio.Future]

    async def _wait(self, timeout: int = 10):
        try:
            await asyncio.wait_for(
                fut=self.future,
                timeout=timeout
            )

        except asyncio.TimeoutError as e:
            raise TimeoutError(
                'Timed out waiting for response'
            ) from e

    def get(self) -> _T:
        if not self.future or self.future.done():
            return self.value

        event_loop = asyncio.get_event_loop()

        self.value = event_loop.run_until_complete(
            self._wait()
        )

        return self.value


@dataclass
class Connection(IConnection):
    in_flight_futures: dict = field(
        init=False,
        repr=False
    )
    ws: 'WebSocketApp' = field(
        init=False,
        repr=False
    )
    ws_thread: threading.Thread = field(
        init=False,
        repr=False
    )
    ws_thread_lock: threading.Lock = field(
        init=False,
        repr=False
    )
    ws_thread_started: bool = field(
        init=False,
        repr=False
    )

    url: str

    def __post_init__(self):
        self.in_flight_futures = {}
        self.ws = WebSocketApp(
            url=self.url,
            on_error=self._on_error,
            on_message=self._on_message,
        )
        self.ws_thread = threading.Thread(
            target=self._run
        )
        self.ws_thread_lock = threading.Lock()
        self.ws_thread_started = False

    def _on_close(self, ws: 'WebSocketApp', status_code: int, message: str):
        print(
            'Closed with context: '
            f'Status Code: {status_code}, '
            f'Message: {message}'
        )

    def _on_error(self, ws: 'WebSocketApp', message: str):
        print(message)

    def _on_message(self, ws: 'WebSocketApp', message: str):
        print(message)

        message = json.loads(message)

        if 'id' in message:
            self.in_flight_futures[message['id']].set_result(message)

    def _run(self):
        self.ws.run_forever()

    def connect(self):
        if not self.ws_thread_started:
            self.ws_thread.start()
            self.ws_thread_started = True

    def send(self, method: str, params: dict, expect_response: bool) -> Result[Optional[dict]]:
        event_loop = asyncio.get_event_loop()

        request_id = JSONRPCRequestID.get()
        request = {
            'id': request_id,
            'method': method,
            'params': params
        }

        request = json.dumps(request)

        future = event_loop.create_future()
        result = Result(
            None,
            future
        )

        if expect_response:
            self.in_flight_futures[request_id] = (
                future
            )

        else:
            future.set_result(
                None
            )

        self.ws.send(request)

        return result
