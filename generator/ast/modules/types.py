import ast
from collections import defaultdict

from generator.parser.types import Domain


def _should_import_typed_dict(domain: 'Domain'):
    for type_ in domain.types:
        if type_.type == 'object':
            return True

    for command in domain.commands:
        if command.returns:
            return True

        if command.parameters:
            return True

    for event in domain.events:
        if event.parameters:
            return True

    return False


def _should_import_string_literal(domain: 'Domain'):
    if domain.events:
        return True

    for type_ in domain.types:
        if type_.enum:
            return True

    return False


def _should_import_any(domain: 'Domain'):
    for type_ in domain.types:
        if type_.type == 'any':
            return True

        if type_.properties:
            for property_ in type_.properties:
                if property_.type == 'any':
                    return True

    return False


def _imports(domain: 'Domain'):
    import_tree = defaultdict(set)

    import_typed_dict = _should_import_typed_dict(
        domain
    )
    import_string_literal = _should_import_string_literal(
        domain
    )
    import_any = _should_import_any(
        domain
    )

    if import_typed_dict:
        import_tree['typing'].add('TypedDict')

    if import_string_literal:
        import_tree['typing'].add('Literal')

    if import_any:
        import_tree['typing'].add('Any')

    for ref in domain.get_refs():
        if ref.type.domain is not domain:
            import_tree['cdp.types'].add(ref.type.domain.domain.snake_case)

    modules = sorted(import_tree.keys())

    for module in modules:
        aliases = sorted(import_tree[module])

        yield ast.ImportFrom(
            module=module,
            names=[
                ast.alias(alias) for
                alias in
                aliases
            ]
        )


def _string_literal_definitions(domain: 'Domain'):
    for type_ in domain.types:
        if type_.enum:
            yield ast.Assign(
                targets=[
                    ast.Name(type_.id)
                ],
                value=ast.Subscript(
                    value=ast.Name('Literal'),
                    slice=ast.Tuple(
                        elts=[
                            ast.Str(enum) for
                            enum in
                            type_.enum
                        ]
                    ),
                    render_context={
                        'expand': True,
                    }
                ),
                render_context={
                    'lines_before': 1
                }
            )


def _primitive_type_definitions(domain: 'Domain'):
    for type_ in domain.types:
        if type_.properties or type_.enum:
            continue

        yield ast.Assign(
            targets=[
                ast.Name(type_.id)
            ],
            value=ast.Name(type_.type.python_type.__name__),
            render_context={
                'lines_before': 1
            }
        )


def _complex_type_definitions(domain: 'Domain'):
    for type_ in domain.types:
        if not type_.properties:
            continue

        root = ast.ClassDef(
            name=type_.id.pascal_case,
            bases=[
                ast.Name('TypedDict')
            ],
            body=[],
            render_context={
                'lines_before': 2
            }
        )

        for property_ in type_.properties:
            if property_.ref:
                if property_.ref.type.domain is not domain:
                    annotation = ast.Constant(
                        property_.ref.type.domain.domain.snake_case + '.' +
                        property_.ref.type.id.pascal_case
                    )
                else:
                    annotation = ast.Constant(
                        property_.ref.type.id.pascal_case
                    )

                root.body.append(
                    ast.AnnAssign(
                        target=ast.Name(property_.name.snake_case),
                        annotation=annotation
                    )
                )

            else:
                root.body.append(
                    ast.AnnAssign(
                        target=ast.Name(property_.name.snake_case),
                        annotation=ast.Name(property_.type.python_type.__name__),
                        simple=1
                    )
                )

        yield root


def _command_params_object_definitions(domain: 'Domain'):
    for command in domain.commands:
        if not command.parameters:
            continue

        root = ast.ClassDef(
            name=command.name.pascal_case + 'ParamsT',
            bases=[
                ast.Name('TypedDict')
            ],
            body=[],
            render_context={
                'lines_before': 2
            }
        )

        for parameter in command.parameters:
            if parameter.ref:
                if parameter.ref.type.domain is not domain:
                    annotation = ast.Constant(
                        parameter.ref.type.domain.domain.snake_case + '.' +
                        parameter.ref.type.id.pascal_case
                    )
                else:
                    annotation = ast.Constant(
                        parameter.ref.type.id.pascal_case
                    )

                root.body.append(
                    ast.AnnAssign(
                        target=ast.Name(parameter.name.snake_case),
                        annotation=annotation
                    )
                )

            else:
                root.body.append(
                    ast.AnnAssign(
                        target=ast.Name(parameter.name.snake_case),
                        annotation=ast.Name(parameter.type.python_type.__name__),
                        simple=1
                    )
                )

        yield root


def _command_return_object_definitions(domain: 'Domain'):
    for command in domain.commands:
        if not command.returns:
            continue

        root = ast.ClassDef(
            name=command.name.pascal_case + 'ReturnT',
            bases=[
                ast.Name('TypedDict')
            ],
            body=[],
            render_context={
                'lines_before': 2
            }
        )

        for return_ in command.returns:
            if return_.ref:
                if return_.ref.type.domain is not domain:
                    annotation = ast.Constant(
                        return_.ref.type.domain.domain.snake_case + '.' +
                        return_.ref.type.id.pascal_case
                    )
                else:
                    annotation = ast.Constant(
                        return_.ref.type.id.pascal_case
                    )

                root.body.append(
                    ast.AnnAssign(
                        target=ast.Name(return_.name.snake_case),
                        annotation=annotation
                    )
                )

            else:
                root.body.append(
                    ast.AnnAssign(
                        target=ast.Name(return_.name.snake_case),
                        annotation=ast.Name(return_.type.python_type.__name__),
                        simple=1
                    )
                )

        yield root


def _event_definitions(domain: 'Domain'):
    for event in domain.events:
        yield ast.ClassDef(
            name=event.name.pascal_case + 'EventT',
            bases=[
                ast.Name('TypedDict')
            ],
            body=[
                ast.AnnAssign(
                    target=ast.Name('name'),
                    annotation=ast.Subscript(
                        value=ast.Name('Literal'),
                        slice=ast.Tuple(
                            elts=[
                                ast.Str(event.name.snake_case)
                            ]
                        )
                    )
                ),
                ast.AnnAssign(
                    target=ast.Name('params'),
                    annotation=(
                        ast.Constant(event.name.pascal_case + 'ParamsT') if
                        event.parameters else
                        ast.Constant(None)
                    )
                )
            ],
            render_context={
                'lines_before': 2
            }
        )


def _event_params_definitions(domain: 'Domain'):
    for event in domain.events:
        if not event.parameters:
            continue

        root = ast.ClassDef(
            name=event.name.pascal_case + 'ParamsT',
            bases=[
                ast.Name('TypedDict')
            ],
            body=[],
            render_context={
                'lines_before': 2
            }
        )

        for parameter in event.parameters:
            if parameter.ref:
                if parameter.ref.type.domain is not domain:
                    annotation = ast.Constant(
                        parameter.ref.type.domain.domain.snake_case + '.' +
                        parameter.ref.type.id.pascal_case
                    )
                else:
                    annotation = ast.Constant(
                        parameter.ref.type.id.pascal_case
                    )

                root.body.append(
                    ast.AnnAssign(
                        target=ast.Name(parameter.name.snake_case),
                        annotation=annotation
                    )
                )

            else:
                root.body.append(
                    ast.AnnAssign(
                        target=ast.Name(parameter.name.snake_case),
                        annotation=ast.Name(parameter.type.python_type.__name__),
                        simple=1
                    )
                )

        yield root


def generate(domain: Domain):
    root = ast.Module(
        body=[]
    )

    root.body += _imports(domain)
    root.body += _primitive_type_definitions(domain)
    root.body += _string_literal_definitions(domain)
    root.body += _complex_type_definitions(domain)
    root.body += _command_params_object_definitions(domain)
    root.body += _command_return_object_definitions(domain)
    root.body += _event_definitions(domain)
    root.body += _event_params_definitions(domain)

    return root
