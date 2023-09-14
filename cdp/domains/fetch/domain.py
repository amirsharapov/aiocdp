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
    ResourceType,
    ErrorReason,
    RequestId,
    Request
)
from cdp.domains.fetch.types import (
    AuthChallenge,
    RequestStage,
    RequestId,
    AuthChallengeResponse
)
from cdp.domains.io.types import (
    StreamHandle
)
from cdp.domains.page.types import (
    FrameId
)


@dataclass
class Fetch(BaseDomain):
    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Fetch.disable",
            params
        )

    def enable(
        self,
        patterns: MaybeUndefined[],
        handle_auth_requests: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            patterns
        ):
            params[] = patterns

        if is_defined(
            handle_auth_requests
        ):
            params[] = handle_auth_requests

        return self._send_command(
            "Fetch.enable",
            params
        )

    def fail_request(
        self,
        request_id: RequestId,
        error_reason: ErrorReason
    ):
        params = {
            "requestId": request_id,
            "errorReason": error_reason,
        }

        return self._send_command(
            "Fetch.failRequest",
            params
        )

    def fulfill_request(
        self,
        request_id: RequestId,
        response_code: int,
        response_headers: MaybeUndefined[],
        binary_response_headers: MaybeUndefined[],
        body: MaybeUndefined[],
        response_phrase: MaybeUndefined[]
    ):
        params = {
            "requestId": request_id,
            "responseCode": response_code,
        }

        if is_defined(
            response_headers
        ):
            params[] = response_headers

        if is_defined(
            binary_response_headers
        ):
            params[] = binary_response_headers

        if is_defined(
            body
        ):
            params[] = body

        if is_defined(
            response_phrase
        ):
            params[] = response_phrase

        return self._send_command(
            "Fetch.fulfillRequest",
            params
        )

    def continue_request(
        self,
        request_id: RequestId,
        url: MaybeUndefined[],
        method: MaybeUndefined[],
        post_data: MaybeUndefined[],
        headers: MaybeUndefined[],
        intercept_response: MaybeUndefined[]
    ):
        params = {
            "requestId": request_id,
        }

        if is_defined(
            url
        ):
            params[] = url

        if is_defined(
            method
        ):
            params[] = method

        if is_defined(
            post_data
        ):
            params[] = post_data

        if is_defined(
            headers
        ):
            params[] = headers

        if is_defined(
            intercept_response
        ):
            params[] = intercept_response

        return self._send_command(
            "Fetch.continueRequest",
            params
        )

    def continue_with_auth(
        self,
        request_id: RequestId,
        auth_challenge_response: AuthChallengeResponse
    ):
        params = {
            "requestId": request_id,
            "authChallengeResponse": auth_challenge_response,
        }

        return self._send_command(
            "Fetch.continueWithAuth",
            params
        )

    def continue_response(
        self,
        request_id: RequestId,
        response_code: MaybeUndefined[],
        response_phrase: MaybeUndefined[],
        response_headers: MaybeUndefined[],
        binary_response_headers: MaybeUndefined[]
    ):
        params = {
            "requestId": request_id,
        }

        if is_defined(
            response_code
        ):
            params[] = response_code

        if is_defined(
            response_phrase
        ):
            params[] = response_phrase

        if is_defined(
            response_headers
        ):
            params[] = response_headers

        if is_defined(
            binary_response_headers
        ):
            params[] = binary_response_headers

        return self._send_command(
            "Fetch.continueResponse",
            params
        )

    def get_response_body(
        self,
        request_id: RequestId
    ):
        params = {
            "requestId": request_id,
        }

        return self._send_command(
            "Fetch.getResponseBody",
            params
        )

    def take_response_body_as_stream(
        self,
        request_id: RequestId
    ):
        params = {
            "requestId": request_id,
        }

        return self._send_command(
            "Fetch.takeResponseBodyAsStream",
            params
        )

