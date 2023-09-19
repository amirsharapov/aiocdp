from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from cdp.domains.base import BaseDomain
from cdp.generated import mapping

if TYPE_CHECKING:
    from cdp.domains.domains import Domains


def transform_method(domain_name: str, domain_method_name: str):
    return (
        mapping.domain_name_map[domain_name] + '.' +
        mapping.domain_method_name_map[domain_method_name]
    )


def transform_params(params: dict[str, Any]):
    params_ = {}

    for k, v in params.items():
        k = mapping.request_param_mapper = None


def validate_method_args_kwargs(args, kwargs, domain_name, method_name):
    if args and kwargs:
        raise Exception(
            ...
        )


def load_params(
        args,
        kwargs
):
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
            validate_method_args_kwargs(
                args,
                kwargs,
                self.name,
                method
            )

            params = load_params(
                args,
                kwargs
            )

            return self._send_command(
                method,
                params
            )

        return wrapper
