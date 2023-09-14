from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.domains.fetch.types import (
    AuthChallengeResponse,
    RequestId
)
from cdp.domains.network.types import (
    ErrorReason
)
from cdp.domains.io.types import (
    StreamHandle
)
from cdp.utils import (
    is_defined,
    UNDEFINED
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
        patterns: list = UNDEFINED,
        handle_auth_requests: bool = UNDEFINED
    ):
        params = {}

        if is_defined(
            patterns
        ):
            params["patterns"] = patterns

        if is_defined(
            handle_auth_requests
        ):
            params["handleAuthRequests"] = handle_auth_requests

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
        response_headers: list = UNDEFINED,
        binary_response_headers: str = UNDEFINED,
        body: str = UNDEFINED,
        response_phrase: str = UNDEFINED
    ):
        params = {
            "requestId": request_id,
            "responseCode": response_code,
        }

        if is_defined(
            response_headers
        ):
            params["responseHeaders"] = response_headers

        if is_defined(
            binary_response_headers
        ):
            params["binaryResponseHeaders"] = binary_response_headers

        if is_defined(
            body
        ):
            params["body"] = body

        if is_defined(
            response_phrase
        ):
            params["responsePhrase"] = response_phrase

        return self._send_command(
            "Fetch.fulfillRequest",
            params
        )

    def continue_request(
        self,
        request_id: RequestId,
        url: str = UNDEFINED,
        method: str = UNDEFINED,
        post_data: str = UNDEFINED,
        headers: list = UNDEFINED,
        intercept_response: bool = UNDEFINED
    ):
        params = {
            "requestId": request_id,
        }

        if is_defined(
            url
        ):
            params["url"] = url

        if is_defined(
            method
        ):
            params["method"] = method

        if is_defined(
            post_data
        ):
            params["postData"] = post_data

        if is_defined(
            headers
        ):
            params["headers"] = headers

        if is_defined(
            intercept_response
        ):
            params["interceptResponse"] = intercept_response

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
        response_code: int = UNDEFINED,
        response_phrase: str = UNDEFINED,
        response_headers: list = UNDEFINED,
        binary_response_headers: str = UNDEFINED
    ):
        params = {
            "requestId": request_id,
        }

        if is_defined(
            response_code
        ):
            params["responseCode"] = response_code

        if is_defined(
            response_phrase
        ):
            params["responsePhrase"] = response_phrase

        if is_defined(
            response_headers
        ):
            params["responseHeaders"] = response_headers

        if is_defined(
            binary_response_headers
        ):
            params["binaryResponseHeaders"] = binary_response_headers

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

