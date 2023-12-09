from dataclasses import dataclass, field
from typing import Optional

from aiocdp.core.interfaces.session import ISession
from aiocdp.core.interfaces.stream import IEventStream
from aiocdp.core.interfaces.target import ITarget


@dataclass
class Session(ISession):
    """
    Represents a session with a target.
    """

    """
    A reference to the target.
    """
    target: ITarget

    """
    The session ID.
    """
    session_id: Optional[str] = field(
        default=None,
        init=False
    )

    @classmethod
    def init(
        cls,
        target: ITarget
    ):
        """
        Initializer method for the ISession class
        """
        return cls(
            target=target
        )

    async def __aenter__(self):
        """
        Allows this object to be used as a context manager.
        """
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        """
        Closes this session when used as a context manager.
        """
        await self.close()

        if exc_type is not None:
            return False

    async def close(self):
        """
        Closes the session by detaching from the target.
        """
        method = 'Target.detachFromTarget'
        params = {
            'targetId': self.session_id
        }

        await self.send_and_await_response(
            method,
            params
        )

    def close_stream(self, stream: IEventStream):
        """
        Closes the stream. Calls `Target.close_stream`.
        """
        return self.target.close_stream(stream)

    async def open(self):
        """
        Opens the session by attaching to the target.
        """
        method = 'Target.attachToTarget'
        params = {
            'targetId': self.target.get_info().id
        }

        result = await self.send_and_await_response(
            method,
            params
        )

        self.session_id = result['sessionId']

    def open_stream(self, events: list[str]):
        """
        Opens a stream. Calls `self.target.open_stream` method on the target.
        """
        return self.target.open_stream(events)

    async def send(self, method: str, params: dict = None):
        """
        Sends a message to the target. Calls `self.target.send`.
        """
        params = params or {}
        params['sessionId'] = self.session_id

        return await self.target.send(
            method,
            params
        )

    async def send_and_await_response(self, method: str, params: dict = None):
        """
        Sends a message to the target and awaits a response. Calls `self.target.send_and_await_response`
        """
        params = params or {}
        params['sessionId'] = self.session_id

        return await self.target.send_and_await_response(
            method,
            params
        )
