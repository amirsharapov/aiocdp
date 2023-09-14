from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

AlternateProtocolUsage = Literal[
    "alternativeJobWonWithoutRace",
    "alternativeJobWonRace",
    "mainJobWonRace",
    "mappingMissing",
    "broken",
    "dnsAlpnH3JobWonWithoutRace",
    "dnsAlpnH3JobWonRace",
    "unspecifiedReason"
]

BlockedReason = Literal[
    "other",
    "csp",
    "mixed-content",
    "origin",
    "inspector",
    "subresource-filter",
    "content-type",
    "coep-frame-resource-needs-coep-header",
    "coop-sandboxed-iframe-cannot-navigate-to-coop-page",
    "corp-not-same-origin",
    "corp-not-same-origin-after-defaulted-to-same-origin-by-coep",
    "corp-not-same-site"
]

CertificateTransparencyCompliance = Literal[
    "unknown",
    "not-compliant",
    "compliant"
]

ConnectionType = Literal[
    "none",
    "cellular2g",
    "cellular3g",
    "cellular4g",
    "bluetooth",
    "ethernet",
    "wifi",
    "wimax",
    "other"
]

ContentEncoding = Literal[
    "deflate",
    "gzip",
    "br",
    "zstd"
]

ContentSecurityPolicySource = Literal[
    "HTTP",
    "Meta"
]

CookieBlockedReason = Literal[
    "SecureOnly",
    "NotOnPath",
    "DomainMismatch",
    "SameSiteStrict",
    "SameSiteLax",
    "SameSiteUnspecifiedTreatedAsLax",
    "SameSiteNoneInsecure",
    "UserPreferences",
    "ThirdPartyBlockedInFirstPartySet",
    "UnknownError",
    "SchemefulSameSiteStrict",
    "SchemefulSameSiteLax",
    "SchemefulSameSiteUnspecifiedTreatedAsLax",
    "SamePartyFromCrossPartyContext",
    "NameValuePairExceedsMaxSize"
]

CookiePriority = Literal[
    "Low",
    "Medium",
    "High"
]

CookieSameSite = Literal[
    "Strict",
    "Lax",
    "None"
]

CookieSourceScheme = Literal[
    "Unset",
    "NonSecure",
    "Secure"
]

CorsError = Literal[
    "DisallowedByMode",
    "InvalidResponse",
    "WildcardOriginNotAllowed",
    "MissingAllowOriginHeader",
    "MultipleAllowOriginValues",
    "InvalidAllowOriginValue",
    "AllowOriginMismatch",
    "InvalidAllowCredentials",
    "CorsDisabledScheme",
    "PreflightInvalidStatus",
    "PreflightDisallowedRedirect",
    "PreflightWildcardOriginNotAllowed",
    "PreflightMissingAllowOriginHeader",
    "PreflightMultipleAllowOriginValues",
    "PreflightInvalidAllowOriginValue",
    "PreflightAllowOriginMismatch",
    "PreflightInvalidAllowCredentials",
    "PreflightMissingAllowExternal",
    "PreflightInvalidAllowExternal",
    "PreflightMissingAllowPrivateNetwork",
    "PreflightInvalidAllowPrivateNetwork",
    "InvalidAllowMethodsPreflightResponse",
    "InvalidAllowHeadersPreflightResponse",
    "MethodDisallowedByPreflightResponse",
    "HeaderDisallowedByPreflightResponse",
    "RedirectContainsCredentials",
    "InsecurePrivateNetwork",
    "InvalidPrivateNetworkAccess",
    "UnexpectedPrivateNetworkAccess",
    "NoCorsRedirectModeNotFollow",
    "PreflightMissingPrivateNetworkAccessId",
    "PreflightMissingPrivateNetworkAccessName",
    "PrivateNetworkAccessPermissionUnavailable",
    "PrivateNetworkAccessPermissionDenied"
]

CrossOriginEmbedderPolicyValue = Literal[
    "None",
    "Credentialless",
    "RequireCorp"
]

CrossOriginOpenerPolicyValue = Literal[
    "SameOrigin",
    "SameOriginAllowPopups",
    "RestrictProperties",
    "UnsafeNone",
    "SameOriginPlusCoep",
    "RestrictPropertiesPlusCoep"
]

ErrorReason = Literal[
    "Failed",
    "Aborted",
    "TimedOut",
    "AccessDenied",
    "ConnectionClosed",
    "ConnectionReset",
    "ConnectionRefused",
    "ConnectionAborted",
    "ConnectionFailed",
    "NameNotResolved",
    "InternetDisconnected",
    "AddressUnreachable",
    "BlockedByClient",
    "BlockedByResponse"
]

IPAddressSpace = Literal[
    "Local",
    "Private",
    "Public",
    "Unknown"
]

InterceptionStage = Literal[
    "Request",
    "HeadersReceived"
]

PrivateNetworkRequestPolicy = Literal[
    "Allow",
    "BlockFromInsecureToMorePrivate",
    "WarnFromInsecureToMorePrivate",
    "PreflightBlock",
    "PreflightWarn"
]

ReportStatus = Literal[
    "Queued",
    "Pending",
    "MarkedForRemoval",
    "Success"
]

ResourcePriority = Literal[
    "VeryLow",
    "Low",
    "Medium",
    "High",
    "VeryHigh"
]

ResourceType = Literal[
    "Document",
    "Stylesheet",
    "Image",
    "Media",
    "Font",
    "Script",
    "TextTrack",
    "XHR",
    "Fetch",
    "Prefetch",
    "EventSource",
    "WebSocket",
    "Manifest",
    "SignedExchange",
    "Ping",
    "CSPViolationReport",
    "Preflight",
    "Other"
]

ServiceWorkerResponseSource = Literal[
    "cache-storage",
    "http-cache",
    "fallback-code",
    "network"
]

SetCookieBlockedReason = Literal[
    "SecureOnly",
    "SameSiteStrict",
    "SameSiteLax",
    "SameSiteUnspecifiedTreatedAsLax",
    "SameSiteNoneInsecure",
    "UserPreferences",
    "ThirdPartyBlockedInFirstPartySet",
    "SyntaxError",
    "SchemeNotSupported",
    "OverwriteSecure",
    "InvalidDomain",
    "InvalidPrefix",
    "UnknownError",
    "SchemefulSameSiteStrict",
    "SchemefulSameSiteLax",
    "SchemefulSameSiteUnspecifiedTreatedAsLax",
    "SamePartyFromCrossPartyContext",
    "SamePartyConflictsWithOtherAttributes",
    "NameValuePairExceedsMaxSize",
    "DisallowedCharacter"
]

SignedExchangeErrorField = Literal[
    "signatureSig",
    "signatureIntegrity",
    "signatureCertUrl",
    "signatureCertSha256",
    "signatureValidityUrl",
    "signatureTimestamps"
]

TrustTokenOperationType = Literal[
    "Issuance",
    "Redemption",
    "Signing"
]


@dataclass
class AuthChallenge:
    source: str
    origin: str
    scheme: str
    realm: str


@dataclass
class AuthChallengeResponse:
    response: str
    username: str
    password: str


@dataclass
class BlockedCookieWithReason:
    blockedReasons: list
    cookie: Cookie


@dataclass
class BlockedSetCookieWithReason:
    blockedReasons: list
    cookieLine: str
    cookie: Cookie


@dataclass
class CachedResource:
    url: str
    type: ResourceType
    response: Response
    bodySize: float


@dataclass
class ClientSecurityState:
    initiatorIsSecureContext: bool
    initiatorIPAddressSpace: IPAddressSpace
    privateNetworkRequestPolicy: PrivateNetworkRequestPolicy


@dataclass
class ConnectTiming:
    requestTime: float


@dataclass
class ContentSecurityPolicyStatus:
    effectiveDirectives: str
    isEnforced: bool
    source: ContentSecurityPolicySource


@dataclass
class Cookie:
    name: str
    value: str
    domain: str
    path: str
    expires: float
    size: int
    httpOnly: bool
    secure: bool
    session: bool
    sameSite: CookieSameSite
    priority: CookiePriority
    sameParty: bool
    sourceScheme: CookieSourceScheme
    sourcePort: int
    partitionKey: str
    partitionKeyOpaque: bool


@dataclass
class CookieParam:
    name: str
    value: str
    url: str
    domain: str
    path: str
    secure: bool
    httpOnly: bool
    sameSite: CookieSameSite
    expires: TimeSinceEpoch
    priority: CookiePriority
    sameParty: bool
    sourceScheme: CookieSourceScheme
    sourcePort: int
    partitionKey: str


@dataclass
class CorsErrorStatus:
    corsError: CorsError
    failedParameter: str


@dataclass
class CrossOriginEmbedderPolicyStatus:
    value: CrossOriginEmbedderPolicyValue
    reportOnlyValue: CrossOriginEmbedderPolicyValue
    reportingEndpoint: str
    reportOnlyReportingEndpoint: str


@dataclass
class CrossOriginOpenerPolicyStatus:
    value: CrossOriginOpenerPolicyValue
    reportOnlyValue: CrossOriginOpenerPolicyValue
    reportingEndpoint: str
    reportOnlyReportingEndpoint: str


@dataclass
class Initiator:
    type: str
    stack: StackTrace
    url: str
    lineNumber: float
    columnNumber: float
    requestId: RequestId


@dataclass
class LoadNetworkResourceOptions:
    disableCache: bool
    includeCredentials: bool


@dataclass
class LoadNetworkResourcePageResult:
    success: bool
    netError: float
    netErrorName: str
    httpStatusCode: float
    stream: StreamHandle
    headers: Headers


@dataclass
class PostDataEntry:
    bytes: str


@dataclass
class ReportingApiEndpoint:
    url: str
    groupName: str


@dataclass
class ReportingApiReport:
    id: ReportId
    initiatorUrl: str
    destination: str
    type: str
    timestamp: TimeSinceEpoch
    depth: int
    completedAttempts: int
    body: object
    status: ReportStatus


@dataclass
class Request:
    url: str
    urlFragment: str
    method: str
    headers: Headers
    postData: str
    hasPostData: bool
    postDataEntries: list
    mixedContentType: MixedContentType
    initialPriority: ResourcePriority
    referrerPolicy: str
    isLinkPreload: bool
    trustTokenParams: TrustTokenParams
    isSameSite: bool


@dataclass
class RequestPattern:
    urlPattern: str
    resourceType: ResourceType
    interceptionStage: InterceptionStage


@dataclass
class ResourceTiming:
    requestTime: float
    proxyStart: float
    proxyEnd: float
    dnsStart: float
    dnsEnd: float
    connectStart: float
    connectEnd: float
    sslStart: float
    sslEnd: float
    workerStart: float
    workerReady: float
    workerFetchStart: float
    workerRespondWithSettled: float
    sendStart: float
    sendEnd: float
    pushStart: float
    pushEnd: float
    receiveHeadersStart: float
    receiveHeadersEnd: float


@dataclass
class Response:
    url: str
    status: int
    statusText: str
    headers: Headers
    headersText: str
    mimeType: str
    requestHeaders: Headers
    requestHeadersText: str
    connectionReused: bool
    connectionId: float
    remoteIPAddress: str
    remotePort: int
    fromDiskCache: bool
    fromServiceWorker: bool
    fromPrefetchCache: bool
    encodedDataLength: float
    timing: ResourceTiming
    serviceWorkerResponseSource: ServiceWorkerResponseSource
    responseTime: TimeSinceEpoch
    cacheStorageCacheName: str
    protocol: str
    alternateProtocolUsage: AlternateProtocolUsage
    securityState: SecurityState
    securityDetails: SecurityDetails


@dataclass
class SecurityDetails:
    protocol: str
    keyExchange: str
    keyExchangeGroup: str
    cipher: str
    mac: str
    certificateId: CertificateId
    subjectName: str
    sanList: list
    issuer: str
    validFrom: TimeSinceEpoch
    validTo: TimeSinceEpoch
    signedCertificateTimestampList: list
    certificateTransparencyCompliance: CertificateTransparencyCompliance
    serverSignatureAlgorithm: int
    encryptedClientHello: bool


@dataclass
class SecurityIsolationStatus:
    coop: CrossOriginOpenerPolicyStatus
    coep: CrossOriginEmbedderPolicyStatus
    csp: list


@dataclass
class SignedCertificateTimestamp:
    status: str
    origin: str
    logDescription: str
    logId: str
    timestamp: float
    hashAlgorithm: str
    signatureAlgorithm: str
    signatureData: str


@dataclass
class SignedExchangeError:
    message: str
    signatureIndex: int
    errorField: SignedExchangeErrorField


@dataclass
class SignedExchangeHeader:
    requestUrl: str
    responseCode: int
    responseHeaders: Headers
    signatures: list
    headerIntegrity: str


@dataclass
class SignedExchangeInfo:
    outerResponse: Response
    header: SignedExchangeHeader
    securityDetails: SecurityDetails
    errors: list


@dataclass
class SignedExchangeSignature:
    label: str
    signature: str
    integrity: str
    certUrl: str
    certSha256: str
    validityUrl: str
    date: int
    expires: int
    certificates: list


@dataclass
class TrustTokenParams:
    operation: TrustTokenOperationType
    refreshPolicy: str
    issuers: list


@dataclass
class WebSocketFrame:
    opcode: float
    mask: bool
    payloadData: str


@dataclass
class WebSocketRequest:
    headers: Headers


@dataclass
class WebSocketResponse:
    status: int
    statusText: str
    headers: Headers
    headersText: str
    requestHeaders: Headers
    requestHeadersText: str
