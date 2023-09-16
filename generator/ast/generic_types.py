import ast
from collections import defaultdict
from typing import Literal

from generator.parser.types import Domain, Type, Command
from generator.utils import cdp_to_python_type


def _generate_domain_type_imports(domain: Domain):
    import_tree = defaultdict(set)

    for type_ in domain.types:
        for ref in type_.get_refs():
            if ref.domain and ref.domain != domain.domain:
                module_name = ref.actual_domain.domain_snake_case
                import_tree[module_name].add(
                    ref.type
                )

    for command in domain.commands:
        for ref in command.get_refs():
            if ref.domain and ref.domain != domain.domain:
                module_name = ref.actual_domain.domain_snake_case
                import_tree[module_name].add(
                    ref.type
                )

    imports = []

    for module, types in import_tree.items():
        types = sorted(types)

        imports.append(
            ast.ImportFrom(
                module=f'cdp.domains.{module}.types',
                names=[
                    ast.alias(type_) for type_ in types
                ]
            )
        )

    return imports


def _generate_basic_imports(domain: Domain):
    import_tree = defaultdict(set)
    import_tree['typing'].add('TYPE_CHECKING')
    import_tree['typing'].add('Any')
    import_tree['typing'].add('Literal')

    if domain.commands:
        import_tree['dataclasses'].add('dataclass')

    for type_ in domain.types:
        if type_.properties:
            import_tree['dataclasses'].add('dataclass')

    imports = []

    for module, types in import_tree.items():
        types = sorted(types)

        imports.append(
            ast.ImportFrom(
                module=module,
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
                    ) for enum in type_.enum
                ],
                ctx=ast.Load()
            ),
            render_context={
                'expand': True
            }
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

    class_.body.append(
        _generate_dataclass_to_dict_method(type_)
    )

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


def _generate_dataclass_to_dict_body(
        type_: 'Type',
        casing_strategy: Literal['snake', 'camel', 'pascal']
):
    return_value = ast.Dict(
        keys=[],
        values=[]
    )

    for property_ in type_.properties:
        if casing_strategy == 'camel':
            key_name = property_.name_camel_cased

        elif casing_strategy == 'snake':
            key_name = property_.name_snake_cased

        elif casing_strategy == 'pascal':
            key_name = property_.name_pascal_cased

        else:
            raise NotImplementedError

        return_value.keys.append(
            ast.Constant(
                key_name,
            )
        )

        property_name = property_.name_snake_cased

        if property_.ref and property_.ref.actual_type.properties:
            value = ast.Call(
                func=ast.Attribute(
                    value=ast.Attribute(
                        value=ast.Name(
                            id='self',
                            ctx=ast.Load()
                        ),
                        attr=property_name,
                        ctx=ast.Load()
                    ),
                    attr='to_dict',
                    ctx=ast.Load()
                ),
                args=[
                    ast.Name(
                        id='casing_strategy',
                        ctx=ast.Load()
                    )
                ],
            )

        elif property_.type == 'array' and property_.items.ref:
            value = ast.ListComp(
                elt=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(
                            id='_',
                            ctx=ast.Load()
                        ),
                        attr='to_dict',
                        ctx=ast.Load()
                    ),
                    args=[
                        ast.Name(
                            id='casing_strategy',
                            ctx=ast.Load()
                        )
                    ],
                    keywords=[],
                    render_context={
                        'expand': False
                    }
                ),
                generators=[
                    ast.comprehension(
                        target=ast.Name(
                            id='_'
                        ),
                        iter=ast.Attribute(
                            value=ast.Name(
                                id='self',
                                ctx=ast.Load()
                            ),
                            attr=property_name,
                            ctx=ast.Load()
                        ),
                        ifs=[]
                    )
                ]
            )

        else:
            value = ast.Attribute(
                value=ast.Name(
                    id='self',
                    ctx=ast.Load()
                ),
                attr=property_name,
                ctx=ast.Load()
            )

        return_value.values.append(value)

    return ast.Return(
        value=return_value
    )


def _generate_dataclass_to_dict_method(type_: 'Type'):
    root = ast.FunctionDef(
        name='to_dict',
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
        ),
        body=[]
    )

    ifs = []

    for casing_strategy in ['snake', 'camel', 'pascal']:
        # noinspection PyTypeChecker
        ifs.append(
            ast.If(
                test=ast.Compare(
                    left=ast.Name(
                        id='casing_strategy',
                        ctx=ast.Load()
                    ),
                    ops=[
                        ast.Eq()
                    ],
                    comparators=[
                        ast.Constant(casing_strategy)
                    ]
                ),
                body=[
                    _generate_dataclass_to_dict_body(
                        type_,
                        casing_strategy
                    )
                ]
            )
        )

    root.body.extend(ifs)

    return root


def generate(domain: Domain):
    root = ast.Module(
        body=[]
    )

    root.body.extend(
        _generate_basic_imports(
            domain
        )
    )

    if imports_ := _generate_domain_type_imports(domain):
        root.body.append(
            ast.If(
                test=ast.Name(
                    id='TYPE_CHECKING',
                    ctx=ast.Load()
                ),
                body=imports_
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