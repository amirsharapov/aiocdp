# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.domains.base import (
    BaseDomain
)
from cdp.domains import (
    mappers
)
from cdp.utils import (
    UNDEFINED,
    is_defined
)
from dataclasses import (
    dataclass
)
from typing import (
    TYPE_CHECKING
)
from cdp.domains.security.types import (
    CertificateErrorAction
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IFutureResponse
    )


@dataclass
class Security(BaseDomain):
    def disable(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Security.disable',
            params,
            False
        )

    def enable(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Security.enable',
            params,
            False
        )

    def set_ignore_certificate_errors(
            self,
            ignore: 'bool'
    ) -> 'IFutureResponse[None]':
        params = {
            'ignore': ignore,
        }

        return self._send_command(
            'Security.setIgnoreCertificateErrors',
            params,
            False
        )

    def handle_certificate_error(
            self,
            event_id: 'int',
            action: 'CertificateErrorAction'
    ) -> 'IFutureResponse[None]':
        params = {
            'eventId': event_id,
            'action': to_dict(
                action,
                'camel'
            ),
        }

        return self._send_command(
            'Security.handleCertificateError',
            params,
            False
        )

    def set_override_certificate_errors(
            self,
            override: 'bool'
    ) -> 'IFutureResponse[None]':
        params = {
            'override': override,
        }

        return self._send_command(
            'Security.setOverrideCertificateErrors',
            params,
            False
        )
