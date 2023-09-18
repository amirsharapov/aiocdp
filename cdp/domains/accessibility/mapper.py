from typing import TYPE_CHECKING

from cdp.domains import mappers

with TYPE_CHECKING:
    from cdp.domains.accessibility import types


def _ax_value_source__to_camel_dict(data: 'types.AXValueSource'):
    mapper_keys = {
        'key': (
            'accessibility.AXValueSourceType',
            'to_dict',
            'camel'
        ),
        'attribute': (
            'accessibility.AXValueSourceAttribute',
            'to_dict',
            'camel'
        ),
    }

    return {
        'type': data.type,
        'value': data.value,
        'key': (
            mappers.get_mapper(mapper_keys['key'])(
                data.key
            )
        ),
        'attribute': (
            mappers.get_mapper(mapper_keys['attribute'])(
                data.attribute
            )
        ),
        'something': list(map(
            mappers.get_mapper(mapper_keys['something']),
            data.something
        ))
    }


def _ax_value_source__to_snake_dict():
    pass


def _ax_value_source__from_camel_dict(data: dict):
    key = mapper_registry.get_mapper(
        'accessibility.AXValueSourceType',
        'from_dict',
        'camel'
    )(data.key)

    attribute = mapper_registry.get_mapper(
        'accessibility.AXValueSourceAttribute',
        'from_dict',
        'camel'
    )(data.attribute)

    something = list(map(
        mapper_registry.get_mapper(
            'accessibility.AXValueSourceType',
            'from_dict',
            'camel'
        )
    ))

    # something = [
    #     mapper_registry.get_mapper(
    #         'accessibility.AXValueSourceType',
    #         'to_camel'
    #     )(item) for item in data.something
    # ]

    return {
        'type': data.type,
        'value': data.value,
        'key': key,
        'attribute': attribute,
        'something': something
    }


def _ax_value_source__from_snake_dict():
    pass


mappers.add_mapper(
    _ax_value_source__to_camel_dict,
    (
        'accessibility.AXValueSource',
        'to_dict',
        'camel'
    )
)
mappers.add_mapper(
    _ax_value_source__to_snake_dict,
    (
        'accessibility.AXValueSource',
        'to_dict',
        'snake',
    )
)
mapper_registry.add_mapper(
    'accessibility.AXValueSource',
    'from_camel',
    _ax_value_source__from_camel_dict
)
mapper_registry.add_mapper(
    'accessibility.AXValueSource',
    'from_snake',
    _ax_value_source__from_snake_dict
)
