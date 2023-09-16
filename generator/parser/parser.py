import json
from pathlib import Path

from generator.parser import registry
from generator.parser.types import Protocol


def parse(protocol_paths: list[str | Path] = None) -> list['Protocol']:
    protocols = []

    for path in protocol_paths:
        protocol = json.load(open(path))
        protocol = Protocol.from_dict(protocol)
        protocol.resolve_parent_refs()

        for domain in protocol.domains:
            registry.add_domain(domain)
            for type_ in domain.types:
                registry.add_type(type_)

        protocols.append(protocol)

    return protocols
