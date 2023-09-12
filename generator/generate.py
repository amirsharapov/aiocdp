import json
import logging
from pathlib import Path

from generator.nodes.protocol import Protocol

ROOT = '.'

logging.basicConfig(
    level=logging.DEBUG,
    format='\n%(message)s\n'
)


def parse(protocol_paths: list[str | Path] = None) -> list['Protocol']:
    protocols = []

    for path in protocol_paths:
        data = json.load(open(path))
        protocol = Protocol.from_dict(data)
        protocol.resolve_children()
        protocols.append(protocol)

    return protocols


def main():
    protocols = parse([
        'static/protocols/1.3/browser_protocol.json',
        'static/protocols/1.3/js_protocol.json'
    ])

    for protocol in protocols:
        for domain in protocol.domains:
            domain.generate_type_imports()
            domain.generate_class_definition()


if __name__ == '__main__':
    main()
