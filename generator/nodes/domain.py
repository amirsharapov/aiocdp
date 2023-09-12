import logging
from collections import defaultdict
from dataclasses import dataclass

from generator.nodes.base import Node
from generator.nodes.command import Command
from generator.nodes.event import Event
from generator.nodes.type import Type
from generator.utils import MaybeUndefined, UNDEFINED, concat_lines, is_defined, split_ref, snake_case

logger = logging.getLogger(
    'cdp.generator'
)


@dataclass
class Domain(Node):
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
    def module_name(self):
        return snake_case(self.domain)

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
        import_tree = defaultdict(set)

        for type_ in self.types:
            for ref in type_.get_refs():
                domain, name = split_ref(ref)
                import_tree[domain].add(name)

        for command in self.commands:
            for ref in command.get_refs():
                domain, name = split_ref(ref)
                import_tree[domain].add(name)

        for event in self.events:
            for ref in event.get_refs():
                domain, name = split_ref(ref)
                import_tree[domain].add(name)

        imports = []

        for domain, types in import_tree.items():

            if domain is None:
                domain = self.domain

            domain = snake_case(domain)

            lines = [
                f'from cdp.domains.{domain} import (',
            ]

            for i, type_ in enumerate(sorted(types)):
                lines.append(
                    f'    {type_}'
                )

                if i != len(types) - 1:
                    lines[-1] += ','

            lines.append(')')

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
