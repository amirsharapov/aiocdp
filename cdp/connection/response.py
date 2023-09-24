import asyncio
from dataclasses import dataclass, field
from typing import Generic, Optional, TypeVar, Callable

_T = TypeVar('_T')


@dataclass
class PendingResponse(Generic[_T]):
    value: Optional[_T] = field(
        init=False,
        repr=False
    )

    future: Optional[asyncio.Future]
    middleware: list[Callable]

    async def _get(self, timeout: int):
        try:
            return await asyncio.wait_for(
                self.future,
                timeout
            )

        except asyncio.TimeoutError as e:
            message = 'Timed out waiting for response'
            raise TimeoutError(message) from e

    def add_middleware(self, middleware: Callable[[_T], _T]):
        self.middleware.append(middleware)

    def get(self, timeout: int = 10) -> _T:
        loop = asyncio.get_event_loop()

        if self.future is None:
            return self.value

        if self.future.done():
            value = self.future.result()

        else:
            value = loop.run_until_complete(
                self._get(
                    timeout=timeout
                )
            )

        for middleware in self.middleware:
            value = middleware(value)

        self.value = value['result']

        return self.value
