from dataclasses import dataclass
from typing import Optional

from cdp.connection.connection import Connection


@dataclass
class IO:
    connection: Connection
    session_id: Optional[str]

    async def send(
            self,
            method: str,
            params: dict = None,
            return_response: bool = True
    ):
        params = params or {}

        if self.session_id:
            params['sessionId'] = self.session_id

        return await self.connection.send(
            method,
            params,
            return_response
        )

    async def open_events_stream(self, events: list[str]):
        return await self.connection.open_stream(
            events
        )
