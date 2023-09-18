_types = {}

def register_type(domain: str, type_name: str, dataclass_type: type):
    _types[domain, type_name] = dataclass_type


def get_type(domain: str, type_name: str) -> type:
    return _types[domain, type_name]
