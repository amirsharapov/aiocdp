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
    RequestId,
    ConnectionType,
    ContentSecurityPolicySource,
    LoadNetworkResourcePageResult,
    ClientSecurityState,
    InterceptionId,
    Initiator,
    ResourcePriority,
    SignedExchangeHeader,
    CrossOriginEmbedderPolicyStatus,
    ErrorReason,
    Request,
    CorsError,
    PrivateNetworkRequestPolicy,
    SecurityIsolationStatus,
    CertificateTransparencyCompliance,
    CrossOriginEmbedderPolicyValue,
    CrossOriginOpenerPolicyStatus,
    ServiceWorkerResponseSource,
    ReportStatus,
    AuthChallenge,
    LoaderId,
    SignedExchangeErrorField,
    WebSocketFrame,
    MonotonicTime,
    TrustTokenOperationType,
    CookieSourceScheme,
    CrossOriginOpenerPolicyValue,
    InterceptionStage,
    CookiePriority,
    IPAddressSpace,
    ConnectTiming,
    LoadNetworkResourceOptions,
    ReportingApiReport,
    CorsErrorStatus,
    SignedExchangeInfo,
    TimeSinceEpoch,
    Response,
    ResourceType,
    WebSocketRequest,
    SecurityDetails,
    ReportId,
    ResourceTiming,
    Headers,
    BlockedReason,
    WebSocketResponse,
    AlternateProtocolUsage,
    CookieSameSite,
    TrustTokenParams,
    AuthChallengeResponse,
    Cookie
)
from cdp.domains.security.types import (
    CertificateId,
    MixedContentType,
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
        error_reason: MaybeUndefined[],
        raw_response: MaybeUndefined[],
        url: MaybeUndefined[],
        method: MaybeUndefined[],
        post_data: MaybeUndefined[],
        headers: MaybeUndefined[],
        auth_challenge_response: MaybeUndefined[]
    ):
        params = {
            "interceptionId": interception_id,
        }

        if is_defined(
            error_reason
        ):
            params[] = error_reason

        if is_defined(
            raw_response
        ):
            params[] = raw_response

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
            auth_challenge_response
        ):
            params[] = auth_challenge_response

        return self._send_command(
            "Network.continueInterceptedRequest",
            params
        )

    def delete_cookies(
        self,
        name: str,
        url: MaybeUndefined[],
        domain: MaybeUndefined[],
        path: MaybeUndefined[]
    ):
        params = {
            "name": name,
        }

        if is_defined(
            url
        ):
            params[] = url

        if is_defined(
            domain
        ):
            params[] = domain

        if is_defined(
            path
        ):
            params[] = path

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
        connection_type: MaybeUndefined[]
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
            params[] = connection_type

        return self._send_command(
            "Network.emulateNetworkConditions",
            params
        )

    def enable(
        self,
        max_total_buffer_size: MaybeUndefined[],
        max_resource_buffer_size: MaybeUndefined[],
        max_post_data_size: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            max_total_buffer_size
        ):
            params[] = max_total_buffer_size

        if is_defined(
            max_resource_buffer_size
        ):
            params[] = max_resource_buffer_size

        if is_defined(
            max_post_data_size
        ):
            params[] = max_post_data_size

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
        urls: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            urls
        ):
            params[] = urls

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
        case_sensitive: MaybeUndefined[],
        is_regex: MaybeUndefined[]
    ):
        params = {
            "requestId": request_id,
            "query": query,
        }

        if is_defined(
            case_sensitive
        ):
            params[] = case_sensitive

        if is_defined(
            is_regex
        ):
            params[] = is_regex

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
        url: MaybeUndefined[],
        domain: MaybeUndefined[],
        path: MaybeUndefined[],
        secure: MaybeUndefined[],
        http_only: MaybeUndefined[],
        same_site: MaybeUndefined[],
        expires: MaybeUndefined[],
        priority: MaybeUndefined[],
        same_party: MaybeUndefined[],
        source_scheme: MaybeUndefined[],
        source_port: MaybeUndefined[],
        partition_key: MaybeUndefined[]
    ):
        params = {
            "name": name,
            "value": value,
        }

        if is_defined(
            url
        ):
            params[] = url

        if is_defined(
            domain
        ):
            params[] = domain

        if is_defined(
            path
        ):
            params[] = path

        if is_defined(
            secure
        ):
            params[] = secure

        if is_defined(
            http_only
        ):
            params[] = http_only

        if is_defined(
            same_site
        ):
            params[] = same_site

        if is_defined(
            expires
        ):
            params[] = expires

        if is_defined(
            priority
        ):
            params[] = priority

        if is_defined(
            same_party
        ):
            params[] = same_party

        if is_defined(
            source_scheme
        ):
            params[] = source_scheme

        if is_defined(
            source_port
        ):
            params[] = source_port

        if is_defined(
            partition_key
        ):
            params[] = partition_key

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
        accept_language: MaybeUndefined[],
        platform: MaybeUndefined[],
        user_agent_metadata: MaybeUndefined[]
    ):
        params = {
            "userAgent": user_agent,
        }

        if is_defined(
            accept_language
        ):
            params[] = accept_language

        if is_defined(
            platform
        ):
            params[] = platform

        if is_defined(
            user_agent_metadata
        ):
            params[] = user_agent_metadata

        return self._send_command(
            "Network.setUserAgentOverride",
            params
        )

    def get_security_isolation_status(
        self,
        frame_id: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            frame_id
        ):
            params[] = frame_id

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
        frame_id: MaybeUndefined[],
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
            params[] = frame_id

        return self._send_command(
            "Network.loadNetworkResource",
            params
        )

