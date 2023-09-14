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
    CorsErrorStatus,
    RequestId,
    ClientSecurityState,
    LoaderId,
    IPAddressSpace
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.audits.types import (
    StylesheetLoadingIssueDetails,
    ContentSecurityPolicyViolationType,
    LowTextContrastIssueDetails,
    MixedContentIssueDetails,
    BlockedByResponseReason,
    BlockedByResponseIssueDetails,
    ClientHintIssueDetails,
    FailedRequestInfo,
    NavigatorUserAgentIssueDetails,
    ClientHintIssueReason,
    AffectedRequest,
    AttributionReportingIssueType,
    SharedArrayBufferIssueDetails,
    FederatedAuthUserInfoRequestIssueDetails,
    AffectedFrame,
    HeavyAdReason,
    DeprecationIssueDetails,
    CookieIssueDetails,
    CorsIssueDetails,
    HeavyAdResolutionStatus,
    SharedArrayBufferIssueType,
    InspectorIssue,
    CookieOperation,
    ContentSecurityPolicyIssueDetails,
    SourceCodeLocation,
    AttributionReportingIssueDetails,
    InspectorIssueDetails,
    GenericIssueDetails,
    IssueId,
    FederatedAuthUserInfoRequestIssueReason,
    MixedContentResourceType,
    AffectedCookie,
    HeavyAdIssueDetails,
    MixedContentResolutionStatus,
    StyleSheetLoadingIssueReason,
    BounceTrackingIssueDetails,
    InspectorIssueCode,
    FederatedAuthRequestIssueReason,
    GenericIssueErrorType,
    QuirksModeIssueDetails,
    FederatedAuthRequestIssueDetails
)
from cdp.domains.runtime.types import (
    ScriptId
)
from cdp.domains.dom.types import (
    BackendNodeId
)


@dataclass
class Audits(BaseDomain):
    def get_encoded_response(
        self,
        request_id: RequestId,
        encoding: str,
        quality: MaybeUndefined[],
        size_only: MaybeUndefined[]
    ):
        params = {
            "requestId": request_id,
            "encoding": encoding,
        }

        if is_defined(
            quality
        ):
            params[] = quality

        if is_defined(
            size_only
        ):
            params[] = size_only

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
        report_aaa: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            report_aaa
        ):
            params[] = report_aaa

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

