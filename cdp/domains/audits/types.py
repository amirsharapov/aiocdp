from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

AttributionReportingIssueType = Literal[
    "PermissionPolicyDisabled",
    "UntrustworthyReportingOrigin",
    "InsecureContext",
    "InvalidHeader",
    "InvalidRegisterTriggerHeader",
    "SourceAndTriggerHeaders",
    "SourceIgnored",
    "TriggerIgnored",
    "OsSourceIgnored",
    "OsTriggerIgnored",
    "InvalidRegisterOsSourceHeader",
    "InvalidRegisterOsTriggerHeader",
    "WebAndOsHeaders",
    "NoWebOrOsSupport",
    "NavigationRegistrationWithoutTransientUserActivation"
]

BlockedByResponseReason = Literal[
    "CoepFrameResourceNeedsCoepHeader",
    "CoopSandboxedIFrameCannotNavigateToCoopPage",
    "CorpNotSameOrigin",
    "CorpNotSameOriginAfterDefaultedToSameOriginByCoep",
    "CorpNotSameSite"
]

ClientHintIssueReason = Literal[
    "MetaTagAllowListInvalidOrigin",
    "MetaTagModifiedHTML"
]

ContentSecurityPolicyViolationType = Literal[
    "kInlineViolation",
    "kEvalViolation",
    "kURLViolation",
    "kTrustedTypesSinkViolation",
    "kTrustedTypesPolicyViolation",
    "kWasmEvalViolation"
]

CookieExclusionReason = Literal[
    "ExcludeSameSiteUnspecifiedTreatedAsLax",
    "ExcludeSameSiteNoneInsecure",
    "ExcludeSameSiteLax",
    "ExcludeSameSiteStrict",
    "ExcludeInvalidSameParty",
    "ExcludeSamePartyCrossPartyContext",
    "ExcludeDomainNonASCII",
    "ExcludeThirdPartyCookieBlockedInFirstPartySet",
    "ExcludeThirdPartyPhaseout"
]

CookieOperation = Literal[
    "SetCookie",
    "ReadCookie"
]

CookieWarningReason = Literal[
    "WarnSameSiteUnspecifiedCrossSiteContext",
    "WarnSameSiteNoneInsecure",
    "WarnSameSiteUnspecifiedLaxAllowUnsafe",
    "WarnSameSiteStrictLaxDowngradeStrict",
    "WarnSameSiteStrictCrossDowngradeStrict",
    "WarnSameSiteStrictCrossDowngradeLax",
    "WarnSameSiteLaxCrossDowngradeStrict",
    "WarnSameSiteLaxCrossDowngradeLax",
    "WarnAttributeValueExceedsMaxSize",
    "WarnDomainNonASCII",
    "WarnThirdPartyPhaseout"
]

FederatedAuthRequestIssueReason = Literal[
    "ShouldEmbargo",
    "TooManyRequests",
    "WellKnownHttpNotFound",
    "WellKnownNoResponse",
    "WellKnownInvalidResponse",
    "WellKnownListEmpty",
    "WellKnownInvalidContentType",
    "ConfigNotInWellKnown",
    "WellKnownTooBig",
    "ConfigHttpNotFound",
    "ConfigNoResponse",
    "ConfigInvalidResponse",
    "ConfigInvalidContentType",
    "ClientMetadataHttpNotFound",
    "ClientMetadataNoResponse",
    "ClientMetadataInvalidResponse",
    "ClientMetadataInvalidContentType",
    "DisabledInSettings",
    "ErrorFetchingSignin",
    "InvalidSigninResponse",
    "AccountsHttpNotFound",
    "AccountsNoResponse",
    "AccountsInvalidResponse",
    "AccountsListEmpty",
    "AccountsInvalidContentType",
    "IdTokenHttpNotFound",
    "IdTokenNoResponse",
    "IdTokenInvalidResponse",
    "IdTokenInvalidRequest",
    "IdTokenInvalidContentType",
    "ErrorIdToken",
    "Canceled",
    "RpPageNotVisible",
    "SilentMediationFailure",
    "ThirdPartyCookiesBlocked"
]

FederatedAuthUserInfoRequestIssueReason = Literal[
    "NotSameOrigin",
    "NotIframe",
    "NotPotentiallyTrustworthy",
    "NoApiPermission",
    "NotSignedInWithIdp",
    "NoAccountSharingPermission",
    "InvalidConfigOrWellKnown",
    "InvalidAccountsResponse",
    "NoReturningUserFromFetchedAccounts"
]

GenericIssueErrorType = Literal[
    "CrossOriginPortalPostMessageError",
    "FormLabelForNameError",
    "FormDuplicateIdForInputError",
    "FormInputWithNoLabelError",
    "FormAutocompleteAttributeEmptyError",
    "FormEmptyIdAndNameAttributesForInputError",
    "FormAriaLabelledByToNonExistingId",
    "FormInputAssignedAutocompleteValueToIdOrNameAttributeError",
    "FormLabelHasNeitherForNorNestedInput",
    "FormLabelForMatchesNonExistingIdError",
    "FormInputHasWrongButWellIntendedAutocompleteValueError",
    "ResponseWasBlockedByORB"
]

HeavyAdReason = Literal[
    "NetworkTotalLimit",
    "CpuTotalLimit",
    "CpuPeakLimit"
]

HeavyAdResolutionStatus = Literal[
    "HeavyAdBlocked",
    "HeavyAdWarning"
]

InspectorIssueCode = Literal[
    "CookieIssue",
    "MixedContentIssue",
    "BlockedByResponseIssue",
    "HeavyAdIssue",
    "ContentSecurityPolicyIssue",
    "SharedArrayBufferIssue",
    "LowTextContrastIssue",
    "CorsIssue",
    "AttributionReportingIssue",
    "QuirksModeIssue",
    "NavigatorUserAgentIssue",
    "GenericIssue",
    "DeprecationIssue",
    "ClientHintIssue",
    "FederatedAuthRequestIssue",
    "BounceTrackingIssue",
    "StylesheetLoadingIssue",
    "FederatedAuthUserInfoRequestIssue"
]

MixedContentResolutionStatus = Literal[
    "MixedContentBlocked",
    "MixedContentAutomaticallyUpgraded",
    "MixedContentWarning"
]

MixedContentResourceType = Literal[
    "AttributionSrc",
    "Audio",
    "Beacon",
    "CSPReport",
    "Download",
    "EventSource",
    "Favicon",
    "Font",
    "Form",
    "Frame",
    "Image",
    "Import",
    "Manifest",
    "Ping",
    "PluginData",
    "PluginResource",
    "Prefetch",
    "Resource",
    "Script",
    "ServiceWorker",
    "SharedWorker",
    "Stylesheet",
    "Track",
    "Video",
    "Worker",
    "XMLHttpRequest",
    "XSLT"
]

SharedArrayBufferIssueType = Literal[
    "TransferIssue",
    "CreationIssue"
]

StyleSheetLoadingIssueReason = Literal[
    "LateImportRule",
    "RequestFailed"
]


@dataclass
class AffectedCookie:
    name: str
    path: str
    domain: str


@dataclass
class AffectedFrame:
    frameId: FrameId


@dataclass
class AffectedRequest:
    requestId: RequestId
    url: str


@dataclass
class AttributionReportingIssueDetails:
    violationType: AttributionReportingIssueType
    request: AffectedRequest
    violatingNodeId: BackendNodeId
    invalidParameter: str


@dataclass
class BlockedByResponseIssueDetails:
    request: AffectedRequest
    parentFrame: AffectedFrame
    blockedFrame: AffectedFrame
    reason: BlockedByResponseReason


@dataclass
class BounceTrackingIssueDetails:
    trackingSites: list


@dataclass
class ClientHintIssueDetails:
    sourceCodeLocation: SourceCodeLocation
    clientHintIssueReason: ClientHintIssueReason


@dataclass
class ContentSecurityPolicyIssueDetails:
    blockedURL: str
    violatedDirective: str
    isReportOnly: bool
    contentSecurityPolicyViolationType: ContentSecurityPolicyViolationType
    frameAncestor: AffectedFrame
    sourceCodeLocation: SourceCodeLocation
    violatingNodeId: BackendNodeId


@dataclass
class CookieIssueDetails:
    cookie: AffectedCookie
    rawCookieLine: str
    cookieWarningReasons: list
    cookieExclusionReasons: list
    operation: CookieOperation
    siteForCookies: str
    cookieUrl: str
    request: AffectedRequest


@dataclass
class CorsIssueDetails:
    corsErrorStatus: CorsErrorStatus
    isWarning: bool
    request: AffectedRequest
    location: SourceCodeLocation
    initiatorOrigin: str
    resourceIPAddressSpace: IPAddressSpace
    clientSecurityState: ClientSecurityState


@dataclass
class DeprecationIssueDetails:
    affectedFrame: AffectedFrame
    sourceCodeLocation: SourceCodeLocation
    type: str


@dataclass
class FailedRequestInfo:
    url: str
    failureMessage: str
    requestId: RequestId


@dataclass
class FederatedAuthRequestIssueDetails:
    federatedAuthRequestIssueReason: FederatedAuthRequestIssueReason


@dataclass
class FederatedAuthUserInfoRequestIssueDetails:
    federatedAuthUserInfoRequestIssueReason: FederatedAuthUserInfoRequestIssueReason


@dataclass
class GenericIssueDetails:
    errorType: GenericIssueErrorType
    frameId: FrameId
    violatingNodeId: BackendNodeId
    violatingNodeAttribute: str
    request: AffectedRequest


@dataclass
class HeavyAdIssueDetails:
    resolution: HeavyAdResolutionStatus
    reason: HeavyAdReason
    frame: AffectedFrame


@dataclass
class InspectorIssue:
    code: InspectorIssueCode
    details: InspectorIssueDetails
    issueId: IssueId


@dataclass
class InspectorIssueDetails:
    cookieIssueDetails: CookieIssueDetails
    mixedContentIssueDetails: MixedContentIssueDetails
    blockedByResponseIssueDetails: BlockedByResponseIssueDetails
    heavyAdIssueDetails: HeavyAdIssueDetails
    contentSecurityPolicyIssueDetails: ContentSecurityPolicyIssueDetails
    sharedArrayBufferIssueDetails: SharedArrayBufferIssueDetails
    lowTextContrastIssueDetails: LowTextContrastIssueDetails
    corsIssueDetails: CorsIssueDetails
    attributionReportingIssueDetails: AttributionReportingIssueDetails
    quirksModeIssueDetails: QuirksModeIssueDetails
    navigatorUserAgentIssueDetails: NavigatorUserAgentIssueDetails
    genericIssueDetails: GenericIssueDetails
    deprecationIssueDetails: DeprecationIssueDetails
    clientHintIssueDetails: ClientHintIssueDetails
    federatedAuthRequestIssueDetails: FederatedAuthRequestIssueDetails
    bounceTrackingIssueDetails: BounceTrackingIssueDetails
    stylesheetLoadingIssueDetails: StylesheetLoadingIssueDetails
    federatedAuthUserInfoRequestIssueDetails: FederatedAuthUserInfoRequestIssueDetails


@dataclass
class LowTextContrastIssueDetails:
    violatingNodeId: BackendNodeId
    violatingNodeSelector: str
    contrastRatio: float
    thresholdAA: float
    thresholdAAA: float
    fontSize: str
    fontWeight: str


@dataclass
class MixedContentIssueDetails:
    resourceType: MixedContentResourceType
    resolutionStatus: MixedContentResolutionStatus
    insecureURL: str
    mainResourceURL: str
    request: AffectedRequest
    frame: AffectedFrame


@dataclass
class NavigatorUserAgentIssueDetails:
    url: str
    location: SourceCodeLocation


@dataclass
class QuirksModeIssueDetails:
    isLimitedQuirksMode: bool
    documentNodeId: BackendNodeId
    url: str
    frameId: FrameId
    loaderId: LoaderId


@dataclass
class SharedArrayBufferIssueDetails:
    sourceCodeLocation: SourceCodeLocation
    isWarning: bool
    type: SharedArrayBufferIssueType


@dataclass
class SourceCodeLocation:
    scriptId: ScriptId
    url: str
    lineNumber: int
    columnNumber: int


@dataclass
class StylesheetLoadingIssueDetails:
    sourceCodeLocation: SourceCodeLocation
    styleSheetLoadingIssueReason: StyleSheetLoadingIssueReason
    failedRequestInfo: FailedRequestInfo
