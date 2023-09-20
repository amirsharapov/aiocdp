import ast

from generator.parser.types import Domain, Type, Command, Event
from generator.utils import cdp_to_python_type


def _type_definitions(type_: 'Type') -> 'ast.AST':
    pass


def _event_definitions(event: 'Event'):
    pass


def _command_params_object_definitions(command: 'Command'):
    pass


def _command_return_object_definitions(command: 'Command'):
    pass


def _generate_type_alias(type_: 'Type'):
    if type_.type not in ('string', 'integer', 'number', 'boolean', 'array', 'object'):
        return

    if type_.enum:
        return

    if type_.type == 'object' and type_.properties:
        return

    if type_.type == 'object':
        value = ast.Name(
            id='dict',
            ctx=ast.Load()
        )

    elif type_.type == 'array':
        inner_type = type_.items.type or type_.items.ref.type

        if type_.items.ref:
            slice_ = ast.Constant(
                value=inner_type,
            )

        else:
            slice_ = ast.Name(
                id=cdp_to_python_type(inner_type),
                ctx=ast.Load()
            )

        value = ast.Subscript(
            value=ast.Name(
                id='list',
                ctx=ast.Load()
            ),
            slice=ast.Index(
                value=slice_
            )
        )

    else:
        value = ast.Name(
            id=cdp_to_python_type(type_.type),
            ctx=ast.Load()
        )

    return ast.Assign(
        targets=[
            ast.Name(
                id=type_.id,
                ctx=ast.Store()
            )
        ],
        value=value,
        render_context={
            'lines_before': 1,
        }
    )


def _generate_string_literal(type_: 'Type'):
    if not type_.enum:
        return

    return ast.Assign(
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
                elts=[
                    ast.Constant(
                        value=enum,
                    ) for enum in type_.enum
                ],
                ctx=ast.Load()
            ),
            render_context={
                'expand': True
            }
        ),
        render_context={
            'lines_before': 1,
        }
    )


def _generate_complex_type_definitions(type_):
    if not type_.properties:
        return

    class_ = ast.ClassDef(
        name=type_.id,
        decorator_list=[
            ast.Name(
                id='dataclass',
                ctx=ast.Load()
            )
        ],
        body=[],
        bases=[],
        render_context={
            'lines_before': 2,
        }
    )

    for property_ in type_.properties:

        if property_.type == 'array':
            if property_.items.type:
                slice_ = ast.Name(
                    id=cdp_to_python_type(property_.items.type),
                    ctx=ast.Load()
                )

            else:
                slice_ = ast.Constant(
                    value=property_.items.ref.type
                )

            annotation = ast.Subscript(
                value=ast.Name(
                    id='list',
                    ctx=ast.Load()
                ),
                slice=slice_
            )

        else:
            if property_.type:
                annotation = ast.Name(
                    id=cdp_to_python_type(property_.type),
                    ctx=ast.Load()
                )

            else:
                annotation = ast.Constant(
                    value=property_.ref.type
                )

        class_.body.append(
            ast.AnnAssign(
                target=ast.Name(
                    id=property_.name_.snake_case,
                    ctx=ast.Store()
                ),
                annotation=annotation,
                value=None,
                simple=1
            )
        )

    return class_


def _generate_return_type_definition(command: Command):
    if not command.returns:
        return

    class_ = ast.ClassDef(
        name=command.return_type_name,
        decorator_list=[
            ast.Name(
                id='dataclass',
                ctx=ast.Load()
            )
        ],
        body=[],
        bases=[],
        render_context={
            'lines_before': 2,
        }
    )

    for return_ in command.returns:
        if return_.ref:
            annotation = ast.Constant(
                value=return_.ref.type,
            )

        else:
            annotation = ast.Name(
                id=cdp_to_python_type(return_.type),
                ctx=ast.Load()
            )

        class_.body.append(
            ast.AnnAssign(
                target=ast.Name(
                    id=return_.name_.snake_case,
                    ctx=ast.Store()
                ),
                annotation=annotation,
                value=None,
                simple=1
            )
        )

    return class_


def generate(domain: Domain):
    root = ast.Module(
        body=[]
    )

    if imports_ := _generate_domain_type_imports(domain):
        root.body.append(
            ast.If(
                test=ast.Name(
                    id='TYPE_CHECKING',
                    ctx=ast.Load()
                ),
                body=imports_,
                render_context={
                    'lines_before': 1
                }
            )
        )

    type_aliases = []
    string_literals = []
    complex_type_definitions = []
    return_type_definitions = []

    for type_ in domain.types:

        if type_definition := _generate_type_alias(type_):
            type_aliases.append(type_definition)

        if type_definition := _generate_complex_type_definitions(type_):
            complex_type_definitions.append(type_definition)

        if type_definition := _generate_string_literal(type_):
            string_literals.append(type_definition)

    for command in domain.commands:

        if type_definition := _generate_return_type_definition(command):
            return_type_definitions.append(type_definition)

    root.body += type_aliases
    root.body += string_literals
    root.body += complex_type_definitions
    root.body += return_type_definitions

    return root
