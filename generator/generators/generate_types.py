import ast

from generator.types import Domain
from generator.utils import convert_to_python_type


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
                module='typing',
                names=[
                    ast.alias('Literal')
                ]
            )
        ]
    )

    string_literals = []
    dataclasses = []

    types_ = sorted(domain.types, key=lambda t: t.id)

    for type_ in types_:
        if type_.enum:
            assign = ast.Assign(
                targets=[
                    ast.Name(
                        id=type_.id,
                        ctx=ast.Store()
                    )
                ],
                value=ast.Subscript(
                    value=ast.Name(
                        id='Literal',
                        ctx=ast.Load()
                    ),
                    slice=ast.Tuple(
                        elts=[],
                        ctx=ast.Load()
                    )
                )
            )

            for enum in type_.enum:
                assign.value.slice.elts.append(
                    ast.Constant(
                        value=enum,
                        kind='str'
                    )
                )

            string_literals.append(assign)

        if type_.properties:
            if type_.type != 'object':
                print('Warning: type has properties but is not an object')
                continue

            class_ = ast.ClassDef(
                name=type_.id,
                decorator_list=[
                    ast.Name(
                        id='dataclass',
                        ctx=ast.Load()
                    )
                ],
                body=[],
                bases=[]
            )

            for property_ in type_.properties:
                class_.body.append(
                    ast.AnnAssign(
                        target=ast.Name(
                            id=property_.name,
                            ctx=ast.Store()
                        ),
                        annotation=ast.Name(
                            id=convert_to_python_type(property_.type or property_.ref.type),
                            ctx=ast.Load()
                        ),
                    )
                )

            dataclasses.append(class_)

    root.body += string_literals
    root.body += dataclasses

    return root
