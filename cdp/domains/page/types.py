from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

AdFrameExplanation = Literal[
    "ParentIsAd",
    "CreatedByAdScript",
    "MatchedBlockingRule"
]

AdFrameType = Literal[
    "none",
    "child",
    "root"
]

AutoResponseMode = Literal[
    "none",
    "autoAccept",
    "autoReject",
    "autoOptOut"
]

BackForwardCacheNotRestoredReason = Literal[
    "NotPrimaryMainFrame",
    "BackForwardCacheDisabled",
    "RelatedActiveContentsExist",
    "HTTPStatusNotOK",
    "SchemeNotHTTPOrHTTPS",
    "Loading",
    "WasGrantedMediaAccess",
    "DisableForRenderFrameHostCalled",
    "DomainNotAllowed",
    "HTTPMethodNotGET",
    "SubframeIsNavigating",
    "Timeout",
    "CacheLimit",
    "JavaScriptExecution",
    "RendererProcessKilled",
    "RendererProcessCrashed",
    "SchedulerTrackedFeatureUsed",
    "ConflictingBrowsingInstance",
    "CacheFlushed",
    "ServiceWorkerVersionActivation",
    "SessionRestored",
    "ServiceWorkerPostMessage",
    "EnteredBackForwardCacheBeforeServiceWorkerHostAdded",
    "RenderFrameHostReused_SameSite",
    "RenderFrameHostReused_CrossSite",
    "ServiceWorkerClaim",
    "IgnoreEventAndEvict",
    "HaveInnerContents",
    "TimeoutPuttingInCache",
    "BackForwardCacheDisabledByLowMemory",
    "BackForwardCacheDisabledByCommandLine",
    "NetworkRequestDatapipeDrainedAsBytesConsumer",
    "NetworkRequestRedirected",
    "NetworkRequestTimeout",
    "NetworkExceedsBufferLimit",
    "NavigationCancelledWhileRestoring",
    "NotMostRecentNavigationEntry",
    "BackForwardCacheDisabledForPrerender",
    "UserAgentOverrideDiffers",
    "ForegroundCacheLimit",
    "BrowsingInstanceNotSwapped",
    "BackForwardCacheDisabledForDelegate",
    "UnloadHandlerExistsInMainFrame",
    "UnloadHandlerExistsInSubFrame",
    "ServiceWorkerUnregistration",
    "CacheControlNoStore",
    "CacheControlNoStoreCookieModified",
    "CacheControlNoStoreHTTPOnlyCookieModified",
    "NoResponseHead",
    "Unknown",
    "ActivationNavigationsDisallowedForBug1234857",
    "ErrorDocument",
    "FencedFramesEmbedder",
    "CookieDisabled",
    "HTTPAuthRequired",
    "CookieFlushed",
    "WebSocket",
    "WebTransport",
    "WebRTC",
    "MainResourceHasCacheControlNoStore",
    "MainResourceHasCacheControlNoCache",
    "SubresourceHasCacheControlNoStore",
    "SubresourceHasCacheControlNoCache",
    "ContainsPlugins",
    "DocumentLoaded",
    "DedicatedWorkerOrWorklet",
    "OutstandingNetworkRequestOthers",
    "RequestedMIDIPermission",
    "RequestedAudioCapturePermission",
    "RequestedVideoCapturePermission",
    "RequestedBackForwardCacheBlockedSensors",
    "RequestedBackgroundWorkPermission",
    "BroadcastChannel",
    "WebXR",
    "SharedWorker",
    "WebLocks",
    "WebHID",
    "WebShare",
    "RequestedStorageAccessGrant",
    "WebNfc",
    "OutstandingNetworkRequestFetch",
    "OutstandingNetworkRequestXHR",
    "AppBanner",
    "Printing",
    "WebDatabase",
    "PictureInPicture",
    "Portal",
    "SpeechRecognizer",
    "IdleManager",
    "PaymentManager",
    "SpeechSynthesis",
    "KeyboardLock",
    "WebOTPService",
    "OutstandingNetworkRequestDirectSocket",
    "InjectedJavascript",
    "InjectedStyleSheet",
    "KeepaliveRequest",
    "IndexedDBEvent",
    "Dummy",
    "JsNetworkRequestReceivedCacheControlNoStoreResource",
    "WebRTCSticky",
    "WebTransportSticky",
    "WebSocketSticky",
    "ContentSecurityHandler",
    "ContentWebAuthenticationAPI",
    "ContentFileChooser",
    "ContentSerial",
    "ContentFileSystemAccess",
    "ContentMediaDevicesDispatcherHost",
    "ContentWebBluetooth",
    "ContentWebUSB",
    "ContentMediaSessionService",
    "ContentScreenReader",
    "EmbedderPopupBlockerTabHelper",
    "EmbedderSafeBrowsingTriggeredPopupBlocker",
    "EmbedderSafeBrowsingThreatDetails",
    "EmbedderAppBannerManager",
    "EmbedderDomDistillerViewerSource",
    "EmbedderDomDistillerSelfDeletingRequestDelegate",
    "EmbedderOomInterventionTabHelper",
    "EmbedderOfflinePage",
    "EmbedderChromePasswordManagerClientBindCredentialManager",
    "EmbedderPermissionRequestManager",
    "EmbedderModalDialog",
    "EmbedderExtensions",
    "EmbedderExtensionMessaging",
    "EmbedderExtensionMessagingForOpenPort",
    "EmbedderExtensionSentMessageToCachedFrame"
]

BackForwardCacheNotRestoredReasonType = Literal[
    "SupportPending",
    "PageSupportNeeded",
    "Circumstantial"
]

ClientNavigationDisposition = Literal[
    "currentTab",
    "newTab",
    "newWindow",
    "download"
]

ClientNavigationReason = Literal[
    "formSubmissionGet",
    "formSubmissionPost",
    "httpHeaderRefresh",
    "scriptInitiated",
    "metaTagRefresh",
    "pageBlockInterstitial",
    "reload",
    "anchorClick"
]

CrossOriginIsolatedContextType = Literal[
    "Isolated",
    "NotIsolated",
    "NotIsolatedFeatureDisabled"
]

DialogType = Literal[
    "alert",
    "confirm",
    "prompt",
    "beforeunload"
]

GatedAPIFeatures = Literal[
    "SharedArrayBuffers",
    "SharedArrayBuffersTransferAllowed",
    "PerformanceMeasureMemory",
    "PerformanceProfile"
]

NavigationType = Literal[
    "Navigation",
    "BackForwardCacheRestore"
]

OriginTrialStatus = Literal[
    "Enabled",
    "ValidTokenNotProvided",
    "OSNotSupported",
    "TrialNotAllowed"
]

OriginTrialTokenStatus = Literal[
    "Success",
    "NotSupported",
    "Insecure",
    "Expired",
    "WrongOrigin",
    "InvalidSignature",
    "Malformed",
    "WrongVersion",
    "FeatureDisabled",
    "TokenDisabled",
    "FeatureDisabledForUser",
    "UnknownTrial"
]

OriginTrialUsageRestriction = Literal[
    "None",
    "Subset"
]

PermissionsPolicyBlockReason = Literal[
    "Header",
    "IframeAttribute",
    "InFencedFrameTree",
    "InIsolatedApp"
]

PermissionsPolicyFeature = Literal[
    "accelerometer",
    "ambient-light-sensor",
    "attribution-reporting",
    "autoplay",
    "bluetooth",
    "browsing-topics",
    "camera",
    "ch-dpr",
    "ch-device-memory",
    "ch-downlink",
    "ch-ect",
    "ch-prefers-color-scheme",
    "ch-prefers-reduced-motion",
    "ch-prefers-reduced-transparency",
    "ch-rtt",
    "ch-save-data",
    "ch-ua",
    "ch-ua-arch",
    "ch-ua-bitness",
    "ch-ua-platform",
    "ch-ua-model",
    "ch-ua-mobile",
    "ch-ua-form-factor",
    "ch-ua-full-version",
    "ch-ua-full-version-list",
    "ch-ua-platform-version",
    "ch-ua-wow64",
    "ch-viewport-height",
    "ch-viewport-width",
    "ch-width",
    "clipboard-read",
    "clipboard-write",
    "compute-pressure",
    "cross-origin-isolated",
    "direct-sockets",
    "display-capture",
    "document-domain",
    "encrypted-media",
    "execution-while-out-of-viewport",
    "execution-while-not-rendered",
    "focus-without-user-activation",
    "fullscreen",
    "frobulate",
    "gamepad",
    "geolocation",
    "gyroscope",
    "hid",
    "identity-credentials-get",
    "idle-detection",
    "interest-cohort",
    "join-ad-interest-group",
    "keyboard-map",
    "local-fonts",
    "magnetometer",
    "microphone",
    "midi",
    "otp-credentials",
    "payment",
    "picture-in-picture",
    "private-aggregation",
    "private-state-token-issuance",
    "private-state-token-redemption",
    "publickey-credentials-get",
    "run-ad-auction",
    "screen-wake-lock",
    "serial",
    "shared-autofill",
    "shared-storage",
    "shared-storage-select-url",
    "smart-card",
    "storage-access",
    "sync-xhr",
    "unload",
    "usb",
    "vertical-scroll",
    "web-share",
    "window-management",
    "window-placement",
    "xr-spatial-tracking"
]

ReferrerPolicy = Literal[
    "noReferrer",
    "noReferrerWhenDowngrade",
    "origin",
    "originWhenCrossOrigin",
    "sameOrigin",
    "strictOrigin",
    "strictOriginWhenCrossOrigin",
    "unsafeUrl"
]

SecureContextType = Literal[
    "Secure",
    "SecureLocalhost",
    "InsecureScheme",
    "InsecureAncestor"
]

TransitionType = Literal[
    "link",
    "typed",
    "address_bar",
    "auto_bookmark",
    "auto_subframe",
    "manual_subframe",
    "generated",
    "auto_toplevel",
    "form_submit",
    "reload",
    "keyword",
    "keyword_generated",
    "other"
]


@dataclass
class AdFrameStatus:
    adFrameType: AdFrameType
    explanations: list


@dataclass
class AdScriptId:
    scriptId: ScriptId
    debuggerId: UniqueDebuggerId


@dataclass
class AppManifestError:
    message: str
    critical: int
    line: int
    column: int


@dataclass
class AppManifestParsedProperties:
    scope: str


@dataclass
class BackForwardCacheNotRestoredExplanation:
    type: BackForwardCacheNotRestoredReasonType
    reason: BackForwardCacheNotRestoredReason
    context: str


@dataclass
class BackForwardCacheNotRestoredExplanationTree:
    url: str
    explanations: list
    children: list


@dataclass
class CompilationCacheParams:
    url: str
    eager: bool


@dataclass
class FontFamilies:
    standard: str
    fixed: str
    serif: str
    sansSerif: str
    cursive: str
    fantasy: str
    math: str


@dataclass
class FontSizes:
    standard: int
    fixed: int


@dataclass
class Frame:
    id: FrameId
    parentId: FrameId
    loaderId: LoaderId
    name: str
    url: str
    urlFragment: str
    domainAndRegistry: str
    securityOrigin: str
    mimeType: str
    unreachableUrl: str
    adFrameStatus: AdFrameStatus
    secureContextType: SecureContextType
    crossOriginIsolatedContextType: CrossOriginIsolatedContextType
    gatedAPIFeatures: list


@dataclass
class FrameResource:
    url: str
    type: ResourceType
    mimeType: str
    lastModified: TimeSinceEpoch
    contentSize: float
    failed: bool
    canceled: bool


@dataclass
class FrameResourceTree:
    frame: Frame
    childFrames: list
    resources: list


@dataclass
class FrameTree:
    frame: Frame
    childFrames: list


@dataclass
class InstallabilityError:
    errorId: str
    errorArguments: list


@dataclass
class InstallabilityErrorArgument:
    name: str
    value: str


@dataclass
class LayoutViewport:
    pageX: int
    pageY: int
    clientWidth: int
    clientHeight: int


@dataclass
class NavigationEntry:
    id: int
    url: str
    userTypedURL: str
    title: str
    transitionType: TransitionType


@dataclass
class OriginTrial:
    trialName: str
    status: OriginTrialStatus
    tokensWithStatus: list


@dataclass
class OriginTrialToken:
    origin: str
    matchSubDomains: bool
    trialName: str
    expiryTime: TimeSinceEpoch
    isThirdParty: bool
    usageRestriction: OriginTrialUsageRestriction


@dataclass
class OriginTrialTokenWithStatus:
    rawTokenText: str
    parsedToken: OriginTrialToken
    status: OriginTrialTokenStatus


@dataclass
class PermissionsPolicyBlockLocator:
    frameId: FrameId
    blockReason: PermissionsPolicyBlockReason


@dataclass
class PermissionsPolicyFeatureState:
    feature: PermissionsPolicyFeature
    allowed: bool
    locator: PermissionsPolicyBlockLocator


@dataclass
class ScreencastFrameMetadata:
    offsetTop: float
    pageScaleFactor: float
    deviceWidth: float
    deviceHeight: float
    scrollOffsetX: float
    scrollOffsetY: float
    timestamp: TimeSinceEpoch


@dataclass
class ScriptFontFamilies:
    script: str
    fontFamilies: FontFamilies


@dataclass
class Viewport:
    x: float
    y: float
    width: float
    height: float
    scale: float


@dataclass
class VisualViewport:
    offsetX: float
    offsetY: float
    pageX: float
    pageY: float
    clientWidth: float
    clientHeight: float
    scale: float
    zoom: float
