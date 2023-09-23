import logging
import shutil
from pathlib import Path

from generator import ast
from generator.parser import parser
from generator.ast.visitor import SourceCodeGenerator

logging.basicConfig(
    level=logging.DEBUG,
    format='\n%(message)s\n'
)


GENERATED_MODULE_HEADER = '''\
# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
'''


def main():
    protocols = parser.parse([
        'static/protocols/1.3/browser_protocol.json',
        'static/protocols/1.3/js_protocol.json'
    ])

    domains = (
        protocols[0].domains +
        protocols[1].domains
    )

    shutil.rmtree(
        path='cdp/generated/types',
        ignore_errors=True
    )

    Path('cdp/generated/types').mkdir(parents=True, exist_ok=True)
    Path('cdp/generated/types/__init__.py').touch()

    for domain in domains:
        module = ast.modules.types.generate(domain)
        module = SourceCodeGenerator().generate(module)

        Path(f'cdp/generated/types/{domain.domain.snake_case}.py').write_text(
            GENERATED_MODULE_HEADER +
            module.source
        )

    module = ast.modules.mapping.generate(domains)
    module = SourceCodeGenerator().generate(module)

    Path(f'cdp/generated/mapping.py').write_text(
        GENERATED_MODULE_HEADER +
        module.source
    )

    module = ast.modules.domains.generate(domains)
    module = SourceCodeGenerator().generate(module)

    Path(f'cdp/domains/domains.pyi').write_text(
        GENERATED_MODULE_HEADER +
        module.source
    )


if __name__ == '__main__':
    main()
