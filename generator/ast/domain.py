import ast
from collections import defaultdict

from generator.parser.types import Domain, Command
from generator.parser.types.property import CommandParameter
from generator.utils import (
    snake_case,
    coalesce_undefined,
    cdp_to_python_type,
    is_builtin
)


def _generate_imports():
    return [
        ast.ImportFrom(
            module='dataclasses',
            names=[
                ast.alias('dataclass')
            ]
        ),
        ast.ImportFrom(
            module='cdp.utils',
            names=[
                ast.alias('is_defined'),
                ast.alias('UNDEFINED')
            ]
        ),
        ast.ImportFrom(
            module='typing',
            names=[
                ast.alias('TYPE_CHECKING')
            ]
        ),
        ast.ImportFrom(
            module='cdp.domains.mapper',
            names=[
                ast.alias('from_dict'),
                ast.alias('to_dict')
            ]
        )
    ]


def _generate_type_imports(domain: Domain):
    import_tree = defaultdict(set)

    for command in domain.commands:
        if command.returns:
            import_tree[domain.domain_snake_case].add(
                command.name_pascal_case + 'ReturnT'
            )

        for parameter in command.parameters:
            for ref in parameter.get_refs():
                module_name = ref.actual_domain.domain_snake_case
                import_tree[module_name].add(
                    ref.type
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


def _generate_send_method_parameter_signature(command: Command):
    arguments = ast.arguments(
        args=[],
        defaults=[],
        render_context={
            'expand': True
        }
    )

    arguments.args.append(
        ast.arg(
            arg='self'
        )
    )

    required = []
    optional = []

    for parameter in command.parameters:
        if parameter.optional:
            optional.append(parameter)
        else:
            required.append(parameter)

    for parameter in required + optional:
        arg = ast.arg(
            arg=parameter.name_snake_cased_collision_safe,
            annotation=ast.Constant(
                cdp_to_python_type(
                    coalesce_undefined([
                        parameter.type,
                        parameter.ref.type
                    ])
                )
            )
        )

        if parameter.optional:
            arguments.defaults.append(
                ast.Name(
                    id='UNDEFINED'
                )
            )

        arguments.args.append(arg)

    return arguments


def _generate_send_method_params_value(parameter: 'CommandParameter'):
    parameter_name = parameter.name_snake_cased_collision_safe

    basic_param = ast.Name(
        id=parameter_name
    )

    basic_param_with_to_json = ast.Call(
        func=ast.Name('to_dict'),
        args=[
            basic_param,
            ast.Constant('camel')
        ],
        render_context={
            'expand': True
        }
    )

    list_comp_with_to_json = ast.ListComp(
        elt=ast.Call(
            func=ast.Name('to_dict'),
            args=[
                ast.Name('item'),
                ast.Constant('camel')
            ]
        ),
        generators=[
            ast.comprehension(
                target=ast.Name('item'),
                iter=basic_param,
                ifs=[]
            )
        ]
    )

    if parameter.type == 'array':
        if parameter.items.ref.actual_type.properties:
            return list_comp_with_to_json
        else:
            return basic_param

    else:
        if parameter.ref.actual_type.properties:
            return basic_param_with_to_json
        else:
            return basic_param


def _generate_send_method_initial_params(command: Command):
    params = ast.Dict(
        keys=[],
        values=[]
    )

    for parameter in command.parameters:
        if parameter.optional:
            continue

        params.keys.append(
            ast.Constant(
                value=parameter.name,
            )
        )

        params.values.append(
            _generate_send_method_params_value(
                parameter
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


def _generate_send_method_optional_params(command: Command):
    ifs = []

    for parameter in command.parameters:
        if not parameter.optional:
            continue

        ifs.append(
            ast.If(
                test=ast.Call(
                    func=ast.Name('is_defined'),
                    args=[
                        ast.Name(
                            parameter.name_snake_cased_collision_safe
                        )
                    ]
                ),
                body=[
                    ast.Assign(
                        targets=[
                            ast.Subscript(
                                value=ast.Name('params'),
                                slice=ast.Constant(parameter.name)
                            )
                        ],
                        value=_generate_send_method_params_value(
                            parameter
                        )
                    )
                ],
                render_context={
                    'lines_before': 1
                }
            )
        )

    return ifs


def _generate_send_method_return_call(command: Command):
    call = ast.Call(
        func=ast.Attribute(
            value=ast.Name('self'),
            attr='_send_command',
        ),
        args=[
            ast.Constant(f'{command.parent.domain}.{command.name}'),
            ast.Name('params'),
            ast.Constant(bool(command.returns))
        ],
        keywords=[],
        render_context={
            'expand': True
        }
    )

    if command.returns:
        call.args.append(
            ast.Lambda(
                args=ast.arguments(
                    args=[
                        ast.arg('data')
                    ]
                ),
                body=ast.Call(
                    func=ast.Name('from_dict'),
                    args=[
                        ast.Name(command.name_pascal_case + 'ReturnT'),
                        ast.Name('data'),
                        ast.Constant('camel')
                    ],
                    render_context={
                        'expand': True
                    }
                )
            )
        )

    return ast.Return(
        value=call,
        render_context={
            'lines_before': 1
        }
    )


def _generate_send_method_return_signature(command: 'Command'):
    if command.returns:
        slice_ = command.name_pascal_case + 'ReturnT'
    else:
        slice_ = 'None'

    return ast.Constant(
        f'IResponse[{slice_}]'
    )


def _generate_send_method(command: Command, index: int):
    function = ast.FunctionDef(
        name=snake_case(command.name),
        args=None,
        body=[],
        render_context={
            'expand': True,
            'lines_before': 1 if index > 0 else 0
        }
    )

    function.args = _generate_send_method_parameter_signature(
        command
    )

    function.body.append(
        _generate_send_method_initial_params(
            command
        ),
    )

    function.body.extend(
        _generate_send_method_optional_params(
            command
        )
    )

    function.body.append(
        _generate_send_method_return_call(
            command
        )
    )

    function.returns = _generate_send_method_return_signature(
        command
    )

    return function


def _generate_class(domain: Domain):
    class_ = ast.ClassDef(
        name=domain.domain,
        bases=[
            ast.Name('BaseDomain')
        ],
        body=[],
        decorator_list=[
            ast.Name('dataclass')
        ],
        render_context={
            'lines_before': 2
        }
    )

    for i, command in enumerate(domain.commands):
        class_.body.append(
            _generate_send_method(
                command,
                i
            )
        )

    return class_


def generate(domain: Domain):
    root = ast.Module(
        body=[
            ast.ImportFrom(
                module='cdp.domains.base',
                names=[
                    ast.alias('BaseDomain')
                ]
            ),
        ]
    )

    if imports := _generate_imports():
        root.body.extend(imports)

    if imports := _generate_type_imports(domain):
        root.body += imports

    root.body.append(
        ast.If(
            test=ast.Name('TYPE_CHECKING'),
            body=[
                ast.ImportFrom(
                    module='cdp.target.connection',
                    names=[
                        ast.alias('IResponse')
                    ]
                )
            ]
        )
    )

    root.body.append(
        _generate_class(domain)
    )

    return root
