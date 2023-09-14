import json
import logging
import shutil
from pathlib import Path

from generator.types.protocol import Protocol
from generator import generators
from generator.utils import snake_case
from generator.generators.visitor import SourceCodeGenerator

logging.basicConfig(
    level=logging.DEBUG,
    format='\n%(message)s\n'
)


def parse(protocol_paths: list[str | Path] = None) -> list['Protocol']:
    protocols = []

    for path in protocol_paths:
        data = json.load(open(path))
        protocol = Protocol.from_dict(data)
        protocol.resolve_parent_refs()
        protocols.append(protocol)

    return protocols


def main():
    protocols = parse([
        'static/protocols/1.3/browser_protocol.json',
        'static/protocols/1.3/js_protocol.json'
    ])

    Path('cdp/domains').mkdir(parents=True, exist_ok=True)
    Path('cdp/domains/__init__.py').touch()

    for item in Path('cdp/domains').iterdir():
        if item.name not in ('__init__.py', 'base.py'):
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

    for protocol in protocols:
        for domain in protocol.domains:
            module_name = snake_case(domain.domain)

            Path(f'cdp/domains/{module_name}').mkdir(parents=True, exist_ok=True)
            Path(f'cdp/domains/{module_name}/__init__.py').touch()

            module = generators.generate_domain.generate(domain)
            module = SourceCodeGenerator().generate(module)

            print(module)

            Path(f'cdp/domains/{module_name}/domain.py').write_text(module)

            module = generators.generate_types.generate(domain)
            module = SourceCodeGenerator().generate(module)

            print(module)

            Path(f'cdp/domains/{module_name}/types.py').write_text(module)


if __name__ == '__main__':
    main()
