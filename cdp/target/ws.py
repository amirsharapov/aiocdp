import json
import threading
from dataclasses import dataclass, field

from websocket import WebSocket


class JSONRPCRequestID:
    next_id = 0
    lock = threading.Lock()

    @classmethod
    def get(cls):
        with cls.lock:
            cls.next_id += 1
            return cls.next_id


def send_json_rpc_request(
        ws: 'WebSocket',
        method: str,
        params: dict = None
):
    request_id = JSONRPCRequestID.get()
    request = {
        'id': request_id,
        'method': method,
    }

    if params is not None:
        request['params'] = params

    ws.send(json.dumps(request))


@dataclass
class Connection:
    in_flight_requests: dict = field(
        init=False
    )

    def __post_init__(self):
        self.in_flight_requests = {}
