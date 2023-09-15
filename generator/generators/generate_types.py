import ast
from collections import defaultdict
from dataclasses import dataclass

from generator.types import Domain, Type, Command
from generator.utils import cdp_to_python_type


def _generate_dataclass_import(domain: Domain):
    should_generate = False

    if domain.commands:
        should_generate = True

    else:
        for type_ in domain.types:
            if type_.properties:
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


def _generate_typing_imports(domain: Domain):
    # TODO: Check first before adding type checking flag
    imports = [ast.ImportFrom(
        module='typing',
        names=[
            ast.alias('TYPE_CHECKING')
        ]
    )]

    if import_ := _generate_literal_t_import(domain):
        imports.append(import_)

    if import_ := _generate_any_t_import(domain):
        imports.append(import_)

    return imports


def _generate_literal_t_import(domain: Domain):
    should_generate = False

    for type_ in domain.types:
        if type_.enum:
            should_generate = True
            break

    if not should_generate:
        return

    return ast.ImportFrom(
        module='typing',
        names=[
            ast.alias('Literal'),
        ]
    )


def _generate_any_t_import(domain: Domain):
    return ast.ImportFrom(
        module='typing',
        names=[
            ast.alias('Any'),
        ]
    )


def _generate_external_type_imports(domain: Domain):
    import_tree = defaultdict(set)

    for type_ in domain.types:
        for ref in type_.get_refs():
            if ref.domain and ref.domain != domain.domain:
                module_name = ref.domain_snake_case or domain.domain_snake_case
                import_tree[module_name].add(
                    ref.type
                )

    for command in domain.commands:
        for ref in command.get_refs():
            if ref.domain and ref.domain != domain.domain:
                module_name = ref.domain_snake_case or domain.domain_snake_case
                import_tree[module_name].add(
                    ref.type
                )

    imports = []

    for domain, types in import_tree.items():
        types = sorted(types)

        imports.append(
            ast.ImportFrom(
                module=f'cdp.domains.{domain}.types',
                names=[
                    ast.alias(type_) for type_ in types
                ]
            )
        )

    return imports


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
                kind='str'
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
        value=value
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
                        kind='str'
                    ) for enum in type_.enum
                ],
                ctx=ast.Load()
            )
        )
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
        bases=[]
    )

    for property_ in type_.properties:
        if property_.ref:
            annotation = ast.Constant(
                value=property_.ref.type,
                kind='str'
            )

        else:
            annotation = ast.Name(
                id=cdp_to_python_type(property_.type),
                ctx=ast.Load()
            )

        class_.body.append(
            ast.AnnAssign(
                target=ast.Name(
                    id=property_.name_snake_cased,
                    ctx=ast.Store()
                ),
                annotation=annotation,
                value=None,
                simple=1
            )
        )

    class_.body.extend([
        _generate_dataclass_to_camel_json_method(type_),
        _generate_dataclass_to_snake_json_method(type_),
        _generate_dataclass_to_pascal_json_method(type_),
        _generate_dataclass_to_json_method(type_)
    ])

    return class_


def _generate_return_type_definition(command: Command):
    if not command.returns:
        return

    class_ = ast.ClassDef(
        name=command.name_pascal_case + 'ReturnT',
        decorator_list=[
            ast.Name(
                id='dataclass',
                ctx=ast.Load()
            )
        ],
        body=[],
        bases=[]
    )

    for return_ in command.returns:
        if return_.ref:
            annotation = ast.Constant(
                value=return_.ref.type,
                kind='str'
            )

        else:
            annotation = ast.Name(
                id=cdp_to_python_type(return_.type),
                ctx=ast.Load()
            )

        class_.body.append(
            ast.AnnAssign(
                target=ast.Name(
                    id=return_.name_snake_cased,
                    ctx=ast.Store()
                ),
                annotation=annotation,
                value=None,
                simple=1
            )
        )

    return class_


def _generate_dataclass_to_json_method(type_: 'Type'):
    root = ast.FunctionDef(
        name='to_json',
        args=ast.arguments(
            args=[
                ast.arg('self'),
                ast.arg(
                    arg='casing_strategy',
                    annotation=ast.Subscript(
                        value=ast.Name(
                            id='Literal',
                            ctx=ast.Load()
                        ),
                        slice=ast.Tuple(
                            elts=[
                                ast.Constant('snake'),
                                ast.Constant('camel'),
                                ast.Constant('pascal')
                            ],
                            ctx=ast.Load()
                        )
                    )
                )
            ],
            defaults=[
                ast.Constant('snake')
            ]
        )
    )


def _generate_dataclass_from_json_method(type_: 'Type'):
    return ast.FunctionDef()


def generate(domain: Domain):
    root = ast.Module(
        body=[]
    )

    if import_ := _generate_dataclass_import(domain):
        root.body.append(import_)

    if imports := _generate_typing_imports(domain):
        root.body += imports

    if imports := _generate_external_type_imports(domain):
        if_type_checking = ast.If(
            test=ast.Name(
                id='TYPE_CHECKING',
                ctx=ast.Load()
            ),
            body=imports
        )

        root.body.append(if_type_checking)

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
