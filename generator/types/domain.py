import logging
from collections import defaultdict
from dataclasses import dataclass

from generator.types.base import ComplexNode
from generator.types.command import Command
from generator.types.event import Event
from generator.types.ref import Ref
from generator.types.type import Type
from generator.utils import (
    MaybeUndefined,
    UNDEFINED,
    concat_lines,
    is_defined,
    split_ref,
    snake_case,
    create_vertical_comma_separated_list
)

logger = logging.getLogger(
    'cdp.generator'
)


@dataclass
class Domain(ComplexNode):
    domain: str
    description: MaybeUndefined[str]
    types: list['Type']
    commands: list['Command']
    events: list['Event']
    dependencies: list[str]
    experimental: MaybeUndefined[bool]
    deprecated: MaybeUndefined[bool]

    @classmethod
    def from_dict(cls, data):
        return cls(
            domain=data['domain'],
            description=data.get('description', UNDEFINED),
            types=[Type.from_dict(type_) for type_ in data.get('types', [])],
            commands=[Command.from_dict(command) for command in data.get('commands', [])],
            events=[Event.from_dict(event) for event in data.get('events', [])],
            dependencies=data.get('dependencies', []),
            experimental=data.get('experimental', UNDEFINED),
            deprecated=data.get('deprecated', UNDEFINED)
        )

    @property
    def class_name(self):
        return self.domain

    @property
    def module_name(self):
        return snake_case(self.domain)

    def get_refs(self) -> list[Ref]:
        refs = []

        for type_ in self.types:
            refs += type_.get_refs()

        for command in self.commands:
            refs += command.get_refs()

        for event in self.events:
            refs += event.get_refs()

        return refs

    def generate_class_definition(self):
        result = concat_lines([
            f'@dataclass',
            f'class {self.domain}(Domain):',
        ])

        if is_defined(self.description):
            description = self.description.split('\n')
            description = '\n    '.join(description)

        else:
            description = 'No description.'

        result = concat_lines([
            result,
            f'    """',
            f'    {description}',
            f'    """'
        ])

        logger.debug(result)

        return result

    def generate_type_imports(self):
        refs = self.get_refs()
        import_tree = defaultdict(set)

        for ref in refs:
            domain, type_ = split_ref(ref)
            domain = domain or self.domain
            domain = snake_case(domain)

            import_tree[domain].add(type_)

        imports = []

        for domain, types in import_tree.items():

            lines = [
                f'from cdp.domains.{domain}.types import (',
                create_vertical_comma_separated_list(
                    sorted(types),
                    4,
                    False
                ),
                f')'
            ]

            imports.append(
                concat_lines(
                    lines
                )
            )

        result = concat_lines(
            sorted(imports)
        )

        logger.debug(result)

        return result
