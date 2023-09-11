from dataclasses import dataclass

from cdp.domains.domains import Domains
from cdp.target.ws import send_json_rpc_request


class DotDict(dict):
    def __getattr__(self, item: str):
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, item):
        del self[item]
    
    def __getitem__(self, item):
        result = super().__getitem__(item)
        
        if isinstance(result, dict):
            result = DotDict(
                result
            )
    
        return result


@dataclass
class DynamicDomain:
    name: str
    domains: 'Domains'

    def __getattr__(self, item: str):
        method = f'{self.name}.{item}'

        def wrapper(**kwargs):
            result = send_json_rpc_request(
                self.domains.target.connection,
                method,
                kwargs
            )

            return DotDict(
                result
            )

        return wrapper
