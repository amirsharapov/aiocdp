from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

CertificateErrorAction = Literal[
    "continue",
    "cancel"
]

MixedContentType = Literal[
    "blockable",
    "optionally-blockable",
    "none"
]

SafetyTipStatus = Literal[
    "badReputation",
    "lookalike"
]

SecurityState = Literal[
    "unknown",
    "neutral",
    "insecure",
    "secure",
    "info",
    "insecure-broken"
]


@dataclass
class CertificateSecurityState:
    protocol: str
    keyExchange: str
    keyExchangeGroup: str
    cipher: str
    mac: str
    certificate: list
    subjectName: str
    issuer: str
    validFrom: TimeSinceEpoch
    validTo: TimeSinceEpoch
    certificateNetworkError: str
    certificateHasWeakSignature: bool
    certificateHasSha1Signature: bool
    modernSSL: bool
    obsoleteSslProtocol: bool
    obsoleteSslKeyExchange: bool
    obsoleteSslCipher: bool
    obsoleteSslSignature: bool


@dataclass
class InsecureContentStatus:
    ranMixedContent: bool
    displayedMixedContent: bool
    containedMixedForm: bool
    ranContentWithCertErrors: bool
    displayedContentWithCertErrors: bool
    ranInsecureContentStyle: SecurityState
    displayedInsecureContentStyle: SecurityState


@dataclass
class SafetyTipInfo:
    safetyTipStatus: SafetyTipStatus
    safeUrl: str


@dataclass
class SecurityStateExplanation:
    securityState: SecurityState
    title: str
    summary: str
    description: str
    mixedContentType: MixedContentType
    certificate: list
    recommendations: list


@dataclass
class VisibleSecurityState:
    securityState: SecurityState
    certificateSecurityState: CertificateSecurityState
    safetyTipInfo: SafetyTipInfo
    securityStateIssueIds: list
