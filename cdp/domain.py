from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from cdp.generated import mapping

if TYPE_CHECKING:
    from cdp.domains import Domains


def validate_args_kwargs(args, kwargs):
    if args and kwargs:
        raise Exception

    if args and len(args) > 1:
        raise Exception

    if args:
        return args[0]

    return kwargs


def command_params_properties_to_camel(
        domain: str,
        method: str,
        params: dict
):
    new_params = {}

    for key, value in params.items():
        key = mapping.command_params_properties['snake:snake:snake:camel'].get(
            (domain, method, key),
            key
        )

        new_params[key] = value

    return new_params


def command_return_properties_to_snake(
        domain: str,
        method: str,
        return_: dict
):
    new_return = {}

    for key, value in return_.items():
        key = mapping.command_return_properties['snake:snake:camel:snake'].get(
            (domain, method, key),
            key
        )

        new_return[key] = value

    return new_return


@dataclass
class Method:
    domain: 'Domain'
    name: str

    cdp_domain: str = field(
        init=False
    )
    cdp_method: str = field(
        init=False
    )

    def __post_init__(self):
        self.cdp_domain = mapping.domain_names['snake:pascal'].get(
            self.domain.name,
            self.domain.name
        )

        self.cdp_method = mapping.command_names['snake:snake:camel'].get(
            (self.domain.name, self.name),
            self.name
        )

    def response_middleware(self, response: dict):
        return {
            **response,
            'result': command_return_properties_to_snake(
                self.domain.name,
                self.name,
                response['result']
            )
        }

    def __call__(self, *args, **kwargs):
        params = validate_args_kwargs(
            args,
            kwargs
        )

        params = command_params_properties_to_camel(
            self.domain.name,
            self.name,
            params
        )

        return self.domain.domains.ws_target.send_command(
            f'{self.cdp_domain}.{self.cdp_method}',
            params,
            [
                self.response_middleware
            ]
        )


@dataclass
class Domain:
    domains: 'Domains'
    name: str

    def __getattr__(self, item: str):
        return Method(
            self,
            item
        )
