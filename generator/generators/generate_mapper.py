import ast
from collections import defaultdict
from dataclasses import dataclass

from generator.types import Protocol, Type, Domain


def _generate_imports(protocols: list[Protocol]):
    import_tree = defaultdict(set)

    for protocol in protocols:
        for domain in protocol.domains:
            for type_ in domain.types:
                if type_.properties:
                    import_tree[domain.domain_snake_case].add(
                        type_.id
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


def _generate_type_specific_to_json_function(type_: 'Type'):
    if not type_.properties:
        return

    return ast.FunctionDef(
        name=f'_cast_{type_.id_snake_case}_to_json',
        args=ast.arguments(
            args=[
                ast.arg('o')
            ]
        ),
        body=[
            ast.Return(
                value=ast.Dict(
                    keys=[
                        ast.Constant(property_.name) for
                        property_ in
                        type_.properties
                    ],
                    values=[
                        ast.Attribute(
                            value=ast.Name(
                                id='o',
                                ctx=ast.Load()
                            ),
                            attr=property_.name_snake_cased,
                            ctx=ast.Load()
                        ) for
                        property_ in
                        type_.properties
                    ]
                )
            )
        ],
        decorator_list=[]
    )


def _generate_generic_to_json_function(protocols: list[Protocol]):
    lookup = ast.Dict(
        keys=[],
        values=[]
    )

    for protocol in protocols:
        for domain in protocol.domains:
            for type_ in domain.types:
                if type_.properties:
                    lookup.keys.append(
                        ast.Name(type_.id)
                    )
                    lookup.values.append(
                        ast.Name(
                            id=f'_cast_{type_.id_snake_case}_to_json',
                            ctx=ast.Load()
                        )
                    )

    return ast.FunctionDef(
        name='to_json',
        args=ast.arguments(
            args=[
                ast.arg('o')
            ]
        ),
        body=[
            ast.Assign(
                targets=[
                    ast.Name(
                        id='lookup',
                        ctx=ast.Store()
                    )
                ],
                value=lookup
            )
        ],
        decorator_list=[]
    )


def generate(protocols: list[Protocol]):
    root = ast.Module(
        body=[]
    )

    if imports := _generate_imports(protocols):
        root.body.extend(imports)

    for protocol in protocols:
        for domain in protocol.domains:
            for type_ in domain.types:
                if definition := _generate_type_specific_to_json_function(type_):
                    root.body.append(definition)

    root.body.append(
        _generate_generic_to_json_function(
            protocols=protocols
        )
    )

    return root
