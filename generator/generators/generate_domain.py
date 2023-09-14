import ast
from collections import defaultdict

from generator.types import Domain
from generator.utils import (
    snake_case,
    is_undefined,
    is_defined,
    coalesce_undefined,
    cdp_to_python_type,
    is_builtin
)


config = {
    'condition': '',
    'engine': 'jinja'  # 'static', 'ast'
}


def generate(domain: Domain):
    root = ast.Module(
        body=[
            ast.ImportFrom(
                module='dataclasses',
                names=[
                    ast.alias('dataclass')
                ]
            ),
            ast.ImportFrom(
                module='cdp.domains.base',
                names=[
                    ast.alias('BaseDomain')
                ]
            ),
            ast.ImportFrom(
                module='cdp.utils',
                names=[
                    ast.alias('is_defined'),
                    ast.alias('MaybeUndefined'),
                    ast.alias('UNDEFINED')
                ]
            )
        ]
    )

    import_tree = defaultdict(set)

    for command in domain.commands:
        for ref in command.get_refs():
            module_name = ref.domain if is_defined(ref.domain) else domain.domain
            module_name = snake_case(module_name)

            import_tree[module_name].add(ref.type)

    for module_name, names in import_tree.items():
        root.body.append(
            ast.ImportFrom(
                module=f'cdp.domains.{module_name}.types',
                names=[ast.alias(name) for name in names]
            )
        )

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
        function = ast.FunctionDef(
            name=snake_case(command.name),
            args=ast.arguments(
                args=[
                    ast.arg('self')
                ],
                defaults=[]
            ),
            body=[]
        )

        required_args = []
        optional_args = []

        for parameter in command.parameters:
            parameter_name = parameter.snake_name

            if is_builtin(parameter_name):
                parameter_name += '_'

            arg = ast.arg(
                arg=snake_case(parameter_name)
            )

            if is_defined(parameter.type) and is_defined(parameter.ref):
                print('Both type and ref are defined. Not sure how to handle')

            if is_undefined(parameter.type) and is_undefined(parameter.ref):
                print('Both type and ref are undefined. Not sure how to handle')

            annotation = cdp_to_python_type(
                coalesce_undefined([
                    parameter.type,
                    parameter.ref.type
                ])
            )

            arg.annotation = ast.Name(annotation)

            if parameter.optional:
                optional_args.append((
                    parameter,
                    arg
                ))

                function.args.defaults.append(
                    ast.Name(
                        id='UNDEFINED'
                    )
                )

            else:
                required_args.append((
                    parameter,
                    arg
                ))

            function.args.args.append(arg)

        assigned_dict = ast.Dict(
            keys=[],
            values=[]
        )

        for parameter, arg in required_args:
            assigned_dict.keys.append(ast.Name(parameter.name))
            assigned_dict.values.append(ast.Name(arg.arg))

        function.body.append(
            ast.Assign(
                targets=[ast.Name('params')],
                value=assigned_dict
            )
        )

        for parameter, arg in optional_args:
            function.body.append(
                ast.If(
                    test=ast.Call(
                        func=ast.Name('is_defined'),
                        args=[
                            ast.Name(arg.arg)
                        ]
                    ),
                    body=[
                        ast.Assign(
                            targets=[
                                ast.Subscript(
                                    value=ast.Name('params'),
                                    slice=ast.Constant(f'"{parameter.name}"')
                                )
                            ],
                            value=ast.Name(arg.arg)
                        )
                    ]
                )
            )

        function.body.append(
            ast.Return(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name('self'),
                        attr='_send_command',
                    ),
                    args=[
                        ast.Constant(f'"{domain.domain}.{command.name}"'),
                        ast.Name('params')
                    ]
                )
            )
        )

        class_.body.append(function)

    root.body.append(class_)

    return root
