import ast
from typing import Iterable

from generator.parser.types import Domain


def assign_dict_key_value(dict_: ast.Dict, key: str | tuple, value: str):
    if isinstance(key, str):
        key = ast.Constant(
            key
        )

    else:
        key = ast.Tuple(
            elts=[
                ast.Constant(part) for
                part in
                key
            ],
            render_context={
                'include_parentheses': True
            }
        )

    dict_.keys.append(key)
    dict_.values.append(
        ast.Constant(
            value=value
        )
    )


def _domain_names(domains: Iterable['Domain']):
    snake_to_pascal = ast.Dict(
        keys=[],
        values=[],
        render_context={
            'expand': True,
        }
    )

    for domain in domains:
        assign_dict_key_value(
            snake_to_pascal,
            domain.domain.snake_case,
            domain.domain.pascal_case
        )

    return ast.Assign(
        targets=[ast.Name('domain_names')],
        value=ast.Dict(
            keys=[ast.Constant('snake:pascal')],
            values=[snake_to_pascal]
        ),
        render_context={
            'lines_before': 2,
        }
    )


def _type_properties(domains: Iterable['Domain']):
    snake_to_camel = ast.Dict(
        keys=[],
        values=[],
        render_context={
            'expand': True,
        }
    )

    camel_to_snake = ast.Dict(
        keys=[],
        values=[],
        render_context={
            'expand': True,
        }
    )

    for domain in domains:
        for type_ in domain.types:
            assign_dict_key_value(
                snake_to_camel,
                (domain.domain.snake_case, type_.id.snake_case),
                type_.id.camel_case
            )
            assign_dict_key_value(
                camel_to_snake,
                (domain.domain.camel_case, type_.id.camel_case),
                type_.id.snake_case
            )

    return ast.Assign(
        targets=[ast.Name('type_properties')],
        value=ast.Dict(
            keys=[
                ast.Constant('snake:camel'),
                ast.Constant('camel:snake')
            ],
            values=[
                snake_to_camel,
                camel_to_snake
            ]
        ),
        render_context={
            'lines_before': 2,
        }
    )


def _command_names(domains: Iterable['Domain']):
    snake_snake_to_camel = ast.Dict(
        keys=[],
        values=[],
        render_context={
            'expand': True,
        }
    )

    for domain in domains:
        for command in domain.commands:
            assign_dict_key_value(
                snake_snake_to_camel,
                (domain.domain.snake_case, command.name.snake_case),
                command.name.camel_case
            )

    return ast.Assign(
        targets=[ast.Name('command_names')],
        value=ast.Dict(
            keys=[ast.Constant('snake:snake:camel')],
            values=[snake_snake_to_camel]
        ),
        render_context={
            'lines_before': 2,
        }
    )


def _command_params_properties(domains: Iterable['Domain']):
    snake_to_camel = ast.Dict(
        keys=[],
        values=[],
        render_context={
            'expand': True,
        }
    )

    for domain in domains:
        for command in domain.commands:
            for parameter in command.parameters:
                assign_dict_key_value(
                    snake_to_camel,
                    (domain.domain.snake_case, command.name.snake_case, parameter.name.snake_case),
                    parameter.name.camel_case
                )

    return ast.Assign(
        targets=[ast.Name('command_params_properties')],
        value=ast.Dict(
            keys=[ast.Constant('snake:camel')],
            values=[snake_to_camel]
        ),
        render_context={
            'lines_before': 2,
        }
    )


def _command_return_properties(domains: Iterable['Domain']):
    camel_to_snake = ast.Dict(
        keys=[],
        values=[],
        render_context={
            'expand': True,
        }
    )

    for domain in domains:
        for command in domain.commands:
            for return_ in command.returns:
                assign_dict_key_value(
                    camel_to_snake,
                    (domain.domain.camel_case, command.name.camel_case, return_.name.camel_case),
                    return_.name.snake_case
                )

    return ast.Assign(
        targets=[ast.Name('command_return_properties')],
        value=ast.Dict(
            keys=[ast.Constant('camel:snake')],
            values=[camel_to_snake]
        ),
        render_context={
            'lines_before': 2,
        }
    )


def _event_names(domains: Iterable['Domain']):
    camel_to_snake = ast.Dict(
        keys=[],
        values=[],
        render_context={
            'expand': True,
        }
    )

    snake_to_camel = ast.Dict(
        keys=[],
        values=[],
        render_context={
            'expand': True,
        }
    )

    for domain in domains:
        for event in domain.events:
            assign_dict_key_value(
                camel_to_snake,
                (domain.domain.camel_case, event.name.camel_case),
                event.name.snake_case
            )
            assign_dict_key_value(
                snake_to_camel,
                (domain.domain.snake_case, event.name.snake_case),
                event.name.camel_case
            )

    return ast.Assign(
        targets=[ast.Name('event_names')],
        value=ast.Dict(
            keys=[
                ast.Constant('camel:snake'),
                ast.Constant('snake:camel')
            ],
            values=[
                camel_to_snake,
                snake_to_camel
            ]
        ),
        render_context={
            'lines_before': 2,
        }
    )


def _event_params_properties(domains: Iterable['Domain']):
    camel_to_snake = ast.Dict(
        keys=[],
        values=[],
        render_context={
            'expand': True,
        }
    )

    for domain in domains:
        for event in domain.events:
            for parameter in event.parameters:
                assign_dict_key_value(
                    camel_to_snake,
                    (domain.domain.camel_case, event.name.camel_case, parameter.name.camel_case),
                    parameter.name.snake_case
                )

    return ast.Assign(
        targets=[ast.Name('event_params_properties')],
        value=ast.Dict(
            keys=[ast.Constant('camel:snake')],
            values=[camel_to_snake]
        ),
        render_context={
            'lines_before': 2,
        }
    )


def generate(domains: Iterable[Domain]):
    root = ast.Module(
        body=[]
    )

    root.body.extend([
        _domain_names(domains),
        _type_properties(domains),
        _command_names(domains),
        _command_params_properties(domains),
        _command_return_properties(domains),
        _event_names(domains),
        _event_params_properties(domains)
    ])

    return root
