import ast
from typing import Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from generator.parser.types.domain import Domain


def _imports():
    return [
        ast.ImportFrom(
            module='dataclasses',
            names=[
                ast.alias('dataclass'),
                ast.alias('field')
            ],
            render_context={
                'lines_before': 2,
            }
        ),
        ast.ImportFrom(
            module='typing',
            names=[
                ast.alias('TYPE_CHECKING'),
                ast.alias('overload'),
                ast.alias('Optional')
            ]
        )
    ]


def _type_checked_imports(domains: Iterable['Domain']):
    aliases = []

    for domain in domains:
        aliases.append(
            ast.alias(
                domain.domain.snake_case
            )
        )

    return [
        ast.ImportFrom(
            module='cdp.target',
            names=[
                ast.alias(
                    name='Target',
                    asname='WSTarget'
                )
            ]
        ),
        ast.ImportFrom(
            module='cdp.connection.response',
            names=[
                ast.alias('PendingResponse')
            ]
        ),
        ast.ImportFrom(
            module='cdp.generated.types',
            names=aliases
        )
    ]


def _domain(domain: 'Domain'):
    root = ast.ClassDef(
        name=domain.domain.pascal_case,
        body=[
            ast.AnnAssign(
                target=ast.Name('domains'),
                annotation=ast.Constant('Domains'),
            )
        ],
        decorator_list=[
            ast.Name('dataclass')
        ],
        render_context={
            'lines_before': 2,
        }
    )

    for command in domain.commands:
        if command.returns:
            returns = ast.Name(
                command.domain.domain.snake_case + '.' +
                command.name.pascal_case + 'ReturnT'
            )
        else:
            returns = ast.Name(
                'None'
            )

        returns = ast.Subscript(
            value=ast.Name('PendingResponse'),
            slice=ast.Index(
                value=returns
            )
        )

        method_with_kwargs = ast.FunctionDef(
            name=command.name.snake_case,
            args=ast.arguments(
                args=[
                    ast.arg(
                        arg='self'
                    )
                ],
                defaults=[],
                render_context={
                    'expand': True,
                }
            ),
            body=[
                ast.Name('...')
            ],
            decorator_list=[
                ast.Name('overload')
            ],
            returns=returns,
            render_context={
                'lines_before': 1
            }
        )

        if command.parameters:
            method_with_kwargs.args.args.append(
                ast.arg(
                    arg='*',
                )
            )

        for parameter in command.parameters:
            annotation = ast.Name(
                parameter.type.python_type.__name__ or
                f'{parameter.ref.type.domain.domain.snake_case}.{parameter.ref.type.id}'
            )

            if parameter.optional:
                annotation = ast.Subscript(
                    value=ast.Name('Optional'),
                    slice=ast.Index(
                        value=annotation
                    )
                )

            method_with_kwargs.args.args.append(
                ast.arg(
                    arg=parameter.name.snake_case,
                    annotation=annotation
                )
            )

            if parameter.optional:
                method_with_kwargs.args.defaults.append(
                    ast.Name('...')
                )

        root.body.append(
            method_with_kwargs
        )

        if command.parameters:
            method_with_params = ast.FunctionDef(
                name=command.name.snake_case,
                args=ast.arguments(
                    args=[
                        ast.arg('self'),
                        ast.arg(
                            arg='params',
                            annotation=ast.Name(f'{domain.domain.snake_case}.{command.name.pascal_case}ParamsT')
                        )
                    ],
                    defaults=[],
                    render_context={
                        'expand': True,
                    }
                ),
                body=[
                    ast.Name('...')
                ],
                decorator_list=[
                    ast.Name('overload')
                ],
                returns=returns,
                render_context={
                    'lines_before': 1
                }
            )

            root.body.append(
                method_with_params
            )

    return root


def generate(domains: Iterable['Domain']):
    root = ast.Module(
        body=[]
    )

    root.body.extend(_imports())
    root.body.append(
        ast.If(
            test=ast.Name('TYPE_CHECKING'),
            body=_type_checked_imports(domains),
            render_context={
                'lines_before': 1,
            }
        )
    )

    domains_definition = ast.ClassDef(
        name='Domains',
        body=[],
        decorator_list=[
            ast.Name('dataclass')
        ],
        render_context={
            'lines_before': 2,
        }
    )

    for domain in domains:
        root.body.append(
            _domain(domain)
        )

        domains_definition.body.append(
            ast.AnnAssign(
                target=ast.Name(domain.domain.snake_case),
                annotation=ast.Name(domain.domain.pascal_case),
                value=ast.Call(
                    func=ast.Name('field'),
                    keywords=[
                        ast.keyword(
                            arg='init',
                            value=ast.Constant(False)
                        ),
                        ast.keyword(
                            arg='repr',
                            value=ast.Constant(False)
                        )
                    ],
                    render_context={
                        'expand': True,
                    }
                )
            )
        )

    domains_definition.body.append(
        ast.AnnAssign(
            target=ast.Name('ws_target'),
            annotation=ast.Constant('WSTarget'),
            render_context={
                'lines_before': 1
            }
        )
    )

    root.body.append(domains_definition)

    return root
