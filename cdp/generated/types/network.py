# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from cdp.generated.types import (
    debugger,
    emulation,
    io,
    page,
    runtime,
    security
)
from typing import (
    Literal,
    TypedDict
)

LoaderId = str

RequestId = str

InterceptionId = str

TimeSinceEpoch = float

MonotonicTime = float

Headers = dict

ReportId = str

ResourceType = Literal[
    'Document',
    'Stylesheet',
    'Image',
    'Media',
    'Font',
    'Script',
    'TextTrack',
    'XHR',
    'Fetch',
    'Prefetch',
    'EventSource',
    'WebSocket',
    'Manifest',
    'SignedExchange',
    'Ping',
    'CSPViolationReport',
    'Preflight',
    'Other'
]

ErrorReason = Literal[
    'Failed',
    'Aborted',
    'TimedOut',
    'AccessDenied',
    'ConnectionClosed',
    'ConnectionReset',
    'ConnectionRefused',
    'ConnectionAborted',
    'ConnectionFailed',
    'NameNotResolved',
    'InternetDisconnected',
    'AddressUnreachable',
    'BlockedByClient',
    'BlockedByResponse'
]

ConnectionType = Literal[
    'none',
    'cellular2g',
    'cellular3g',
    'cellular4g',
    'bluetooth',
    'ethernet',
    'wifi',
    'wimax',
    'other'
]

CookieSameSite = Literal[
    'Strict',
    'Lax',
    'None'
]

CookiePriority = Literal[
    'Low',
    'Medium',
    'High'
]

CookieSourceScheme = Literal[
    'Unset',
    'NonSecure',
    'Secure'
]

ResourcePriority = Literal[
    'VeryLow',
    'Low',
    'Medium',
    'High',
    'VeryHigh'
]

CertificateTransparencyCompliance = Literal[
    'unknown',
    'not-compliant',
    'compliant'
]

BlockedReason = Literal[
    'other',
    'csp',
    'mixed-content',
    'origin',
    'inspector',
    'subresource-filter',
    'content-type',
    'coep-frame-resource-needs-coep-header',
    'coop-sandboxed-iframe-cannot-navigate-to-coop-page',
    'corp-not-same-origin',
    'corp-not-same-origin-after-defaulted-to-same-origin-by-coep',
    'corp-not-same-site'
]

CorsError = Literal[
    'DisallowedByMode',
    'InvalidResponse',
    'WildcardOriginNotAllowed',
    'MissingAllowOriginHeader',
    'MultipleAllowOriginValues',
    'InvalidAllowOriginValue',
    'AllowOriginMismatch',
    'InvalidAllowCredentials',
    'CorsDisabledScheme',
    'PreflightInvalidStatus',
    'PreflightDisallowedRedirect',
    'PreflightWildcardOriginNotAllowed',
    'PreflightMissingAllowOriginHeader',
    'PreflightMultipleAllowOriginValues',
    'PreflightInvalidAllowOriginValue',
    'PreflightAllowOriginMismatch',
    'PreflightInvalidAllowCredentials',
    'PreflightMissingAllowExternal',
    'PreflightInvalidAllowExternal',
    'PreflightMissingAllowPrivateNetwork',
    'PreflightInvalidAllowPrivateNetwork',
    'InvalidAllowMethodsPreflightResponse',
    'InvalidAllowHeadersPreflightResponse',
    'MethodDisallowedByPreflightResponse',
    'HeaderDisallowedByPreflightResponse',
    'RedirectContainsCredentials',
    'InsecurePrivateNetwork',
    'InvalidPrivateNetworkAccess',
    'UnexpectedPrivateNetworkAccess',
    'NoCorsRedirectModeNotFollow',
    'PreflightMissingPrivateNetworkAccessId',
    'PreflightMissingPrivateNetworkAccessName',
    'PrivateNetworkAccessPermissionUnavailable',
    'PrivateNetworkAccessPermissionDenied'
]

ServiceWorkerResponseSource = Literal[
    'cache-storage',
    'http-cache',
    'fallback-code',
    'network'
]

TrustTokenOperationType = Literal[
    'Issuance',
    'Redemption',
    'Signing'
]

AlternateProtocolUsage = Literal[
    'alternativeJobWonWithoutRace',
    'alternativeJobWonRace',
    'mainJobWonRace',
    'mappingMissing',
    'broken',
    'dnsAlpnH3JobWonWithoutRace',
    'dnsAlpnH3JobWonRace',
    'unspecifiedReason'
]

SetCookieBlockedReason = Literal[
    'SecureOnly',
    'SameSiteStrict',
    'SameSiteLax',
    'SameSiteUnspecifiedTreatedAsLax',
    'SameSiteNoneInsecure',
    'UserPreferences',
    'ThirdPartyBlockedInFirstPartySet',
    'SyntaxError',
    'SchemeNotSupported',
    'OverwriteSecure',
    'InvalidDomain',
    'InvalidPrefix',
    'UnknownError',
    'SchemefulSameSiteStrict',
    'SchemefulSameSiteLax',
    'SchemefulSameSiteUnspecifiedTreatedAsLax',
    'SamePartyFromCrossPartyContext',
    'SamePartyConflictsWithOtherAttributes',
    'NameValuePairExceedsMaxSize',
    'DisallowedCharacter'
]

CookieBlockedReason = Literal[
    'SecureOnly',
    'NotOnPath',
    'DomainMismatch',
    'SameSiteStrict',
    'SameSiteLax',
    'SameSiteUnspecifiedTreatedAsLax',
    'SameSiteNoneInsecure',
    'UserPreferences',
    'ThirdPartyBlockedInFirstPartySet',
    'UnknownError',
    'SchemefulSameSiteStrict',
    'SchemefulSameSiteLax',
    'SchemefulSameSiteUnspecifiedTreatedAsLax',
    'SamePartyFromCrossPartyContext',
    'NameValuePairExceedsMaxSize'
]

InterceptionStage = Literal[
    'Request',
    'HeadersReceived'
]

SignedExchangeErrorField = Literal[
    'signatureSig',
    'signatureIntegrity',
    'signatureCertUrl',
    'signatureCertSha256',
    'signatureValidityUrl',
    'signatureTimestamps'
]

ContentEncoding = Literal[
    'deflate',
    'gzip',
    'br',
    'zstd'
]

PrivateNetworkRequestPolicy = Literal[
    'Allow',
    'BlockFromInsecureToMorePrivate',
    'WarnFromInsecureToMorePrivate',
    'PreflightBlock',
    'PreflightWarn'
]

IPAddressSpace = Literal[
    'Local',
    'Private',
    'Public',
    'Unknown'
]

CrossOriginOpenerPolicyValue = Literal[
    'SameOrigin',
    'SameOriginAllowPopups',
    'RestrictProperties',
    'UnsafeNone',
    'SameOriginPlusCoep',
    'RestrictPropertiesPlusCoep'
]

CrossOriginEmbedderPolicyValue = Literal[
    'None',
    'Credentialless',
    'RequireCorp'
]

ContentSecurityPolicySource = Literal[
    'HTTP',
    'Meta'
]

ReportStatus = Literal[
    'Queued',
    'Pending',
    'MarkedForRemoval',
    'Success'
]


class ResourceTiming(TypedDict):
    request_time: float
    proxy_start: float
    proxy_end: float
    dns_start: float
    dns_end: float
    connect_start: float
    connect_end: float
    ssl_start: float
    ssl_end: float
    worker_start: float
    worker_ready: float
    worker_fetch_start: float
    worker_respond_with_settled: float
    send_start: float
    send_end: float
    push_start: float
    push_end: float
    receive_headers_start: float
    receive_headers_end: float


class PostDataEntry(TypedDict):
    bytes: str


class Request(TypedDict):
    url: str
    method: str
    headers: 'Headers'
    initial_priority: 'ResourcePriority'
    referrer_policy: str
    url_fragment: str
    post_data: str
    has_post_data: bool
    post_data_entries: list
    mixed_content_type: 'security.MixedContentType'
    is_link_preload: bool
    trust_token_params: 'TrustTokenParams'
    is_same_site: bool


class SignedCertificateTimestamp(TypedDict):
    status: str
    origin: str
    log_description: str
    log_id: str
    timestamp: float
    hash_algorithm: str
    signature_algorithm: str
    signature_data: str


class SecurityDetails(TypedDict):
    protocol: str
    key_exchange: str
    cipher: str
    certificate_id: 'security.CertificateId'
    subject_name: str
    san_list: list
    issuer: str
    valid_from: 'TimeSinceEpoch'
    valid_to: 'TimeSinceEpoch'
    signed_certificate_timestamp_list: list
    certificate_transparency_compliance: 'CertificateTransparencyCompliance'
    encrypted_client_hello: bool
    key_exchange_group: str
    mac: str
    server_signature_algorithm: int


class CorsErrorStatus(TypedDict):
    cors_error: 'CorsError'
    failed_parameter: str


class TrustTokenParams(TypedDict):
    operation: 'TrustTokenOperationType'
    refresh_policy: str
    issuers: list


class Response(TypedDict):
    url: str
    status: int
    status_text: str
    headers: 'Headers'
    mime_type: str
    connection_reused: bool
    connection_id: float
    encoded_data_length: float
    security_state: 'security.SecurityState'
    headers_text: str
    request_headers: 'Headers'
    request_headers_text: str
    remote_ip_address: str
    remote_port: int
    from_disk_cache: bool
    from_service_worker: bool
    from_prefetch_cache: bool
    timing: 'ResourceTiming'
    service_worker_response_source: 'ServiceWorkerResponseSource'
    response_time: 'TimeSinceEpoch'
    cache_storage_cache_name: str
    protocol: str
    alternate_protocol_usage: 'AlternateProtocolUsage'
    security_details: 'SecurityDetails'


class WebSocketRequest(TypedDict):
    headers: 'Headers'


class WebSocketResponse(TypedDict):
    status: int
    status_text: str
    headers: 'Headers'
    headers_text: str
    request_headers: 'Headers'
    request_headers_text: str


class WebSocketFrame(TypedDict):
    opcode: float
    mask: bool
    payload_data: str


class CachedResource(TypedDict):
    url: str
    type: 'ResourceType'
    body_size: float
    response: 'Response'


class Initiator(TypedDict):
    type: str
    stack: 'runtime.StackTrace'
    url: str
    line_number: float
    column_number: float
    request_id: 'RequestId'


class Cookie(TypedDict):
    name: str
    value: str
    domain: str
    path: str
    expires: float
    size: int
    http_only: bool
    secure: bool
    session: bool
    priority: 'CookiePriority'
    same_party: bool
    source_scheme: 'CookieSourceScheme'
    source_port: int
    same_site: 'CookieSameSite'
    partition_key: str
    partition_key_opaque: bool


class BlockedSetCookieWithReason(TypedDict):
    blocked_reasons: list
    cookie_line: str
    cookie: 'Cookie'


class BlockedCookieWithReason(TypedDict):
    blocked_reasons: list
    cookie: 'Cookie'


class CookieParam(TypedDict):
    name: str
    value: str
    url: str
    domain: str
    path: str
    secure: bool
    http_only: bool
    same_site: 'CookieSameSite'
    expires: 'TimeSinceEpoch'
    priority: 'CookiePriority'
    same_party: bool
    source_scheme: 'CookieSourceScheme'
    source_port: int
    partition_key: str


class AuthChallenge(TypedDict):
    origin: str
    scheme: str
    realm: str
    source: str


class AuthChallengeResponse(TypedDict):
    response: str
    username: str
    password: str


class RequestPattern(TypedDict):
    url_pattern: str
    resource_type: 'ResourceType'
    interception_stage: 'InterceptionStage'


class SignedExchangeSignature(TypedDict):
    label: str
    signature: str
    integrity: str
    validity_url: str
    date: int
    expires: int
    cert_url: str
    cert_sha256: str
    certificates: list


class SignedExchangeHeader(TypedDict):
    request_url: str
    response_code: int
    response_headers: 'Headers'
    signatures: list
    header_integrity: str


class SignedExchangeError(TypedDict):
    message: str
    signature_index: int
    error_field: 'SignedExchangeErrorField'


class SignedExchangeInfo(TypedDict):
    outer_response: 'Response'
    header: 'SignedExchangeHeader'
    security_details: 'SecurityDetails'
    errors: list


class ConnectTiming(TypedDict):
    request_time: float


class ClientSecurityState(TypedDict):
    initiator_is_secure_context: bool
    initiator_ip_address_space: 'IPAddressSpace'
    private_network_request_policy: 'PrivateNetworkRequestPolicy'


class CrossOriginOpenerPolicyStatus(TypedDict):
    value: 'CrossOriginOpenerPolicyValue'
    report_only_value: 'CrossOriginOpenerPolicyValue'
    reporting_endpoint: str
    report_only_reporting_endpoint: str


class CrossOriginEmbedderPolicyStatus(TypedDict):
    value: 'CrossOriginEmbedderPolicyValue'
    report_only_value: 'CrossOriginEmbedderPolicyValue'
    reporting_endpoint: str
    report_only_reporting_endpoint: str


class ContentSecurityPolicyStatus(TypedDict):
    effective_directives: str
    is_enforced: bool
    source: 'ContentSecurityPolicySource'


class SecurityIsolationStatus(TypedDict):
    coop: 'CrossOriginOpenerPolicyStatus'
    coep: 'CrossOriginEmbedderPolicyStatus'
    csp: list


class ReportingApiReport(TypedDict):
    id: 'ReportId'
    initiator_url: str
    destination: str
    type: str
    timestamp: 'TimeSinceEpoch'
    depth: int
    completed_attempts: int
    body: dict
    status: 'ReportStatus'


class ReportingApiEndpoint(TypedDict):
    url: str
    group_name: str


class LoadNetworkResourcePageResult(TypedDict):
    success: bool
    net_error: float
    net_error_name: str
    http_status_code: float
    stream: 'io.StreamHandle'
    headers: 'Headers'


class LoadNetworkResourceOptions(TypedDict):
    disable_cache: bool
    include_credentials: bool


class SetAcceptedEncodingsParamsT(TypedDict):
    encodings: list


class ContinueInterceptedRequestParamsT(TypedDict):
    interception_id: 'InterceptionId'
    error_reason: 'ErrorReason'
    raw_response: str
    url: str
    method: str
    post_data: str
    headers: 'Headers'
    auth_challenge_response: 'AuthChallengeResponse'


class DeleteCookiesParamsT(TypedDict):
    name: str
    url: str
    domain: str
    path: str


class EmulateNetworkConditionsParamsT(TypedDict):
    offline: bool
    latency: float
    download_throughput: float
    upload_throughput: float
    connection_type: 'ConnectionType'


class EnableParamsT(TypedDict):
    max_total_buffer_size: int
    max_resource_buffer_size: int
    max_post_data_size: int


class GetCertificateParamsT(TypedDict):
    origin: str


class GetCookiesParamsT(TypedDict):
    urls: list


class GetResponseBodyParamsT(TypedDict):
    request_id: 'RequestId'


class GetRequestPostDataParamsT(TypedDict):
    request_id: 'RequestId'


class GetResponseBodyForInterceptionParamsT(TypedDict):
    interception_id: 'InterceptionId'


class TakeResponseBodyForInterceptionAsStreamParamsT(TypedDict):
    interception_id: 'InterceptionId'


class ReplayXHRParamsT(TypedDict):
    request_id: 'RequestId'


class SearchInResponseBodyParamsT(TypedDict):
    request_id: 'RequestId'
    query: str
    case_sensitive: bool
    is_regex: bool


class SetBlockedURLsParamsT(TypedDict):
    urls: list


class SetBypassServiceWorkerParamsT(TypedDict):
    bypass: bool


class SetCacheDisabledParamsT(TypedDict):
    cache_disabled: bool


class SetCookieParamsT(TypedDict):
    name: str
    value: str
    url: str
    domain: str
    path: str
    secure: bool
    http_only: bool
    same_site: 'CookieSameSite'
    expires: 'TimeSinceEpoch'
    priority: 'CookiePriority'
    same_party: bool
    source_scheme: 'CookieSourceScheme'
    source_port: int
    partition_key: str


class SetCookiesParamsT(TypedDict):
    cookies: list


class SetExtraHTTPHeadersParamsT(TypedDict):
    headers: 'Headers'


class SetAttachDebugStackParamsT(TypedDict):
    enabled: bool


class SetRequestInterceptionParamsT(TypedDict):
    patterns: list


class SetUserAgentOverrideParamsT(TypedDict):
    user_agent: str
    accept_language: str
    platform: str
    user_agent_metadata: 'emulation.UserAgentMetadata'


class GetSecurityIsolationStatusParamsT(TypedDict):
    frame_id: 'page.FrameId'


class EnableReportingApiParamsT(TypedDict):
    enable: bool


class LoadNetworkResourceParamsT(TypedDict):
    frame_id: 'page.FrameId'
    url: str
    options: 'LoadNetworkResourceOptions'


class CanClearBrowserCacheReturnT(TypedDict):
    result: bool


class CanClearBrowserCookiesReturnT(TypedDict):
    result: bool


class CanEmulateNetworkConditionsReturnT(TypedDict):
    result: bool


class GetAllCookiesReturnT(TypedDict):
    cookies: list


class GetCertificateReturnT(TypedDict):
    table_names: list


class GetCookiesReturnT(TypedDict):
    cookies: list


class GetResponseBodyReturnT(TypedDict):
    body: str
    base64_encoded: bool


class GetRequestPostDataReturnT(TypedDict):
    post_data: str


class GetResponseBodyForInterceptionReturnT(TypedDict):
    body: str
    base64_encoded: bool


class TakeResponseBodyForInterceptionAsStreamReturnT(TypedDict):
    stream: 'io.StreamHandle'


class SearchInResponseBodyReturnT(TypedDict):
    result: list


class SetCookieReturnT(TypedDict):
    success: bool


class GetSecurityIsolationStatusReturnT(TypedDict):
    status: 'SecurityIsolationStatus'


class LoadNetworkResourceReturnT(TypedDict):
    resource: 'LoadNetworkResourcePageResult'


class DataReceivedEventT(TypedDict):
    name: Literal['data_received']
    params: 'DataReceivedParamsT'


class EventSourceMessageReceivedEventT(TypedDict):
    name: Literal['event_source_message_received']
    params: 'EventSourceMessageReceivedParamsT'


class LoadingFailedEventT(TypedDict):
    name: Literal['loading_failed']
    params: 'LoadingFailedParamsT'


class LoadingFinishedEventT(TypedDict):
    name: Literal['loading_finished']
    params: 'LoadingFinishedParamsT'


class RequestInterceptedEventT(TypedDict):
    name: Literal['request_intercepted']
    params: 'RequestInterceptedParamsT'


class RequestServedFromCacheEventT(TypedDict):
    name: Literal['request_served_from_cache']
    params: 'RequestServedFromCacheParamsT'


class RequestWillBeSentEventT(TypedDict):
    name: Literal['request_will_be_sent']
    params: 'RequestWillBeSentParamsT'


class ResourceChangedPriorityEventT(TypedDict):
    name: Literal['resource_changed_priority']
    params: 'ResourceChangedPriorityParamsT'


class SignedExchangeReceivedEventT(TypedDict):
    name: Literal['signed_exchange_received']
    params: 'SignedExchangeReceivedParamsT'


class ResponseReceivedEventT(TypedDict):
    name: Literal['response_received']
    params: 'ResponseReceivedParamsT'


class WebSocketClosedEventT(TypedDict):
    name: Literal['web_socket_closed']
    params: 'WebSocketClosedParamsT'


class WebSocketCreatedEventT(TypedDict):
    name: Literal['web_socket_created']
    params: 'WebSocketCreatedParamsT'


class WebSocketFrameErrorEventT(TypedDict):
    name: Literal['web_socket_frame_error']
    params: 'WebSocketFrameErrorParamsT'


class WebSocketFrameReceivedEventT(TypedDict):
    name: Literal['web_socket_frame_received']
    params: 'WebSocketFrameReceivedParamsT'


class WebSocketFrameSentEventT(TypedDict):
    name: Literal['web_socket_frame_sent']
    params: 'WebSocketFrameSentParamsT'


class WebSocketHandshakeResponseReceivedEventT(TypedDict):
    name: Literal['web_socket_handshake_response_received']
    params: 'WebSocketHandshakeResponseReceivedParamsT'


class WebSocketWillSendHandshakeRequestEventT(TypedDict):
    name: Literal['web_socket_will_send_handshake_request']
    params: 'WebSocketWillSendHandshakeRequestParamsT'


class WebTransportCreatedEventT(TypedDict):
    name: Literal['web_transport_created']
    params: 'WebTransportCreatedParamsT'


class WebTransportConnectionEstablishedEventT(TypedDict):
    name: Literal['web_transport_connection_established']
    params: 'WebTransportConnectionEstablishedParamsT'


class WebTransportClosedEventT(TypedDict):
    name: Literal['web_transport_closed']
    params: 'WebTransportClosedParamsT'


class RequestWillBeSentExtraInfoEventT(TypedDict):
    name: Literal['request_will_be_sent_extra_info']
    params: 'RequestWillBeSentExtraInfoParamsT'


class ResponseReceivedExtraInfoEventT(TypedDict):
    name: Literal['response_received_extra_info']
    params: 'ResponseReceivedExtraInfoParamsT'


class TrustTokenOperationDoneEventT(TypedDict):
    name: Literal['trust_token_operation_done']
    params: 'TrustTokenOperationDoneParamsT'


class SubresourceWebBundleMetadataReceivedEventT(TypedDict):
    name: Literal['subresource_web_bundle_metadata_received']
    params: 'SubresourceWebBundleMetadataReceivedParamsT'


class SubresourceWebBundleMetadataErrorEventT(TypedDict):
    name: Literal['subresource_web_bundle_metadata_error']
    params: 'SubresourceWebBundleMetadataErrorParamsT'


class SubresourceWebBundleInnerResponseParsedEventT(TypedDict):
    name: Literal['subresource_web_bundle_inner_response_parsed']
    params: 'SubresourceWebBundleInnerResponseParsedParamsT'


class SubresourceWebBundleInnerResponseErrorEventT(TypedDict):
    name: Literal['subresource_web_bundle_inner_response_error']
    params: 'SubresourceWebBundleInnerResponseErrorParamsT'


class ReportingApiReportAddedEventT(TypedDict):
    name: Literal['reporting_api_report_added']
    params: 'ReportingApiReportAddedParamsT'


class ReportingApiReportUpdatedEventT(TypedDict):
    name: Literal['reporting_api_report_updated']
    params: 'ReportingApiReportUpdatedParamsT'


class ReportingApiEndpointsChangedForOriginEventT(TypedDict):
    name: Literal['reporting_api_endpoints_changed_for_origin']
    params: 'ReportingApiEndpointsChangedForOriginParamsT'


class DataReceivedParamsT(TypedDict):
    request_id: 'RequestId'
    timestamp: 'MonotonicTime'
    data_length: int
    encoded_data_length: int


class EventSourceMessageReceivedParamsT(TypedDict):
    request_id: 'RequestId'
    timestamp: 'MonotonicTime'
    event_name: str
    event_id: str
    data: str


class LoadingFailedParamsT(TypedDict):
    request_id: 'RequestId'
    timestamp: 'MonotonicTime'
    type: 'ResourceType'
    error_text: str
    canceled: bool
    blocked_reason: 'BlockedReason'
    cors_error_status: 'CorsErrorStatus'


class LoadingFinishedParamsT(TypedDict):
    request_id: 'RequestId'
    timestamp: 'MonotonicTime'
    encoded_data_length: float


class RequestInterceptedParamsT(TypedDict):
    interception_id: 'InterceptionId'
    request: 'Request'
    frame_id: 'page.FrameId'
    resource_type: 'ResourceType'
    is_navigation_request: bool
    is_download: bool
    redirect_url: str
    auth_challenge: 'AuthChallenge'
    response_error_reason: 'ErrorReason'
    response_status_code: int
    response_headers: 'Headers'
    request_id: 'RequestId'


class RequestServedFromCacheParamsT(TypedDict):
    request_id: 'RequestId'


class RequestWillBeSentParamsT(TypedDict):
    request_id: 'RequestId'
    loader_id: 'LoaderId'
    document_url: str
    request: 'Request'
    timestamp: 'MonotonicTime'
    wall_time: 'TimeSinceEpoch'
    initiator: 'Initiator'
    redirect_has_extra_info: bool
    redirect_response: 'Response'
    type: 'ResourceType'
    frame_id: 'page.FrameId'
    has_user_gesture: bool


class ResourceChangedPriorityParamsT(TypedDict):
    request_id: 'RequestId'
    new_priority: 'ResourcePriority'
    timestamp: 'MonotonicTime'


class SignedExchangeReceivedParamsT(TypedDict):
    request_id: 'RequestId'
    info: 'SignedExchangeInfo'


class ResponseReceivedParamsT(TypedDict):
    request_id: 'RequestId'
    loader_id: 'LoaderId'
    timestamp: 'MonotonicTime'
    type: 'ResourceType'
    response: 'Response'
    has_extra_info: bool
    frame_id: 'page.FrameId'


class WebSocketClosedParamsT(TypedDict):
    request_id: 'RequestId'
    timestamp: 'MonotonicTime'


class WebSocketCreatedParamsT(TypedDict):
    request_id: 'RequestId'
    url: str
    initiator: 'Initiator'


class WebSocketFrameErrorParamsT(TypedDict):
    request_id: 'RequestId'
    timestamp: 'MonotonicTime'
    error_message: str


class WebSocketFrameReceivedParamsT(TypedDict):
    request_id: 'RequestId'
    timestamp: 'MonotonicTime'
    response: 'WebSocketFrame'


class WebSocketFrameSentParamsT(TypedDict):
    request_id: 'RequestId'
    timestamp: 'MonotonicTime'
    response: 'WebSocketFrame'


class WebSocketHandshakeResponseReceivedParamsT(TypedDict):
    request_id: 'RequestId'
    timestamp: 'MonotonicTime'
    response: 'WebSocketResponse'


class WebSocketWillSendHandshakeRequestParamsT(TypedDict):
    request_id: 'RequestId'
    timestamp: 'MonotonicTime'
    wall_time: 'TimeSinceEpoch'
    request: 'WebSocketRequest'


class WebTransportCreatedParamsT(TypedDict):
    transport_id: 'RequestId'
    url: str
    timestamp: 'MonotonicTime'
    initiator: 'Initiator'


class WebTransportConnectionEstablishedParamsT(TypedDict):
    transport_id: 'RequestId'
    timestamp: 'MonotonicTime'


class WebTransportClosedParamsT(TypedDict):
    transport_id: 'RequestId'
    timestamp: 'MonotonicTime'


class RequestWillBeSentExtraInfoParamsT(TypedDict):
    request_id: 'RequestId'
    associated_cookies: list
    headers: 'Headers'
    connect_timing: 'ConnectTiming'
    client_security_state: 'ClientSecurityState'
    site_has_cookie_in_other_partition: bool


class ResponseReceivedExtraInfoParamsT(TypedDict):
    request_id: 'RequestId'
    blocked_cookies: list
    headers: 'Headers'
    resource_ip_address_space: 'IPAddressSpace'
    status_code: int
    headers_text: str
    cookie_partition_key: str
    cookie_partition_key_opaque: bool


class TrustTokenOperationDoneParamsT(TypedDict):
    status: str
    type: 'TrustTokenOperationType'
    request_id: 'RequestId'
    top_level_origin: str
    issuer_origin: str
    issued_token_count: int


class SubresourceWebBundleMetadataReceivedParamsT(TypedDict):
    request_id: 'RequestId'
    urls: list


class SubresourceWebBundleMetadataErrorParamsT(TypedDict):
    request_id: 'RequestId'
    error_message: str


class SubresourceWebBundleInnerResponseParsedParamsT(TypedDict):
    inner_request_id: 'RequestId'
    inner_request_url: str
    bundle_request_id: 'RequestId'


class SubresourceWebBundleInnerResponseErrorParamsT(TypedDict):
    inner_request_id: 'RequestId'
    inner_request_url: str
    error_message: str
    bundle_request_id: 'RequestId'


class ReportingApiReportAddedParamsT(TypedDict):
    report: 'ReportingApiReport'


class ReportingApiReportUpdatedParamsT(TypedDict):
    report: 'ReportingApiReport'


class ReportingApiEndpointsChangedForOriginParamsT(TypedDict):
    origin: str
    endpoints: list
