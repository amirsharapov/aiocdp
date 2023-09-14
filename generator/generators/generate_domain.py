import ast
from collections import defaultdict

from generator.types import Domain, Command
from generator.utils import (
    snake_case,
    is_undefined,
    is_defined,
    coalesce_undefined,
    cdp_to_python_type,
    is_builtin
)


def _generate_dataclass_import(domain: Domain):
    should_generate = False

    for command in domain.commands:
        if command.parameters:
            should_generate = True
            break

    if not should_generate:
        return

    return ast.ImportFrom(
        module='dataclasses',
        names=[
            ast.alias('dataclass')
        ]
    )


def _generate_external_type_imports(domain: Domain):
    import_tree = defaultdict(set)

    for command in domain.commands:
        for parameter in command.parameters:
            if parameter.ref.domain:
                import_tree[parameter.ref.domain_snake_case].add(
                    parameter.ref.type
                )

    imports = []

    for domain, types in import_tree.items():
        types = sorted(types)

        imports.append(
            ast.ImportFrom(
                module=f'cdp.domains.{domain}.types',
                names=[ast.alias(name) for name in types]
            )
        )

    return imports


def _generate_util_imports(domain: Domain):
    return [
        ast.ImportFrom(
            module='cdp.utils',
            names=[
                ast.alias('is_defined'),
                ast.alias('MaybeUndefined'),
                ast.alias('UNDEFINED')
            ]
        )
    ]


def _generate_send_command_method_parameter_signature(command: Command):
    arguments = ast.arguments(
        args=[],
        defaults=[]
    )

    arguments.args.append(
        ast.arg(
            arg='self'
        )
    )

    for parameter in command.parameters:
        parameter_name = parameter.name_snake_cased

        if is_builtin(parameter_name):
            parameter_name += '_'

        arg = ast.arg(
            arg=snake_case(parameter_name)
        )

        annotation = cdp_to_python_type(
            coalesce_undefined([
                parameter.type,
                parameter.ref.type
            ])
        )

        arg.annotation = ast.Name(annotation)

        if parameter.optional:
            arguments.defaults.append(
                ast.Name(
                    id='UNDEFINED'
                )
            )

        arguments.args.append(arg)

    return arguments


def _generate_send_command_method_initial_params(command: Command):
    params = ast.Dict(
        keys=[],
        values=[]
    )

    for parameter in command.parameters:
        if parameter.optional:
            continue

        parameter_name = parameter.name_snake_cased

        if is_builtin(parameter_name):
            parameter_name += '_'

        params.keys.append(
            ast.Constant(
                value=parameter.name,
                kind='str'
            )
        )

        params.values.append(
            ast.Name(
                id=parameter_name
            )
        )

    return ast.Assign(
        targets=[
            ast.Name(
                id='params'
            )
        ],
        value=params
    )


def _generate_send_command_method_optional_params(command: Command):
    ifs = []

    for parameter in command.parameters:
        if not parameter.optional:
            continue

        ifs.append(
            ast.If(
                test=ast.Call(
                    func=ast.Name('is_defined'),
                    args=[
                        ast.Name(parameter.name_snake_cased)
                    ]
                ),
                body=[
                    ast.Assign(
                        targets=[
                            ast.Subscript(
                                value=ast.Name('params'),
                                slice=ast.Constant(parameter.name, kind='str')
                            )
                        ],
                        value=ast.Name(parameter.name_snake_cased)
                    )
                ]
            )
        )

    return ifs


def _generate_send_command_method_return_call(command: Command):
    return ast.Return(
        value=ast.Call(
            func=ast.Attribute(
                value=ast.Name('self'),
                attr='_send_command',
            ),
            args=[
                ast.Constant(f'"{command.parent.domain}.{command.name}"'),
                ast.Name('params')
            ]
        )
    )


def _generate_send_command_method_return_signature(command: Command):
    return ast.Name(
        command.returns
    )


def _generate_send_command_method(command: Command):
    function = ast.FunctionDef(
        name=snake_case(command.name),
        args=None,
        body=[]
    )

    function.args = _generate_send_command_method_parameter_signature(
        command
    )

    function.body.append(
        _generate_send_command_method_initial_params(
            command
        ),
    )

    function.body.extend(
        _generate_send_command_method_optional_params(
            command
        )
    )

    function.body.append(
        _generate_send_command_method_return_call(
            command
        )
    )

    function.returns = _generate_send_command_method_return_signature(
        command
    )

    return function


def _generate_class_definition(domain: Domain):
    class_ = ast.ClassDef(
        name=domain.domain,
        bases=[
            ast.Name('BaseDomain')
        ],
        body=[],
        decorator_list=[
            ast.Name('dataclass')
        ]
    )

    for command in domain.commands:
        class_.body.append(
            _generate_send_command_method(command)
        )

    return class_


def generate(domain: Domain):
    root = ast.Module(
        body=[]
    )

    if import_ := _generate_dataclass_import(domain):
        root.body.append(import_)

    if imports := _generate_external_type_imports(domain):
        root.body += imports

    if imports := _generate_util_imports(domain):
        root.body += imports

    root.body.append(
        _generate_class_definition(domain)
    )

    return root
