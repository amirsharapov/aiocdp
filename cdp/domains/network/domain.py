from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.network.types import (
    WebSocketFrame,
    CookieSameSite,
    ReportId,
    InterceptionId,
    SignedExchangeInfo,
    MonotonicTime,
    Request,
    SecurityDetails,
    WebSocketResponse,
    CorsErrorStatus,
    SignedExchangeHeader,
    TrustTokenParams,
    ResourcePriority,
    CertificateTransparencyCompliance,
    AuthChallengeResponse,
    AuthChallenge,
    IPAddressSpace,
    ConnectionType,
    WebSocketRequest,
    CookieSourceScheme,
    ServiceWorkerResponseSource,
    CookiePriority,
    SignedExchangeErrorField,
    ConnectTiming,
    ResourceTiming,
    ContentSecurityPolicySource,
    LoaderId,
    CrossOriginEmbedderPolicyStatus,
    SecurityIsolationStatus,
    CrossOriginOpenerPolicyValue,
    AlternateProtocolUsage,
    ErrorReason,
    BlockedReason,
    TrustTokenOperationType,
    Cookie,
    PrivateNetworkRequestPolicy,
    CrossOriginEmbedderPolicyValue,
    LoadNetworkResourceOptions,
    CorsError,
    ResourceType,
    RequestId,
    CrossOriginOpenerPolicyStatus,
    TimeSinceEpoch,
    ReportingApiReport,
    InterceptionStage,
    ClientSecurityState,
    LoadNetworkResourcePageResult,
    Initiator,
    ReportStatus,
    Response,
    Headers
)
from cdp.domains.security.types import (
    MixedContentType,
    CertificateId,
    SecurityState
)
from cdp.domains.runtime.types import (
    StackTrace
)
from cdp.domains.io.types import (
    StreamHandle
)
from cdp.domains.emulation.types import (
    UserAgentMetadata
)
from cdp.domains.page.types import (
    FrameId
)


@dataclass
class Network(BaseDomain):
    def set_accepted_encodings(
        self,
        encodings: list
    ):
        params = {
            "encodings": encodings,
        }

        return self._send_command(
            "Network.setAcceptedEncodings",
            params
        )

    def clear_accepted_encodings_override(
        self
    ):
        params = {}

        return self._send_command(
            "Network.clearAcceptedEncodingsOverride",
            params
        )

    def can_clear_browser_cache(
        self
    ):
        params = {}

        return self._send_command(
            "Network.canClearBrowserCache",
            params
        )

    def can_clear_browser_cookies(
        self
    ):
        params = {}

        return self._send_command(
            "Network.canClearBrowserCookies",
            params
        )

    def can_emulate_network_conditions(
        self
    ):
        params = {}

        return self._send_command(
            "Network.canEmulateNetworkConditions",
            params
        )

    def clear_browser_cache(
        self
    ):
        params = {}

        return self._send_command(
            "Network.clearBrowserCache",
            params
        )

    def clear_browser_cookies(
        self
    ):
        params = {}

        return self._send_command(
            "Network.clearBrowserCookies",
            params
        )

    def continue_intercepted_request(
        self,
        interception_id: InterceptionId,
        error_reason: MaybeUndefined[ErrorReason],
        raw_response: MaybeUndefined[str],
        url: MaybeUndefined[str],
        method: MaybeUndefined[str],
        post_data: MaybeUndefined[str],
        headers: MaybeUndefined[Headers],
        auth_challenge_response: MaybeUndefined[AuthChallengeResponse]
    ):
        params = {
            "interceptionId": interception_id,
        }

        if is_defined(
            error_reason
        ):
            params["errorReason"] = error_reason

        if is_defined(
            raw_response
        ):
            params["rawResponse"] = raw_response

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
            auth_challenge_response
        ):
            params["authChallengeResponse"] = auth_challenge_response

        return self._send_command(
            "Network.continueInterceptedRequest",
            params
        )

    def delete_cookies(
        self,
        name: str,
        url: MaybeUndefined[str],
        domain: MaybeUndefined[str],
        path: MaybeUndefined[str]
    ):
        params = {
            "name": name,
        }

        if is_defined(
            url
        ):
            params["url"] = url

        if is_defined(
            domain
        ):
            params["domain"] = domain

        if is_defined(
            path
        ):
            params["path"] = path

        return self._send_command(
            "Network.deleteCookies",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Network.disable",
            params
        )

    def emulate_network_conditions(
        self,
        offline: bool,
        latency: float,
        download_throughput: float,
        upload_throughput: float,
        connection_type: MaybeUndefined[ConnectionType]
    ):
        params = {
            "offline": offline,
            "latency": latency,
            "downloadThroughput": download_throughput,
            "uploadThroughput": upload_throughput,
        }

        if is_defined(
            connection_type
        ):
            params["connectionType"] = connection_type

        return self._send_command(
            "Network.emulateNetworkConditions",
            params
        )

    def enable(
        self,
        max_total_buffer_size: MaybeUndefined[int],
        max_resource_buffer_size: MaybeUndefined[int],
        max_post_data_size: MaybeUndefined[int]
    ):
        params = {}

        if is_defined(
            max_total_buffer_size
        ):
            params["maxTotalBufferSize"] = max_total_buffer_size

        if is_defined(
            max_resource_buffer_size
        ):
            params["maxResourceBufferSize"] = max_resource_buffer_size

        if is_defined(
            max_post_data_size
        ):
            params["maxPostDataSize"] = max_post_data_size

        return self._send_command(
            "Network.enable",
            params
        )

    def get_all_cookies(
        self
    ):
        params = {}

        return self._send_command(
            "Network.getAllCookies",
            params
        )

    def get_certificate(
        self,
        origin: str
    ):
        params = {
            "origin": origin,
        }

        return self._send_command(
            "Network.getCertificate",
            params
        )

    def get_cookies(
        self,
        urls: MaybeUndefined[list]
    ):
        params = {}

        if is_defined(
            urls
        ):
            params["urls"] = urls

        return self._send_command(
            "Network.getCookies",
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
            "Network.getResponseBody",
            params
        )

    def get_request_post_data(
        self,
        request_id: RequestId
    ):
        params = {
            "requestId": request_id,
        }

        return self._send_command(
            "Network.getRequestPostData",
            params
        )

    def get_response_body_for_interception(
        self,
        interception_id: InterceptionId
    ):
        params = {
            "interceptionId": interception_id,
        }

        return self._send_command(
            "Network.getResponseBodyForInterception",
            params
        )

    def take_response_body_for_interception_as_stream(
        self,
        interception_id: InterceptionId
    ):
        params = {
            "interceptionId": interception_id,
        }

        return self._send_command(
            "Network.takeResponseBodyForInterceptionAsStream",
            params
        )

    def replay_xhr(
        self,
        request_id: RequestId
    ):
        params = {
            "requestId": request_id,
        }

        return self._send_command(
            "Network.replayXHR",
            params
        )

    def search_in_response_body(
        self,
        request_id: RequestId,
        query: str,
        case_sensitive: MaybeUndefined[bool],
        is_regex: MaybeUndefined[bool]
    ):
        params = {
            "requestId": request_id,
            "query": query,
        }

        if is_defined(
            case_sensitive
        ):
            params["caseSensitive"] = case_sensitive

        if is_defined(
            is_regex
        ):
            params["isRegex"] = is_regex

        return self._send_command(
            "Network.searchInResponseBody",
            params
        )

    def set_blocked_ur_ls(
        self,
        urls: list
    ):
        params = {
            "urls": urls,
        }

        return self._send_command(
            "Network.setBlockedURLs",
            params
        )

    def set_bypass_service_worker(
        self,
        bypass: bool
    ):
        params = {
            "bypass": bypass,
        }

        return self._send_command(
            "Network.setBypassServiceWorker",
            params
        )

    def set_cache_disabled(
        self,
        cache_disabled: bool
    ):
        params = {
            "cacheDisabled": cache_disabled,
        }

        return self._send_command(
            "Network.setCacheDisabled",
            params
        )

    def set_cookie(
        self,
        name: str,
        value: str,
        url: MaybeUndefined[str],
        domain: MaybeUndefined[str],
        path: MaybeUndefined[str],
        secure: MaybeUndefined[bool],
        http_only: MaybeUndefined[bool],
        same_site: MaybeUndefined[CookieSameSite],
        expires: MaybeUndefined[TimeSinceEpoch],
        priority: MaybeUndefined[CookiePriority],
        same_party: MaybeUndefined[bool],
        source_scheme: MaybeUndefined[CookieSourceScheme],
        source_port: MaybeUndefined[int],
        partition_key: MaybeUndefined[str]
    ):
        params = {
            "name": name,
            "value": value,
        }

        if is_defined(
            url
        ):
            params["url"] = url

        if is_defined(
            domain
        ):
            params["domain"] = domain

        if is_defined(
            path
        ):
            params["path"] = path

        if is_defined(
            secure
        ):
            params["secure"] = secure

        if is_defined(
            http_only
        ):
            params["httpOnly"] = http_only

        if is_defined(
            same_site
        ):
            params["sameSite"] = same_site

        if is_defined(
            expires
        ):
            params["expires"] = expires

        if is_defined(
            priority
        ):
            params["priority"] = priority

        if is_defined(
            same_party
        ):
            params["sameParty"] = same_party

        if is_defined(
            source_scheme
        ):
            params["sourceScheme"] = source_scheme

        if is_defined(
            source_port
        ):
            params["sourcePort"] = source_port

        if is_defined(
            partition_key
        ):
            params["partitionKey"] = partition_key

        return self._send_command(
            "Network.setCookie",
            params
        )

    def set_cookies(
        self,
        cookies: list
    ):
        params = {
            "cookies": cookies,
        }

        return self._send_command(
            "Network.setCookies",
            params
        )

    def set_extra_http_headers(
        self,
        headers: Headers
    ):
        params = {
            "headers": headers,
        }

        return self._send_command(
            "Network.setExtraHTTPHeaders",
            params
        )

    def set_attach_debug_stack(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Network.setAttachDebugStack",
            params
        )

    def set_request_interception(
        self,
        patterns: list
    ):
        params = {
            "patterns": patterns,
        }

        return self._send_command(
            "Network.setRequestInterception",
            params
        )

    def set_user_agent_override(
        self,
        user_agent: str,
        accept_language: MaybeUndefined[str],
        platform: MaybeUndefined[str],
        user_agent_metadata: MaybeUndefined[UserAgentMetadata]
    ):
        params = {
            "userAgent": user_agent,
        }

        if is_defined(
            accept_language
        ):
            params["acceptLanguage"] = accept_language

        if is_defined(
            platform
        ):
            params["platform"] = platform

        if is_defined(
            user_agent_metadata
        ):
            params["userAgentMetadata"] = user_agent_metadata

        return self._send_command(
            "Network.setUserAgentOverride",
            params
        )

    def get_security_isolation_status(
        self,
        frame_id: MaybeUndefined[FrameId]
    ):
        params = {}

        if is_defined(
            frame_id
        ):
            params["frameId"] = frame_id

        return self._send_command(
            "Network.getSecurityIsolationStatus",
            params
        )

    def enable_reporting_api(
        self,
        enable: bool
    ):
        params = {
            "enable": enable,
        }

        return self._send_command(
            "Network.enableReportingApi",
            params
        )

    def load_network_resource(
        self,
        frame_id: MaybeUndefined[FrameId],
        url: str,
        options: LoadNetworkResourceOptions
    ):
        params = {
            "url": url,
            "options": options,
        }

        if is_defined(
            frame_id
        ):
            params["frameId"] = frame_id

        return self._send_command(
            "Network.loadNetworkResource",
            params
        )

