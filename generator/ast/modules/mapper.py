import ast
from collections import defaultdict

from generator.ast.utils import ast_imports
from generator.parser.types import Domain, Type, Command


def _base_imports():
    import_tree = defaultdict(set)

    import_tree['typing'].add('TYPE_CHECKING')
    import_tree['cdp.utils'].add('is_defined')
    import_tree['cdp.domains'].add('mappers')

    return ast_imports(
        import_tree
    )


def _type_checked_imports(domain: 'Domain'):
    import_tree = defaultdict(set)

    for type_ in domain.types:
        if type_.properties:
            module = f'cdp.domains.{domain.domain_.snake_case}.types'
            import_tree[module].add(
                type_.id_.pascal_case
            )

    return ast_imports(
        import_tree
    )


def _type_to_camel_dict_map_function(type_: 'Type'):
    root = ast.FunctionDef(
        name=f'_{type_.id_.snake_case}__to_camel_dict',
        args=ast.arguments(
            args=[
                ast.arg(
                    arg='o',
                    annotation=ast.Name(type_.id_.pascal_case)
                )
            ]
        ),
        body=[],
        returns=ast.Name('dict'),
        render_context={
            'lines_before': 2
        }
    )

    ast_mapper_keys = ast.Dict(
        keys=[],
        values=[],
        render_context={
            'expand': True
        }
    )

    ast_result = ast.Dict(
        keys=[],
        values=[],
        render_context={
            'expand': True,
            'lines_before': 1
        }
    )

    ast_ifs = []

    for property_ in type_.properties_with_required_first:
        if property_.is_array_of_complex_type or property_.is_complex_type:
            ref = property_.ref or property_.items.ref

            ast_mapper_keys.keys.append(
                ast.Constant(
                    property_.name_.camel_case
                )
            )

            ast_mapper_keys.values.append(
                ast.Tuple(
                    elts=[
                        ast.Constant(
                            ref.actual_domain.domain_.snake_case + '.' +
                            ref.type
                        ),
                        ast.Constant('to_dict'),
                        ast.Constant('camel')
                    ],
                    render_context={
                        'expand': True
                    }
                )
            )

        ast_result_value = ast.Attribute(
            value=ast.Name('o'),
            attr=property_.name_.snake_case
        )

        if property_.is_array_of_complex_type:
            ast_result_value = ast.Call(
                func=ast.Name('list'),
                args=[
                    ast.Call(
                        func=ast.Name('map'),
                        args=[
                            ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name('mappers'),
                                    attr='get_mapper'
                                ),
                                args=[
                                    ast.Subscript(
                                        value=ast.Name('mapper_keys'),
                                        slice=ast.Constant(property_.name_.camel_case)
                                    )
                                ]
                            ),
                            ast.Attribute(
                                value=ast.Name('o'),
                                attr=property_.name_.snake_case
                            )
                        ],
                        render_context={
                            'expand': True
                        }
                    )
                ],
                render_context={
                    'expand': True
                }
            )

        if property_.is_complex_type:
            ast_result_value = ast.Call(
                func=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name('mappers'),
                        attr='get_mapper'
                    ),
                    args=[
                        ast.Subscript(
                            value=ast.Name('mapper_keys'),
                            slice=ast.Constant(property_.name_.camel_case)
                        )
                    ]
                ),
                args=[
                    ast.Attribute(
                        value=ast.Name('o'),
                        attr=property_.name_.snake_case
                    )
                ],
                render_context={
                    'expand': True
                }
            )

        if property_.optional:
            ast_ifs.append(
                ast.If(
                    test=ast.Call(
                        func=ast.Name('is_defined'),
                        args=[
                            ast.Attribute(
                                value=ast.Name('o'),
                                attr=property_.name_.snake_case
                            )
                        ]
                    ),
                    body=[
                        ast.Assign(
                            targets=[
                                ast.Subscript(
                                    value=ast.Name('result'),
                                    slice=ast.Constant(property_.name_.camel_case)
                                )
                            ],
                            value=ast_result_value
                        )
                    ],
                    render_context={
                        'lines_before': 1
                    }
                )
            )

        else:
            ast_result.keys.append(
                ast.Constant(
                    property_.name_.camel_case
                )
            )

            ast_result.values.append(
                ast_result_value
            )

    root.body.extend([
        ast.Assign(
            targets=[
                ast.Name('mapper_keys'),
            ],
            value=ast_mapper_keys
        ),
        ast.Assign(
            targets=[
                ast.Name('result'),
            ],
            value=ast_result
        ),
        *ast_ifs,
        ast.Return(
            value=ast.Name('result'),
            render_context={
                'lines_before': 1
            }
        )
    ])

    return root


def _type_to_snake_dict_map_function(type_: 'Type') -> ast.FunctionDef:
    pass


def _type_from_camel_dict_map_function(type_: 'Type') -> ast.FunctionDef:
    pass


def _type_from_snake_dict_map_function(type_: 'Type') -> ast.FunctionDef:
    pass


def _command_return_t_to_camel_dict_map_function(command: 'Command') -> ast.FunctionDef:
    pass


def _command_return_t_to_snake_dict_map_function(command: 'Command') -> ast.FunctionDef:
    pass


def _command_return_t_from_camel_dict_map_function(command: 'Command') -> ast.FunctionDef:
    pass


def _command_return_t_from_snake_dict_map_function(command: 'Command') -> ast.FunctionDef:
    pass


def generate(domain: 'Domain'):
    root = ast.Module(
        body=[
            *_base_imports(),
            ast.If(
                test=ast.Name('TYPE_CHECKING'),
                body=_type_checked_imports(domain)
            )
        ]
    )

    for type_ in domain.types:
        if type_.properties:
            root.body.append(
                _type_to_camel_dict_map_function(type_)
            )

    for command in domain.commands:
        root.body.extend([
        ])

    return root
