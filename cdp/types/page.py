# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.types import (
    debugger,
    dom,
    emulation,
    io,
    network,
    runtime
)
from typing import (
    Literal,
    TypedDict
)

FrameId = str

ScriptIdentifier = str

AdFrameType = Literal[
    'none',
    'child',
    'root'
]

AdFrameExplanation = Literal[
    'ParentIsAd',
    'CreatedByAdScript',
    'MatchedBlockingRule'
]

SecureContextType = Literal[
    'Secure',
    'SecureLocalhost',
    'InsecureScheme',
    'InsecureAncestor'
]

CrossOriginIsolatedContextType = Literal[
    'Isolated',
    'NotIsolated',
    'NotIsolatedFeatureDisabled'
]

GatedAPIFeatures = Literal[
    'SharedArrayBuffers',
    'SharedArrayBuffersTransferAllowed',
    'PerformanceMeasureMemory',
    'PerformanceProfile'
]

PermissionsPolicyFeature = Literal[
    'accelerometer',
    'ambient-light-sensor',
    'attribution-reporting',
    'autoplay',
    'bluetooth',
    'browsing-topics',
    'camera',
    'ch-dpr',
    'ch-device-memory',
    'ch-downlink',
    'ch-ect',
    'ch-prefers-color-scheme',
    'ch-prefers-reduced-motion',
    'ch-prefers-reduced-transparency',
    'ch-rtt',
    'ch-save-data',
    'ch-ua',
    'ch-ua-arch',
    'ch-ua-bitness',
    'ch-ua-platform',
    'ch-ua-model',
    'ch-ua-mobile',
    'ch-ua-form-factor',
    'ch-ua-full-version',
    'ch-ua-full-version-list',
    'ch-ua-platform-version',
    'ch-ua-wow64',
    'ch-viewport-height',
    'ch-viewport-width',
    'ch-width',
    'clipboard-read',
    'clipboard-write',
    'compute-pressure',
    'cross-origin-isolated',
    'direct-sockets',
    'display-capture',
    'document-domain',
    'encrypted-media',
    'execution-while-out-of-viewport',
    'execution-while-not-rendered',
    'focus-without-user-activation',
    'fullscreen',
    'frobulate',
    'gamepad',
    'geolocation',
    'gyroscope',
    'hid',
    'identity-credentials-get',
    'idle-detection',
    'interest-cohort',
    'join-ad-interest-group',
    'keyboard-map',
    'local-fonts',
    'magnetometer',
    'microphone',
    'midi',
    'otp-credentials',
    'payment',
    'picture-in-picture',
    'private-aggregation',
    'private-state-token-issuance',
    'private-state-token-redemption',
    'publickey-credentials-get',
    'run-ad-auction',
    'screen-wake-lock',
    'serial',
    'shared-autofill',
    'shared-storage',
    'shared-storage-select-url',
    'smart-card',
    'storage-access',
    'sync-xhr',
    'unload',
    'usb',
    'vertical-scroll',
    'web-share',
    'window-management',
    'window-placement',
    'xr-spatial-tracking'
]

PermissionsPolicyBlockReason = Literal[
    'Header',
    'IframeAttribute',
    'InFencedFrameTree',
    'InIsolatedApp'
]

OriginTrialTokenStatus = Literal[
    'Success',
    'NotSupported',
    'Insecure',
    'Expired',
    'WrongOrigin',
    'InvalidSignature',
    'Malformed',
    'WrongVersion',
    'FeatureDisabled',
    'TokenDisabled',
    'FeatureDisabledForUser',
    'UnknownTrial'
]

OriginTrialStatus = Literal[
    'Enabled',
    'ValidTokenNotProvided',
    'OSNotSupported',
    'TrialNotAllowed'
]

OriginTrialUsageRestriction = Literal[
    'None',
    'Subset'
]

TransitionType = Literal[
    'link',
    'typed',
    'address_bar',
    'auto_bookmark',
    'auto_subframe',
    'manual_subframe',
    'generated',
    'auto_toplevel',
    'form_submit',
    'reload',
    'keyword',
    'keyword_generated',
    'other'
]

DialogType = Literal[
    'alert',
    'confirm',
    'prompt',
    'beforeunload'
]

ClientNavigationReason = Literal[
    'formSubmissionGet',
    'formSubmissionPost',
    'httpHeaderRefresh',
    'scriptInitiated',
    'metaTagRefresh',
    'pageBlockInterstitial',
    'reload',
    'anchorClick'
]

ClientNavigationDisposition = Literal[
    'currentTab',
    'newTab',
    'newWindow',
    'download'
]

ReferrerPolicy = Literal[
    'noReferrer',
    'noReferrerWhenDowngrade',
    'origin',
    'originWhenCrossOrigin',
    'sameOrigin',
    'strictOrigin',
    'strictOriginWhenCrossOrigin',
    'unsafeUrl'
]

AutoResponseMode = Literal[
    'none',
    'autoAccept',
    'autoReject',
    'autoOptOut'
]

NavigationType = Literal[
    'Navigation',
    'BackForwardCacheRestore'
]

BackForwardCacheNotRestoredReason = Literal[
    'NotPrimaryMainFrame',
    'BackForwardCacheDisabled',
    'RelatedActiveContentsExist',
    'HTTPStatusNotOK',
    'SchemeNotHTTPOrHTTPS',
    'Loading',
    'WasGrantedMediaAccess',
    'DisableForRenderFrameHostCalled',
    'DomainNotAllowed',
    'HTTPMethodNotGET',
    'SubframeIsNavigating',
    'Timeout',
    'CacheLimit',
    'JavaScriptExecution',
    'RendererProcessKilled',
    'RendererProcessCrashed',
    'SchedulerTrackedFeatureUsed',
    'ConflictingBrowsingInstance',
    'CacheFlushed',
    'ServiceWorkerVersionActivation',
    'SessionRestored',
    'ServiceWorkerPostMessage',
    'EnteredBackForwardCacheBeforeServiceWorkerHostAdded',
    'RenderFrameHostReused_SameSite',
    'RenderFrameHostReused_CrossSite',
    'ServiceWorkerClaim',
    'IgnoreEventAndEvict',
    'HaveInnerContents',
    'TimeoutPuttingInCache',
    'BackForwardCacheDisabledByLowMemory',
    'BackForwardCacheDisabledByCommandLine',
    'NetworkRequestDatapipeDrainedAsBytesConsumer',
    'NetworkRequestRedirected',
    'NetworkRequestTimeout',
    'NetworkExceedsBufferLimit',
    'NavigationCancelledWhileRestoring',
    'NotMostRecentNavigationEntry',
    'BackForwardCacheDisabledForPrerender',
    'UserAgentOverrideDiffers',
    'ForegroundCacheLimit',
    'BrowsingInstanceNotSwapped',
    'BackForwardCacheDisabledForDelegate',
    'UnloadHandlerExistsInMainFrame',
    'UnloadHandlerExistsInSubFrame',
    'ServiceWorkerUnregistration',
    'CacheControlNoStore',
    'CacheControlNoStoreCookieModified',
    'CacheControlNoStoreHTTPOnlyCookieModified',
    'NoResponseHead',
    'Unknown',
    'ActivationNavigationsDisallowedForBug1234857',
    'ErrorDocument',
    'FencedFramesEmbedder',
    'CookieDisabled',
    'HTTPAuthRequired',
    'CookieFlushed',
    'WebSocket',
    'WebTransport',
    'WebRTC',
    'MainResourceHasCacheControlNoStore',
    'MainResourceHasCacheControlNoCache',
    'SubresourceHasCacheControlNoStore',
    'SubresourceHasCacheControlNoCache',
    'ContainsPlugins',
    'DocumentLoaded',
    'DedicatedWorkerOrWorklet',
    'OutstandingNetworkRequestOthers',
    'RequestedMIDIPermission',
    'RequestedAudioCapturePermission',
    'RequestedVideoCapturePermission',
    'RequestedBackForwardCacheBlockedSensors',
    'RequestedBackgroundWorkPermission',
    'BroadcastChannel',
    'WebXR',
    'SharedWorker',
    'WebLocks',
    'WebHID',
    'WebShare',
    'RequestedStorageAccessGrant',
    'WebNfc',
    'OutstandingNetworkRequestFetch',
    'OutstandingNetworkRequestXHR',
    'AppBanner',
    'Printing',
    'WebDatabase',
    'PictureInPicture',
    'Portal',
    'SpeechRecognizer',
    'IdleManager',
    'PaymentManager',
    'SpeechSynthesis',
    'KeyboardLock',
    'WebOTPService',
    'OutstandingNetworkRequestDirectSocket',
    'InjectedJavascript',
    'InjectedStyleSheet',
    'KeepaliveRequest',
    'IndexedDBEvent',
    'Dummy',
    'JsNetworkRequestReceivedCacheControlNoStoreResource',
    'WebRTCSticky',
    'WebTransportSticky',
    'WebSocketSticky',
    'ContentSecurityHandler',
    'ContentWebAuthenticationAPI',
    'ContentFileChooser',
    'ContentSerial',
    'ContentFileSystemAccess',
    'ContentMediaDevicesDispatcherHost',
    'ContentWebBluetooth',
    'ContentWebUSB',
    'ContentMediaSessionService',
    'ContentScreenReader',
    'EmbedderPopupBlockerTabHelper',
    'EmbedderSafeBrowsingTriggeredPopupBlocker',
    'EmbedderSafeBrowsingThreatDetails',
    'EmbedderAppBannerManager',
    'EmbedderDomDistillerViewerSource',
    'EmbedderDomDistillerSelfDeletingRequestDelegate',
    'EmbedderOomInterventionTabHelper',
    'EmbedderOfflinePage',
    'EmbedderChromePasswordManagerClientBindCredentialManager',
    'EmbedderPermissionRequestManager',
    'EmbedderModalDialog',
    'EmbedderExtensions',
    'EmbedderExtensionMessaging',
    'EmbedderExtensionMessagingForOpenPort',
    'EmbedderExtensionSentMessageToCachedFrame'
]

BackForwardCacheNotRestoredReasonType = Literal[
    'SupportPending',
    'PageSupportNeeded',
    'Circumstantial'
]


class AdFrameStatus(TypedDict):
    ad_frame_type: 'AdFrameType'
    explanations: list


class AdScriptId(TypedDict):
    script_id: 'runtime.ScriptId'
    debugger_id: 'runtime.UniqueDebuggerId'


class PermissionsPolicyBlockLocator(TypedDict):
    frame_id: 'FrameId'
    block_reason: 'PermissionsPolicyBlockReason'


class PermissionsPolicyFeatureState(TypedDict):
    feature: 'PermissionsPolicyFeature'
    allowed: bool
    locator: 'PermissionsPolicyBlockLocator'


class OriginTrialToken(TypedDict):
    origin: str
    match_sub_domains: bool
    trial_name: str
    expiry_time: 'network.TimeSinceEpoch'
    is_third_party: bool
    usage_restriction: 'OriginTrialUsageRestriction'


class OriginTrialTokenWithStatus(TypedDict):
    raw_token_text: str
    status: 'OriginTrialTokenStatus'
    parsed_token: 'OriginTrialToken'


class OriginTrial(TypedDict):
    trial_name: str
    status: 'OriginTrialStatus'
    tokens_with_status: list


class Frame(TypedDict):
    id: 'FrameId'
    loader_id: 'network.LoaderId'
    url: str
    domain_and_registry: str
    security_origin: str
    mime_type: str
    secure_context_type: 'SecureContextType'
    cross_origin_isolated_context_type: 'CrossOriginIsolatedContextType'
    gated_api_features: list
    parent_id: 'FrameId'
    name: str
    url_fragment: str
    unreachable_url: str
    ad_frame_status: 'AdFrameStatus'


class FrameResource(TypedDict):
    url: str
    type: 'network.ResourceType'
    mime_type: str
    last_modified: 'network.TimeSinceEpoch'
    content_size: float
    failed: bool
    canceled: bool


class FrameResourceTree(TypedDict):
    frame: 'Frame'
    resources: list
    child_frames: list


class FrameTree(TypedDict):
    frame: 'Frame'
    child_frames: list


class NavigationEntry(TypedDict):
    id: int
    url: str
    user_typed_url: str
    title: str
    transition_type: 'TransitionType'


class ScreencastFrameMetadata(TypedDict):
    offset_top: float
    page_scale_factor: float
    device_width: float
    device_height: float
    scroll_offset_x: float
    scroll_offset_y: float
    timestamp: 'network.TimeSinceEpoch'


class AppManifestError(TypedDict):
    message: str
    critical: int
    line: int
    column: int


class AppManifestParsedProperties(TypedDict):
    scope: str


class LayoutViewport(TypedDict):
    page_x: int
    page_y: int
    client_width: int
    client_height: int


class VisualViewport(TypedDict):
    offset_x: float
    offset_y: float
    page_x: float
    page_y: float
    client_width: float
    client_height: float
    scale: float
    zoom: float


class Viewport(TypedDict):
    x: float
    y: float
    width: float
    height: float
    scale: float


class FontFamilies(TypedDict):
    standard: str
    fixed: str
    serif: str
    sans_serif: str
    cursive: str
    fantasy: str
    math: str


class ScriptFontFamilies(TypedDict):
    script: str
    font_families: 'FontFamilies'


class FontSizes(TypedDict):
    standard: int
    fixed: int


class InstallabilityErrorArgument(TypedDict):
    name: str
    value: str


class InstallabilityError(TypedDict):
    error_id: str
    error_arguments: list


class CompilationCacheParams(TypedDict):
    url: str
    eager: bool


class BackForwardCacheNotRestoredExplanation(TypedDict):
    type: 'BackForwardCacheNotRestoredReasonType'
    reason: 'BackForwardCacheNotRestoredReason'
    context: str


class BackForwardCacheNotRestoredExplanationTree(TypedDict):
    url: str
    explanations: list
    children: list