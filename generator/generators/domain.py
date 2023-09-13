import ast
from _ast import ImportFrom
from collections import defaultdict

from generator.types.domain import Domain
from generator.utils import (
    snake_case,
    is_undefined,
    is_defined,
    coalesce_undefined
)


def generate_base_imports() -> list[ast.ImportFrom]:
    return [
        ImportFrom(
            module='cdp.domains.base',
            names=[
                ast.alias('BaseDomain')
            ]
        )
    ]


def generate_type_imports(domain: Domain) -> list[ast.ImportFrom]:
    imports = []
    import_tree = defaultdict(set)

    for ref in domain.get_refs():
        module = ref.domain if is_defined(ref.domain) else domain.domain
        module = snake_case(module)

        import_tree[module].add(ref.type)

    for module, names in import_tree.items():
        imports.append(
            init_import_from(
                module=f'cdp.domains.{module}.types',
                names=[init_alias(name) for name in names]
            )
        )

    return imports


def generate_class(domain: Domain) -> ast.ClassDef:
    return init_class_def(
        name=domain.domain,
        bases=[
            init_name('BaseDomain')
        ],
        body=[
            generate_command_method(
                domain,
                command
            ) for
            command in
            domain.commands
        ]
    )


def generate_command_method(domain, command) -> ast.FunctionDef:
    function = init_function_def(
        name=snake_case(command.name),
        args=init_arguments(
            args=[
                init_arg('self')
            ]
        )
    )

    for parameter in command.parameters:
        arg = init_arg(
            arg=snake_case(parameter.name)
        )

        if is_defined(parameter.type) and is_defined(parameter.ref):
            print('Both type and ref are defined. Not sure how to handle')
            continue

        if is_undefined(parameter.type) and is_undefined(parameter.ref):
            print('Both type and ref are undefined. Not sure how to handle')

        annotation = coalesce_undefined([
            parameter.type,
            parameter.ref.type
        ])

        annotation = init_name(annotation)

        if parameter.optional:
            annotation = init_subscript(
                value=init_name('Optional'),
                slice_=annotation
            )

        arg.annotation = annotation

        function.args.args.append(arg)

    return function

def generate(domain: Domain):
    module = init_module(
        body=[
            *generate_base_imports(),
            *generate_type_imports(domain),
            generate_class(domain)
        ]
    )

    return module
