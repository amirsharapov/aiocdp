from dataclasses import dataclass
from typing import TYPE_CHECKING

from cdp.domains.base import BaseDomain
from cdp.generated import mapping

if TYPE_CHECKING:
    from cdp.domains.domains import Domains


def load_params(
        domain_name: str,
        method_name: str,
        args: tuple,
        kwargs: dict
):
    """
    Loads the params by either using the first argument as the params dictionary or the kwargs.
    *args and **kwargs are mutually exclusive.
    """
    if args and kwargs:
        raise Exception

    if args and len(args) > 1:
        raise Exception

    if args:
        old_params = args[0]

    else:
        old_params = kwargs

    new_params = {}

    for key, value in old_params.items():
        key = mapping.command_params_properties['snake:camel'].get(
            (domain_name, method_name, key),
            key
        )

        new_params[key] = value

    return new_params


@dataclass
class Domain(BaseDomain):
    name: str
    domains: 'Domains'

    def __getattr__(self, item: str):
        domain_name = mapping.domain_names['snake:pascal'].get(
            self.name,
            self.name
        )

        method_name = mapping.command_names['snake:camel'].get(
            (self.name, item),
            item
        )

        method_name = f'{domain_name}.{method_name}'

        def wrapper(*args, **kwargs):
            params = load_params(
                self.name,
                method_name,
                args,
                kwargs
            )

            return self._send_command(
                method_name,
                params
            )

        return wrapper
