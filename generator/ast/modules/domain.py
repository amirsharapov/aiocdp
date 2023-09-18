import ast
from collections import defaultdict

from generator.ast.utils import ast_imports
from generator.parser.types import Domain, Command
from generator.parser.types.property import CommandParameter
from generator.utils import (
    coalesce_undefined,
    cdp_to_python_type,
)


def _generate_imports():
    import_tree = defaultdict(set)

    import_tree['dataclasses'].add('dataclass')
    import_tree['cdp.utils'].add('is_defined')
    import_tree['cdp.utils'].add('UNDEFINED')
    import_tree['typing'].add('TYPE_CHECKING')
    import_tree['cdp.domains'].add('mappers')

    return ast_imports(
        import_tree
    )


def _generate_type_imports(domain: Domain):
    import_tree = defaultdict(set)

    for command in domain.commands:
        if command.returns:
            module = f'cdp.domains.{domain.domain_.snake_case}.types'
            import_tree[module].add(
                command.return_type_name
            )

        for parameter in command.parameters:
            for ref in parameter.get_refs():
                module = f'cdp.domains.{ref.actual_domain.domain_.snake_case}.types'
                import_tree[module].add(
                    ref.type
                )

    return ast_imports(
        import_tree
    )


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
            arg=parameter.name_.snake_case_non_colliding,
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


def _send_method_parameter_value(parameter: 'CommandParameter'):
    param_name = parameter.name_.snake_case_non_colliding
    value = ast.Name(param_name)

    if parameter.is_simple_type or parameter.is_array_of_simple_type:
        return value

    if parameter.is_complex_type:
        return ast.Call(
            func=ast.Name('to_dict'),
            args=[
                value,
                ast.Constant('camel')
            ],
            render_context={
                'expand': True
            }
        )

    if parameter.is_array_of_complex_type:
        return ast.ListComp(
            elt=ast.Call(
                func=ast.Name('to_dict'),
                args=[
                    ast.Name('_'),
                    ast.Constant('camel')
                ]
            ),
            generators=[
                ast.comprehension(
                    target=ast.Name('_'),
                    iter=value
                )
            ]
        )


def _generate_send_method_initial_params(command: Command):
    params = ast.Dict(
        keys=[],
        values=[]
    )

    for parameter in command.parameters:
        if parameter.optional:
            continue

        params.keys.append(
            ast.Constant(parameter.name)
        )

        params.values.append(
            _send_method_parameter_value(
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
                            parameter.name_.snake_case_non_colliding
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
                        value=_send_method_parameter_value(
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
                        ast.Name(command.return_type_name),
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


def _generate_send_method(command: Command, index: int):
    function = ast.FunctionDef(
        name=command.name_.snake_case,
        args=None,
        body=[],
        returns=ast.Constant(
            f'IFutureResponse[{command.return_type_name}]'
        ),
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
                        ast.alias('IFutureResponse')
                    ]
                )
            ]
        )
    )

    root.body.append(
        _generate_class(domain)
    )

    return root
