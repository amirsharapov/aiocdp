import json
from pathlib import Path

from generator.parser.types import Protocol
from generator.parser.types.base import recursively_link_children


def parse(protocol_paths: list[str | Path] = None) -> list['Protocol']:
    protocols = []

    for path in protocol_paths:
        protocol = json.load(open(path))
        protocol = Protocol(protocol)

        recursively_link_children(protocol)

        protocols.append(protocol)

    for protocol in protocols:
        for domain in protocol.domains:
            domain.resolve_refs()

    return protocols
