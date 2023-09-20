import ast
from typing import Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from cdp.domains.domain import Domain


def generate(domains: Iterable['Domain']):
    root = ast.Module(
        body=[
            ast.ImportFrom(
                module='typing',
                names=[
                    ast.alias('TYPE_CHECKING'),
                ]
            )
        ]
    )

    root.body.append(
        ast.If(
            test=ast.Name(
                id='TYPE_CHECKING',
                ctx=ast.Load()
            ),
            body=[
                ast.ImportFrom(
                    module='cdp.target.target',
                    names=[
                        ast.alias(
                            name='Target',
                            asname='_Target'
                        )
                    ],
                )
            ]
        )
    )

    return root
