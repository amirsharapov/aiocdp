import ast

from generator.parser.types import Protocol, Type


def _generate_imports(protocols: list['Protocol']):
    imports = [
        ast.ImportFrom(
            module='typing',
            names=[
                ast.alias('TypeVar'),
            ]
        ),
        ast.ImportFrom(
            module='cdp.domains.utils',
            names=[
                ast.alias('CasingStrategyT')
            ]
        )
    ]

    for protocol in protocols:
        for domain in protocol.domains:
            imports.append(
                ast.ImportFrom(
                    module=f'cdp.domains.{domain.domain_snake_case}',
                    names=[
                        ast.alias(
                            name='types',
                            asname=f'{domain.domain_snake_case_collision_safe}'
                        )
                    ]
                )
            )

    return imports


def _generate_type_constants():
    return [
        ast.Assign(
            targets=[
                ast.Name('_T')
            ],
            value=ast.Subscript(
                value=ast.Name('TypeVar'),
                slice=ast.Constant('_T')
            )
        )
    ]


def _generate_type_specific_to_dict_mapper_body(
        type_: 'Type',
        casing_strategy: str
):
    assert casing_strategy in ('snake', 'camel', 'pascal')

    root = ast.Dict(
        keys=[],
        values=[]
    )

    for property_ in type_.properties:
        key = None

        if casing_strategy == 'snake':
            key = property_.name_snake_cased

        if casing_strategy == 'camel':
            key = property_.name_camel_cased

        if casing_strategy == 'pascal':
            key = property_.name_pascal_cased

        root.keys.append(
            ast.Constant(
                key
            )
        )

        attribute_access = ast.Attribute(
            value=ast.Name('data'),
            attr=property_.name_snake_cased
        )

        to_dict_call = ast.Call(
            func=ast.Name('to_dict'),
            args=[
                attribute_access,
                ast.Name('casing_strategy')
            ]
        )

        attribute_access_list_comp = ast.ListComp(
            elt=ast.Name('item'),
            generators=[
                ast.comprehension(
                    target=ast.Name('item'),
                    iter=attribute_access,
                    ifs=[]
                )
            ]
        )

        to_dict_call_list_comp = ast.ListComp(
            elt=ast.Call(
                func=ast.Name('to_dict'),
                args=[
                    ast.Name('item'),
                    ast.Name('casing_strategy')
                ]
            ),
            generators=[
                ast.comprehension(
                    target=ast.Name('item'),
                    iter=attribute_access,
                    ifs=[]
                )
            ]
        )

        if property_.type == 'array':
            if property_.items.ref.actual_type.properties:
                root.values.append(to_dict_call_list_comp)
            else:
                root.values.append(attribute_access_list_comp)

        else:
            if property_.ref.actual_type.properties:
                root.values.append(to_dict_call)
            else:
                root.values.append(attribute_access)

    return root


def _generate_type_specific_to_dict_mappers(protocols: list['Protocol']):
    functions = []

    for protocol in protocols:
        for domain in protocol.domains:
            for type_ in domain.types:
                if not type_.properties:
                    continue

                function = ast.FunctionDef(
                    name=f'_map_{domain.domain_snake_case}__{type_.id_snake_case}__to_dict',
                    args=ast.arguments(
                        args=[
                            ast.arg(
                                arg='data',
                                annotation=ast.Constant((
                                    f'{type_.actual_domain.domain_snake_case_collision_safe}.'
                                    f'{type_.id_pascal_case}'
                                ))
                            ),
                            ast.arg(
                                arg='casing_strategy',
                                annotation=ast.Constant(
                                    value='CasingStrategyT'
                                )
                            )
                        ],
                        defaults=[
                            ast.Constant(
                                value='snake'
                            )
                        ]
                    ),
                    body=[],
                    returns=ast.Name(
                        id='dict'
                    )
                )

                for casing_strategy in ['snake', 'camel', 'pascal']:
                    function.body.append(
                        ast.If(
                            test=ast.Compare(
                                left=ast.Name('casing_strategy'),
                                ops=[
                                    ast.Eq()
                                ],
                                comparators=[
                                    ast.Constant(casing_strategy)
                                ]
                            ),
                            body=[
                                ast.Return(
                                    value=_generate_type_specific_to_dict_mapper_body(
                                        type_,
                                        casing_strategy
                                    )
                                )
                            ]
                        )
                    )

                functions.append(
                    function
                )

    return functions


def _generate_generic_to_dict_mapper(protocols: list['Protocol']):
    function = ast.FunctionDef(
        name='to_dict',
        args=ast.arguments(
            args=[
                ast.arg('data'),
                ast.arg(
                    arg='casing_strategy',
                    annotation=ast.Name('CasingStrategyT')
                )
            ],
        ),
        defaults=[
            ast.Constant(
                value='snake'
            )
        ],
        body=[ast.Name('pass')],
    )

    return function


def _generate_type_specific_from_dict_mappers(protocols: list['Protocol']):
    functions = []

    for protocol in protocols:
        for domain in protocol.domains:
            for type_ in domain.types:
                function = ast.FunctionDef(
                    name=f'_map_{domain.domain_snake_case}__{type_.id_snake_case}__from_dict',
                    args=ast.arguments(
                        args=[
                            ast.arg(
                                arg='data',
                                annotation=ast.Name(
                                    id='dict'
                                )
                            ),
                            ast.arg(
                                arg='casing_strategy',
                                annotation=ast.Constant(
                                    value='CasingStrategyT'
                                )
                            )
                        ],
                        defaults=[
                            ast.Constant(
                                value='snake'
                            )
                        ]
                    ),
                    body=[ast.Name('pass')],
                    returns=ast.Constant((
                        f'{type_.actual_domain.domain_snake_case_collision_safe}.'
                        f'{type_.id_pascal_case}'
                    ))
                )

                functions.append(
                    function
                )

    return functions


def _generate_generic_from_dict_mapper(protocols: list['Protocol']):
    function = ast.FunctionDef(
        name='from_dict',
        args=ast.arguments(
            args=[
                ast.arg('dataclass_type'),
                ast.arg(
                    arg='data',
                    annotation=ast.Name('dict')
                ),
                ast.arg(
                    arg='casing_strategy',
                    annotation=ast.Name('CasingStrategyT')
                )
            ]
        ),
        body=[],
    )

    lookup = ast.Dict(
        keys=[],
        values=[],
        render_context={
            'expand': True
        }
    )

    for protocol in protocols:
        for domain in protocol.domains:
            for type_ in domain.types:
                if not type_.properties:
                    continue

                lookup.keys.append(
                    ast.Name((
                        f'{domain.domain_snake_case_collision_safe}.'
                        f'{type_.id_pascal_case}'
                    ))
                )

                lookup.values.append(
                    ast.Name((
                        f'_map_{domain.domain_snake_case}__{type_.id_snake_case}__from_dict'
                    ))
                )

    function.body.append(
        ast.Assign(
            targets=[
                ast.Name(
                    id='lookup',
                    ctx=ast.Store()
                )
            ],
            value=lookup
        )
    )

    function.body.append(
        ast.Return(
            value=ast.Call(
                func=ast.Subscript(
                    value=ast.Name(
                        id='lookup',
                        ctx=ast.Load()
                    ),
                    slice=ast.Name(
                        id='dataclass_type',
                        ctx=ast.Load()
                    )
                ),
                args=[
                    ast.Name('data'),
                    ast.Name('casing_strategy')
                ]
            ),
            render_context={
                'expand': True
            }
        )
    )

    return function


def generate(protocols: list['Protocol']):
    root = ast.Module(
        body=[]
    )

    root.body.extend(
        _generate_imports(
            protocols
        )
    )

    root.body.extend(
        _generate_type_specific_to_dict_mappers(
            protocols
        )
    )

    root.body.append(
        _generate_generic_to_dict_mapper(
            protocols
        )
    )

    root.body.extend(
        _generate_type_specific_from_dict_mappers(
            protocols
        )
    )

    root.body.append(
        _generate_generic_from_dict_mapper(
            protocols
        )
    )

    return root
