# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from cdp.generated.types import (
    dom,
    network,
    page,
    runtime
)
from typing import (
    Literal,
    TypedDict
)

IssueId = str

CookieExclusionReason = Literal[
    'ExcludeSameSiteUnspecifiedTreatedAsLax',
    'ExcludeSameSiteNoneInsecure',
    'ExcludeSameSiteLax',
    'ExcludeSameSiteStrict',
    'ExcludeInvalidSameParty',
    'ExcludeSamePartyCrossPartyContext',
    'ExcludeDomainNonASCII',
    'ExcludeThirdPartyCookieBlockedInFirstPartySet',
    'ExcludeThirdPartyPhaseout'
]

CookieWarningReason = Literal[
    'WarnSameSiteUnspecifiedCrossSiteContext',
    'WarnSameSiteNoneInsecure',
    'WarnSameSiteUnspecifiedLaxAllowUnsafe',
    'WarnSameSiteStrictLaxDowngradeStrict',
    'WarnSameSiteStrictCrossDowngradeStrict',
    'WarnSameSiteStrictCrossDowngradeLax',
    'WarnSameSiteLaxCrossDowngradeStrict',
    'WarnSameSiteLaxCrossDowngradeLax',
    'WarnAttributeValueExceedsMaxSize',
    'WarnDomainNonASCII',
    'WarnThirdPartyPhaseout'
]

CookieOperation = Literal[
    'SetCookie',
    'ReadCookie'
]

MixedContentResolutionStatus = Literal[
    'MixedContentBlocked',
    'MixedContentAutomaticallyUpgraded',
    'MixedContentWarning'
]

MixedContentResourceType = Literal[
    'AttributionSrc',
    'Audio',
    'Beacon',
    'CSPReport',
    'Download',
    'EventSource',
    'Favicon',
    'Font',
    'Form',
    'Frame',
    'Image',
    'Import',
    'Manifest',
    'Ping',
    'PluginData',
    'PluginResource',
    'Prefetch',
    'Resource',
    'Script',
    'ServiceWorker',
    'SharedWorker',
    'Stylesheet',
    'Track',
    'Video',
    'Worker',
    'XMLHttpRequest',
    'XSLT'
]

BlockedByResponseReason = Literal[
    'CoepFrameResourceNeedsCoepHeader',
    'CoopSandboxedIFrameCannotNavigateToCoopPage',
    'CorpNotSameOrigin',
    'CorpNotSameOriginAfterDefaultedToSameOriginByCoep',
    'CorpNotSameSite'
]

HeavyAdResolutionStatus = Literal[
    'HeavyAdBlocked',
    'HeavyAdWarning'
]

HeavyAdReason = Literal[
    'NetworkTotalLimit',
    'CpuTotalLimit',
    'CpuPeakLimit'
]

ContentSecurityPolicyViolationType = Literal[
    'kInlineViolation',
    'kEvalViolation',
    'kURLViolation',
    'kTrustedTypesSinkViolation',
    'kTrustedTypesPolicyViolation',
    'kWasmEvalViolation'
]

SharedArrayBufferIssueType = Literal[
    'TransferIssue',
    'CreationIssue'
]

AttributionReportingIssueType = Literal[
    'PermissionPolicyDisabled',
    'UntrustworthyReportingOrigin',
    'InsecureContext',
    'InvalidHeader',
    'InvalidRegisterTriggerHeader',
    'SourceAndTriggerHeaders',
    'SourceIgnored',
    'TriggerIgnored',
    'OsSourceIgnored',
    'OsTriggerIgnored',
    'InvalidRegisterOsSourceHeader',
    'InvalidRegisterOsTriggerHeader',
    'WebAndOsHeaders',
    'NoWebOrOsSupport',
    'NavigationRegistrationWithoutTransientUserActivation'
]

GenericIssueErrorType = Literal[
    'CrossOriginPortalPostMessageError',
    'FormLabelForNameError',
    'FormDuplicateIdForInputError',
    'FormInputWithNoLabelError',
    'FormAutocompleteAttributeEmptyError',
    'FormEmptyIdAndNameAttributesForInputError',
    'FormAriaLabelledByToNonExistingId',
    'FormInputAssignedAutocompleteValueToIdOrNameAttributeError',
    'FormLabelHasNeitherForNorNestedInput',
    'FormLabelForMatchesNonExistingIdError',
    'FormInputHasWrongButWellIntendedAutocompleteValueError',
    'ResponseWasBlockedByORB'
]

ClientHintIssueReason = Literal[
    'MetaTagAllowListInvalidOrigin',
    'MetaTagModifiedHTML'
]

FederatedAuthRequestIssueReason = Literal[
    'ShouldEmbargo',
    'TooManyRequests',
    'WellKnownHttpNotFound',
    'WellKnownNoResponse',
    'WellKnownInvalidResponse',
    'WellKnownListEmpty',
    'WellKnownInvalidContentType',
    'ConfigNotInWellKnown',
    'WellKnownTooBig',
    'ConfigHttpNotFound',
    'ConfigNoResponse',
    'ConfigInvalidResponse',
    'ConfigInvalidContentType',
    'ClientMetadataHttpNotFound',
    'ClientMetadataNoResponse',
    'ClientMetadataInvalidResponse',
    'ClientMetadataInvalidContentType',
    'DisabledInSettings',
    'ErrorFetchingSignin',
    'InvalidSigninResponse',
    'AccountsHttpNotFound',
    'AccountsNoResponse',
    'AccountsInvalidResponse',
    'AccountsListEmpty',
    'AccountsInvalidContentType',
    'IdTokenHttpNotFound',
    'IdTokenNoResponse',
    'IdTokenInvalidResponse',
    'IdTokenInvalidRequest',
    'IdTokenInvalidContentType',
    'ErrorIdToken',
    'Canceled',
    'RpPageNotVisible',
    'SilentMediationFailure',
    'ThirdPartyCookiesBlocked'
]

FederatedAuthUserInfoRequestIssueReason = Literal[
    'NotSameOrigin',
    'NotIframe',
    'NotPotentiallyTrustworthy',
    'NoApiPermission',
    'NotSignedInWithIdp',
    'NoAccountSharingPermission',
    'InvalidConfigOrWellKnown',
    'InvalidAccountsResponse',
    'NoReturningUserFromFetchedAccounts'
]

StyleSheetLoadingIssueReason = Literal[
    'LateImportRule',
    'RequestFailed'
]

InspectorIssueCode = Literal[
    'CookieIssue',
    'MixedContentIssue',
    'BlockedByResponseIssue',
    'HeavyAdIssue',
    'ContentSecurityPolicyIssue',
    'SharedArrayBufferIssue',
    'LowTextContrastIssue',
    'CorsIssue',
    'AttributionReportingIssue',
    'QuirksModeIssue',
    'NavigatorUserAgentIssue',
    'GenericIssue',
    'DeprecationIssue',
    'ClientHintIssue',
    'FederatedAuthRequestIssue',
    'BounceTrackingIssue',
    'StylesheetLoadingIssue',
    'FederatedAuthUserInfoRequestIssue'
]


class AffectedCookie(TypedDict):
    name: str
    path: str
    domain: str


class AffectedRequest(TypedDict):
    request_id: 'network.RequestId'
    url: str


class AffectedFrame(TypedDict):
    frame_id: 'page.FrameId'


class CookieIssueDetails(TypedDict):
    cookie_warning_reasons: list
    cookie_exclusion_reasons: list
    operation: 'CookieOperation'
    cookie: 'AffectedCookie'
    raw_cookie_line: str
    site_for_cookies: str
    cookie_url: str
    request: 'AffectedRequest'


class MixedContentIssueDetails(TypedDict):
    resolution_status: 'MixedContentResolutionStatus'
    insecure_url: str
    main_resource_url: str
    resource_type: 'MixedContentResourceType'
    request: 'AffectedRequest'
    frame: 'AffectedFrame'


class BlockedByResponseIssueDetails(TypedDict):
    request: 'AffectedRequest'
    reason: 'BlockedByResponseReason'
    parent_frame: 'AffectedFrame'
    blocked_frame: 'AffectedFrame'


class HeavyAdIssueDetails(TypedDict):
    resolution: 'HeavyAdResolutionStatus'
    reason: 'HeavyAdReason'
    frame: 'AffectedFrame'


class SourceCodeLocation(TypedDict):
    url: str
    line_number: int
    column_number: int
    script_id: 'runtime.ScriptId'


class ContentSecurityPolicyIssueDetails(TypedDict):
    violated_directive: str
    is_report_only: bool
    content_security_policy_violation_type: 'ContentSecurityPolicyViolationType'
    blocked_url: str
    frame_ancestor: 'AffectedFrame'
    source_code_location: 'SourceCodeLocation'
    violating_node_id: 'dom.BackendNodeId'


class SharedArrayBufferIssueDetails(TypedDict):
    source_code_location: 'SourceCodeLocation'
    is_warning: bool
    type: 'SharedArrayBufferIssueType'


class LowTextContrastIssueDetails(TypedDict):
    violating_node_id: 'dom.BackendNodeId'
    violating_node_selector: str
    contrast_ratio: float
    threshold_aa: float
    threshold_aaa: float
    font_size: str
    font_weight: str


class CorsIssueDetails(TypedDict):
    cors_error_status: 'network.CorsErrorStatus'
    is_warning: bool
    request: 'AffectedRequest'
    location: 'SourceCodeLocation'
    initiator_origin: str
    resource_ip_address_space: 'network.IPAddressSpace'
    client_security_state: 'network.ClientSecurityState'


class AttributionReportingIssueDetails(TypedDict):
    violation_type: 'AttributionReportingIssueType'
    request: 'AffectedRequest'
    violating_node_id: 'dom.BackendNodeId'
    invalid_parameter: str


class QuirksModeIssueDetails(TypedDict):
    is_limited_quirks_mode: bool
    document_node_id: 'dom.BackendNodeId'
    url: str
    frame_id: 'page.FrameId'
    loader_id: 'network.LoaderId'


class NavigatorUserAgentIssueDetails(TypedDict):
    url: str
    location: 'SourceCodeLocation'


class GenericIssueDetails(TypedDict):
    error_type: 'GenericIssueErrorType'
    frame_id: 'page.FrameId'
    violating_node_id: 'dom.BackendNodeId'
    violating_node_attribute: str
    request: 'AffectedRequest'


class DeprecationIssueDetails(TypedDict):
    source_code_location: 'SourceCodeLocation'
    type: str
    affected_frame: 'AffectedFrame'


class BounceTrackingIssueDetails(TypedDict):
    tracking_sites: list


class FederatedAuthRequestIssueDetails(TypedDict):
    federated_auth_request_issue_reason: 'FederatedAuthRequestIssueReason'


class FederatedAuthUserInfoRequestIssueDetails(TypedDict):
    federated_auth_user_info_request_issue_reason: 'FederatedAuthUserInfoRequestIssueReason'


class ClientHintIssueDetails(TypedDict):
    source_code_location: 'SourceCodeLocation'
    client_hint_issue_reason: 'ClientHintIssueReason'


class FailedRequestInfo(TypedDict):
    url: str
    failure_message: str
    request_id: 'network.RequestId'


class StylesheetLoadingIssueDetails(TypedDict):
    source_code_location: 'SourceCodeLocation'
    style_sheet_loading_issue_reason: 'StyleSheetLoadingIssueReason'
    failed_request_info: 'FailedRequestInfo'


class InspectorIssueDetails(TypedDict):
    cookie_issue_details: 'CookieIssueDetails'
    mixed_content_issue_details: 'MixedContentIssueDetails'
    blocked_by_response_issue_details: 'BlockedByResponseIssueDetails'
    heavy_ad_issue_details: 'HeavyAdIssueDetails'
    content_security_policy_issue_details: 'ContentSecurityPolicyIssueDetails'
    shared_array_buffer_issue_details: 'SharedArrayBufferIssueDetails'
    low_text_contrast_issue_details: 'LowTextContrastIssueDetails'
    cors_issue_details: 'CorsIssueDetails'
    attribution_reporting_issue_details: 'AttributionReportingIssueDetails'
    quirks_mode_issue_details: 'QuirksModeIssueDetails'
    navigator_user_agent_issue_details: 'NavigatorUserAgentIssueDetails'
    generic_issue_details: 'GenericIssueDetails'
    deprecation_issue_details: 'DeprecationIssueDetails'
    client_hint_issue_details: 'ClientHintIssueDetails'
    federated_auth_request_issue_details: 'FederatedAuthRequestIssueDetails'
    bounce_tracking_issue_details: 'BounceTrackingIssueDetails'
    stylesheet_loading_issue_details: 'StylesheetLoadingIssueDetails'
    federated_auth_user_info_request_issue_details: 'FederatedAuthUserInfoRequestIssueDetails'


class InspectorIssue(TypedDict):
    code: 'InspectorIssueCode'
    details: 'InspectorIssueDetails'
    issue_id: 'IssueId'


class GetEncodedResponseParamsT(TypedDict):
    request_id: 'network.RequestId'
    encoding: str
    quality: float
    size_only: bool


class CheckContrastParamsT(TypedDict):
    report_aaa: bool


class GetEncodedResponseReturnT(TypedDict):
    body: str
    original_size: int
    encoded_size: int


class CheckFormsIssuesReturnT(TypedDict):
    form_issues: list


class IssueAddedEventT(TypedDict):
    name: Literal['issue_added']
    params: 'IssueAddedParamsT'


class IssueAddedParamsT(TypedDict):
    issue: 'InspectorIssue'
