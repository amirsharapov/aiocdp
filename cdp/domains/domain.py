from dataclasses import dataclass
from typing import TYPE_CHECKING

from cdp.domains.base import BaseDomain
from cdp.domains import conversions

if TYPE_CHECKING:
    from cdp.domains.domains import Domains


def transform_method(domain_name: str, method_name: str):
    return (
        conversions.domain_names[domain_name] + '.' +
        conversions.method_names[method_name]
    )


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
        params = args[0]
    else:
        params = kwargs

    return {}


@dataclass
class Domain(BaseDomain):
    name: str
    domains: 'Domains'

    def __getattr__(self, item: str):
        method = transform_method(
            self.name,
            item
        )

        def wrapper(*args, **kwargs):
            params = load_params(
                self.name,
                method,
                args,
                kwargs
            )

            return self._send_command(
                method,
                params
            )

        return wrapper
