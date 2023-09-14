from dataclasses import (
    dataclass
)
from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.network.types import (
    RequestId
)


@dataclass
class Audits(BaseDomain):
    def get_encoded_response(
        self,
        request_id: RequestId,
        encoding: str,
        quality: float = UNDEFINED,
        size_only: bool = UNDEFINED
    ):
        params = {
            "requestId": request_id,
            "encoding": encoding,
        }

        if is_defined(
            quality
        ):
            params["quality"] = quality

        if is_defined(
            size_only
        ):
            params["sizeOnly"] = size_only

        return self._send_command(
            "Audits.getEncodedResponse",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Audits.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Audits.enable",
            params
        )

    def check_contrast(
        self,
        report_aaa: bool = UNDEFINED
    ):
        params = {}

        if is_defined(
            report_aaa
        ):
            params["reportAAA"] = report_aaa

        return self._send_command(
            "Audits.checkContrast",
            params
        )

    def check_forms_issues(
        self
    ):
        params = {}

        return self._send_command(
            "Audits.checkFormsIssues",
            params
        )

