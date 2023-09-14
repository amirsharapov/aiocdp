from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

PrefetchStatus = Literal[
    "PrefetchAllowed",
    "PrefetchFailedIneligibleRedirect",
    "PrefetchFailedInvalidRedirect",
    "PrefetchFailedMIMENotSupported",
    "PrefetchFailedNetError",
    "PrefetchFailedNon2XX",
    "PrefetchFailedPerPageLimitExceeded",
    "PrefetchEvicted",
    "PrefetchHeldback",
    "PrefetchIneligibleRetryAfter",
    "PrefetchIsPrivacyDecoy",
    "PrefetchIsStale",
    "PrefetchNotEligibleBrowserContextOffTheRecord",
    "PrefetchNotEligibleDataSaverEnabled",
    "PrefetchNotEligibleExistingProxy",
    "PrefetchNotEligibleHostIsNonUnique",
    "PrefetchNotEligibleNonDefaultStoragePartition",
    "PrefetchNotEligibleSameSiteCrossOriginPrefetchRequiredProxy",
    "PrefetchNotEligibleSchemeIsNotHttps",
    "PrefetchNotEligibleUserHasCookies",
    "PrefetchNotEligibleUserHasServiceWorker",
    "PrefetchNotEligibleBatterySaverEnabled",
    "PrefetchNotEligiblePreloadingDisabled",
    "PrefetchNotFinishedInTime",
    "PrefetchNotStarted",
    "PrefetchNotUsedCookiesChanged",
    "PrefetchProxyNotAvailable",
    "PrefetchResponseUsed",
    "PrefetchSuccessfulButNotUsed",
    "PrefetchNotUsedProbeFailed"
]

PreloadingStatus = Literal[
    "Pending",
    "Running",
    "Ready",
    "Success",
    "Failure",
    "NotSupported"
]

PrerenderFinalStatus = Literal[
    "Activated",
    "Destroyed",
    "LowEndDevice",
    "InvalidSchemeRedirect",
    "InvalidSchemeNavigation",
    "InProgressNavigation",
    "NavigationRequestBlockedByCsp",
    "MainFrameNavigation",
    "MojoBinderPolicy",
    "RendererProcessCrashed",
    "RendererProcessKilled",
    "Download",
    "TriggerDestroyed",
    "NavigationNotCommitted",
    "NavigationBadHttpStatus",
    "ClientCertRequested",
    "NavigationRequestNetworkError",
    "MaxNumOfRunningPrerendersExceeded",
    "CancelAllHostsForTesting",
    "DidFailLoad",
    "Stop",
    "SslCertificateError",
    "LoginAuthRequested",
    "UaChangeRequiresReload",
    "BlockedByClient",
    "AudioOutputDeviceRequested",
    "MixedContent",
    "TriggerBackgrounded",
    "MemoryLimitExceeded",
    "DataSaverEnabled",
    "HasEffectiveUrl",
    "ActivatedBeforeStarted",
    "InactivePageRestriction",
    "StartFailed",
    "TimeoutBackgrounded",
    "CrossSiteRedirectInInitialNavigation",
    "CrossSiteNavigationInInitialNavigation",
    "SameSiteCrossOriginRedirectNotOptInInInitialNavigation",
    "SameSiteCrossOriginNavigationNotOptInInInitialNavigation",
    "ActivationNavigationParameterMismatch",
    "ActivatedInBackground",
    "EmbedderHostDisallowed",
    "ActivationNavigationDestroyedBeforeSuccess",
    "TabClosedByUserGesture",
    "TabClosedWithoutUserGesture",
    "PrimaryMainFrameRendererProcessCrashed",
    "PrimaryMainFrameRendererProcessKilled",
    "ActivationFramePolicyNotCompatible",
    "PreloadingDisabled",
    "BatterySaverEnabled",
    "ActivatedDuringMainFrameNavigation",
    "PreloadingUnsupportedByWebContents",
    "CrossSiteRedirectInMainFrameNavigation",
    "CrossSiteNavigationInMainFrameNavigation",
    "SameSiteCrossOriginRedirectNotOptInInMainFrameNavigation",
    "SameSiteCrossOriginNavigationNotOptInInMainFrameNavigation",
    "MemoryPressureOnTrigger",
    "MemoryPressureAfterTriggered",
    "PrerenderingDisabledByDevTools",
    "ResourceLoadBlockedByClient",
    "SpeculationRuleRemoved",
    "ActivatedWithAuxiliaryBrowsingContexts"
]

RuleSetErrorType = Literal[
    "SourceIsNotJsonObject",
    "InvalidRulesSkipped"
]

SpeculationAction = Literal[
    "Prefetch",
    "Prerender"
]

SpeculationTargetHint = Literal[
    "Blank",
    "Self"
]


@dataclass
class PreloadingAttemptKey:
    loaderId: LoaderId
    action: SpeculationAction
    url: str
    targetHint: SpeculationTargetHint


@dataclass
class PreloadingAttemptSource:
    key: PreloadingAttemptKey
    ruleSetIds: list
    nodeIds: list


@dataclass
class RuleSet:
    id: RuleSetId
    loaderId: LoaderId
    sourceText: str
    backendNodeId: BackendNodeId
    url: str
    requestId: RequestId
    errorType: RuleSetErrorType
    errorMessage: str
