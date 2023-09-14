import ast
from collections import defaultdict

from generator.types import Domain, Type
from generator.utils import cdp_to_python_type


def _generate_dataclass_import(domain: Domain):
    should_generate = False

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
            ast.alias('Literal')
        ]
    )


def _generate_external_type_imports(domain: Domain):
    import_tree = defaultdict(set)

    for type_ in domain.types:
        for property_ in type_.properties:
            if property_.ref.domain:
                import_tree[property_.ref.domain_snake_case].add(
                    property_.ref.type
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
    if type_.type not in ('string', 'integer', 'number', 'boolean', 'array'):
        return

    if type_.enum:
        return

    if type_.type == 'array':
        inner_type = type_.items.type or type_.items.ref.type

        if inner_type not in ('string', 'integer', 'number', 'boolean'):
            return

        value = ast.Subscript(
            value=ast.Name(
                id='list',
                ctx=ast.Load()
            ),
            slice=ast.Name(
                id=cdp_to_python_type(inner_type),
                ctx=ast.Load()
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


def _generate_dataclass_definition(type_):
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
        _generate_dataclass_from_json_method(type_),
        _generate_dataclass_to_json_method(type_)
    ])

    return class_


def _generate_dataclass_to_json_method(type_: 'Type'):
    return ast.FunctionDef()


def _generate_dataclass_from_json_method(type_: 'Type'):
    return ast.FunctionDef()


def generate(domain: Domain):
    root = ast.Module(
        body=[]
    )

    if import_ := _generate_dataclass_import(domain):
        root.body.append(import_)

    if import_ := _generate_literal_t_import(domain):
        root.body.append(import_)

    if imports := _generate_external_type_imports(domain):
        root.body += imports

    type_aliases = []
    string_literals = []
    dataclass_definitions = []

    for type_ in domain.types:
        if type_definition := _generate_type_alias(type_):
            type_aliases.append(type_definition)

        if type_definition := _generate_dataclass_definition(type_):
            dataclass_definitions.append(type_definition)

        if type_definition := _generate_string_literal(type_):
            string_literals.append(type_definition)

    root.body += type_aliases
    root.body += string_literals
    root.body += dataclass_definitions

    return root
