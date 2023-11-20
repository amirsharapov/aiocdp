from abc import ABC, abstractmethod

from aiocdp.core.interfaces.stream import IEventStream


class ITargetInfo(ABC):
    id: int


class ITarget(ABC):
    info: ITargetInfo = None

    @abstractmethod
    def close_stream(self, stream: IEventStream):
        pass
