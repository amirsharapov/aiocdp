from abc import ABC

from aiocdp.core.interfaces.stream import IEventStream


class ISession(ABC):
    async def close(self):
        """
        Closes the session by detaching from the target.
        """
        pass

    def close_stream(self, stream: IEventStream):
        """
        Closes the stream. Calls `Target.close_stream`.
        """
        pass

    async def open(self):
        """
        Opens the session by attaching to the target.
        """
        pass

    def open_stream(self, events: list[str]):
        """
        Opens a stream. Calls `self.target.open_stream` method on the target.
        """
        pass

    async def send(self, method: str, params: dict = None):
        """
        Sends a message to the target. Calls `self.target.send`.
        """
        pass

    async def send_and_await_response(self, method: str, params: dict = None):
        """
        Sends a message to the target and awaits a response. Calls `self.target.send_and_await_response`
        """
        pass
