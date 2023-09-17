import ast

from generator.parser.types import Protocol, Type, Command


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
            value=ast.Call(
                func=ast.Name('TypeVar'),
                args=[
                    ast.Constant('_T')
                ]
            ),
            render_context={
                'lines_before': 1
            }
        )
    ]


def _generate_return_type_from_dict_mapper_body(
        command: 'Command',
        casing_strategy: str
):
    assert casing_strategy in ('snake', 'camel', 'pascal')

    root = ast.Call(
        func=ast.Name((
            f'{command.actual_domain.domain_snake_case_collision_safe}.'
            f'{command.name_pascal_case}ReturnT'
        )),
        args=[],
        keywords=[],
        render_context={
            'expand': True
        }
    )

    for return_property in command.returns:
        key = None

        if casing_strategy == 'snake':
            key = return_property.name_snake_cased

        if casing_strategy == 'camel':
            key = return_property.name_camel_cased

        if casing_strategy == 'pascal':
            key = return_property.name_pascal_cased

        if return_property.optional:
            key_access = ast.Call(
                func=ast.Attribute(
                    value=ast.Name('data'),
                    attr='get'
                ),
                args=[
                    ast.Constant(key),
                    ast.Constant([]) if return_property.type == 'array' else ast.Constant(None)
                ]
            )

        else:
            key_access = ast.Subscript(
                value=ast.Name('data'),
                slice=ast.Constant(key)
            )

        if return_property.type == 'array':
            if return_property.items.ref.actual_type.properties:
                value = ast.ListComp(
                    elt=ast.Call(
                        func=ast.Name('from_dict'),
                        args=[
                            ast.Name(
                                f'{command.actual_domain.domain_snake_case_collision_safe}.'
                                f'{return_property.items.ref.actual_type.id_pascal_case}'
                            ),
                            ast.Name('item'),
                            ast.Name('casing_strategy')
                        ]
                    ),
                    generators=[
                        ast.comprehension(
                            target=ast.Name('item'),
                            iter=key_access,
                            ifs=[]
                        )
                    ]
                )
            else:
                value = key_access

        else:
            if return_property.ref.actual_type.properties:
                value = ast.Call(
                    func=ast.Name('from_dict'),
                    args=[
                        ast.Name((
                            f'{command.actual_domain.domain_snake_case_collision_safe}.'
                            f'{return_property.ref.actual_type.id_pascal_case}'
                        )),
                        key_access,
                        ast.Name('casing_strategy')
                    ],
                    render_context={
                        'expand': True
                    }
                )
            else:
                value = key_access

        keyword = ast.keyword(
            arg=return_property.name_snake_cased,
            value=value
        )

        root.keywords.append(keyword)

    return root


def _generate_return_type_from_dict_mappers(protocols: list['Protocol']):
    functions = []

    for protocol in protocols:
        for domain in protocol.domains:
            for command in domain.commands:
                if not command.returns:
                    continue

                function = ast.FunctionDef(
                    name=f'_{domain.domain_snake_case}__{command.name_snake_case}_return_t__from_dict',
                    args=ast.arguments(
                        args=[
                            ast.arg(
                                arg='data',
                                annotation=ast.Name('dict')
                            ),
                            ast.arg(
                                arg='casing_strategy',
                                annotation=ast.Constant('CasingStrategyT')
                            )
                        ],
                        defaults=[
                            ast.Constant('snake')
                        ],
                        render_context={
                            'expand': True
                        }
                    ),
                    body=[],
                    returns=ast.Constant((
                        f'{command.actual_domain.domain_snake_case_collision_safe}.'
                        f'{command.name_pascal_case}ReturnT'
                    )),
                    render_context={
                        'lines_before': 2
                    }
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
                                    value=_generate_return_type_from_dict_mapper_body(
                                        command,
                                        casing_strategy
                                    )
                                )
                            ],
                            render_context={
                                'lines_before': 1
                            }
                        )
                    )

                function.body.append(
                    ast.Raise(
                        exc=ast.Call(
                            func=ast.Name('NotImplementedError'),
                            args=[
                                ast.Constant('Unknown casing strategy')
                            ],
                            render_context={
                                'expand': True
                            }
                        ),
                        render_context={
                            'lines_before': 1
                        }
                    )
                )

                functions.append(
                    function
                )

    return functions


def _generate_type_specific_from_dict_mapper_body(
        type_: 'Type',
        casing_strategy: str
):
    assert casing_strategy in ('snake', 'camel', 'pascal')

    root = ast.Call(
        func=ast.Name((
            f'{type_.actual_domain.domain_snake_case_collision_safe}.'
            f'{type_.id_pascal_case}'
        )),
        args=[],
        keywords=[],
        render_context={
            'expand': True
        }
    )

    for property_ in type_.properties:
        key = None

        if casing_strategy == 'snake':
            key = property_.name_snake_cased

        if casing_strategy == 'camel':
            key = property_.name_camel_cased

        if casing_strategy == 'pascal':
            key = property_.name_pascal_cased

        if property_.optional:
            key_access = ast.Call(
                func=ast.Attribute(
                    value=ast.Name('data'),
                    attr='get'
                ),
                args=[
                    ast.Constant(key),
                    ast.Constant([]) if property_.type == 'array' else ast.Constant(None)
                ]
            )

        else:
            key_access = ast.Subscript(
                value=ast.Name('data'),
                slice=ast.Constant(key)
            )

        if property_.type == 'array':
            if property_.items.ref.actual_type.properties:
                value = ast.ListComp(
                    elt=ast.Call(
                        func=ast.Name('from_dict'),
                        args=[
                            ast.Name((
                                f'{property_.parent.actual_domain.domain_snake_case_collision_safe}.'
                                f'{property_.items.ref.actual_type.id_pascal_case}'
                            )),
                            ast.Name('item'),
                            ast.Name('casing_strategy')
                        ]
                    ),
                    generators=[
                        ast.comprehension(
                            target=ast.Name('item'),
                            iter=key_access,
                            ifs=[]
                        )
                    ]
                )
            else:
                value = key_access

        else:
            if property_.ref.actual_type.properties:
                value = ast.Call(
                    func=ast.Name('from_dict'),
                    args=[
                        ast.Name((
                            f'{property_.parent.actual_domain.domain_snake_case_collision_safe}.'
                            f'{property_.ref.actual_type.id_pascal_case}'
                        )),
                        key_access,
                        ast.Name('casing_strategy')
                    ],
                    render_context={
                        'expand': True
                    }
                )
            else:
                value = key_access

        keyword = ast.keyword(
            arg=property_.name_snake_cased,
            value=value
        )

        root.keywords.append(keyword)

    return root


def _generate_type_specific_from_dict_mappers(protocols: list['Protocol']):
    functions = []

    for protocol in protocols:
        for domain in protocol.domains:
            for type_ in domain.types:
                if not type_.properties:
                    continue

                function = ast.FunctionDef(
                    name=f'_{domain.domain_snake_case}__{type_.id_snake_case}__from_dict',
                    args=ast.arguments(
                        args=[
                            ast.arg(
                                arg='data',
                                annotation=ast.Name('dict')
                            ),
                            ast.arg(
                                arg='casing_strategy',
                                annotation=ast.Constant('CasingStrategyT')
                            )
                        ],
                        defaults=[
                            ast.Constant('snake')
                        ],
                        render_context={
                            'expand': True
                        }
                    ),
                    body=[],
                    returns=ast.Constant((
                        f'{type_.actual_domain.domain_snake_case_collision_safe}.'
                        f'{type_.id_pascal_case}'
                    )),
                    render_context={
                        'lines_before': 2
                    }
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
                                    value=_generate_type_specific_from_dict_mapper_body(
                                        type_,
                                        casing_strategy
                                    )
                                )
                            ],
                            render_context={
                                'lines_before': 1
                            }
                        )
                    )

                function.body.append(
                    ast.Raise(
                        exc=ast.Call(
                            func=ast.Name('NotImplementedError'),
                            args=[
                                ast.Constant('Unknown casing strategy')
                            ],
                            render_context={
                                'expand': True
                            }
                        ),
                        render_context={
                            'lines_before': 1
                        }
                    )
                )

                functions.append(
                    function
                )

    return functions


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
            ],
            render_context={
                'expand': True
            }
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
                root.values.append(attribute_access)

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
                    name=f'_{domain.domain_snake_case}__{type_.id_snake_case}__to_dict',
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
                        ],
                        render_context={
                            'expand': True
                        }
                    ),
                    body=[],
                    returns=ast.Name(
                        id='dict'
                    ),
                    render_context={
                        'lines_before': 2
                    }
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
                            ],
                            render_context={
                                'lines_before': 1
                            }
                        )
                    )

                function.body.append(
                    ast.Raise(
                        exc=ast.Call(
                            func=ast.Name('NotImplementedError'),
                            args=[
                                ast.Constant('Unknown casing strategy')
                            ],
                            render_context={
                                'expand': True
                            }
                        ),
                        render_context={
                            'lines_before': 1
                        }
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
            render_context={
                'expand': True
            }
        ),
        defaults=[
            ast.Constant(
                value='snake'
            )
        ],
        body=[],
        returns=ast.Name('dict'),
        render_context={
            'lines_before': 2
        }
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
                        f'_{domain.domain_snake_case}__{type_.id_snake_case}__to_dict'
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
                    slice=ast.Call(
                        func=ast.Name(
                            id='type',
                            ctx=ast.Load()
                        ),
                        args=[
                            ast.Name('data')
                        ]
                    )
                ),
                args=[
                    ast.Name('data'),
                    ast.Name('casing_strategy')
                ],
                render_context={
                    'expand': True
                }
            ),
        )
    )

    return function


def _generate_generic_from_dict_mapper(protocols: list['Protocol']):
    function = ast.FunctionDef(
        name='from_dict',
        args=ast.arguments(
            args=[
                ast.arg(
                    arg='dataclass_type',
                    annotation=ast.Subscript(
                        value=ast.Name('type'),
                        slice=ast.Name('_T')
                    )
                ),
                ast.arg(
                    arg='data',
                    annotation=ast.Name('dict')
                ),
                ast.arg(
                    arg='casing_strategy',
                    annotation=ast.Name('CasingStrategyT')
                )
            ],
            render_context={
                'expand': True
            }
        ),
        body=[],
        returns=ast.Name('_T'),
        render_context={
            'lines_before': 2
        }
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
            for command in domain.commands:
                if not command.returns:
                    continue

                lookup.keys.append(
                    ast.Name((
                        f'{command.actual_domain.domain_snake_case_collision_safe}.'
                        f'{command.name_pascal_case}ReturnT'
                    ))
                )

                lookup.values.append(
                    ast.Name((
                        f'_{domain.domain_snake_case}__{command.name_snake_case}_return_t__from_dict'
                    ))
                )

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
                        f'_{domain.domain_snake_case}__{type_.id_snake_case}__from_dict'
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
                ],
                render_context={
                    'expand': True
                }
            ),
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
        _generate_type_constants()
    )

    root.body.extend(
        _generate_type_specific_to_dict_mappers(
            protocols
        )
    )

    root.body.extend(
        _generate_type_specific_from_dict_mappers(
            protocols
        )
    )

    root.body.extend(
        _generate_return_type_from_dict_mappers(
            protocols
        )
    )

    root.body.append(
        _generate_generic_to_dict_mapper(
            protocols
        )
    )

    root.body.append(
        _generate_generic_from_dict_mapper(
            protocols
        )
    )

    return root
