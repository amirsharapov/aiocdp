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
                ast.alias('Literal'),
            ]
        ),
        ast.ImportFrom(
            module='cdp.connection.connection',
            names=[
                ast.alias('Connection')
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
            module='cdp.types',
            names=aliases
        )
    ]


def _io(domains: Iterable['Domain']):
    root = ast.ClassDef(
        name='IO',
        body=[
            ast.AnnAssign(
                target=ast.Name('connection'),
                annotation=ast.Constant('Connection'),
            ),
            ast.AnnAssign(
                target=ast.Name('session_id'),
                annotation=ast.Constant('Optional[str]'),
            )
        ],
        decorator_list=[
            ast.Name('dataclass')
        ],
        render_context={
            'lines_before': 2,
        }
    )

    for domain in domains:
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

            if command.parameters:
                method = ast.AsyncFunctionDef(
                    name='send',
                    args=ast.arguments(
                        args=[
                            ast.arg('self'),
                            ast.arg(
                                arg='method',
                                annotation=ast.Subscript(
                                    value=ast.Name('Literal'),
                                    slice=ast.Index(
                                        value=ast.Constant(
                                            domain.domain + '.' +
                                            command.name
                                        )
                                    )
                                )
                            ),
                            ast.arg(
                                arg='params',
                                # annotation=ast.Name(f'{domain.domain.snake_case}.{command.name.pascal_case}ParamsT')
                                annotation=ast.Name('dict')
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
                    method
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

    root.body.append(
        _io(domains)
    )

    return root
