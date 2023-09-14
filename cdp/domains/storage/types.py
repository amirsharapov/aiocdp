from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

AttributionReportingSourceRegistrationResult = Literal[
    "success",
    "internalError",
    "insufficientSourceCapacity",
    "insufficientUniqueDestinationCapacity",
    "excessiveReportingOrigins",
    "prohibitedByBrowserPolicy",
    "successNoised",
    "destinationReportingLimitReached",
    "destinationGlobalLimitReached",
    "destinationBothLimitsReached",
    "reportingOriginsPerSiteLimitReached",
    "exceedsMaxChannelCapacity"
]

AttributionReportingSourceType = Literal[
    "navigation",
    "event"
]

InterestGroupAccessType = Literal[
    "join",
    "leave",
    "update",
    "loaded",
    "bid",
    "win"
]

SharedStorageAccessType = Literal[
    "documentAddModule",
    "documentSelectURL",
    "documentRun",
    "documentSet",
    "documentAppend",
    "documentDelete",
    "documentClear",
    "workletSet",
    "workletAppend",
    "workletDelete",
    "workletClear",
    "workletGet",
    "workletKeys",
    "workletEntries",
    "workletLength",
    "workletRemainingBudget"
]

StorageBucketsDurability = Literal[
    "relaxed",
    "strict"
]

StorageType = Literal[
    "appcache",
    "cookies",
    "file_systems",
    "indexeddb",
    "local_storage",
    "shader_cache",
    "websql",
    "service_workers",
    "cache_storage",
    "interest_groups",
    "shared_storage",
    "storage_buckets",
    "all",
    "other"
]


@dataclass
class AttributionReportingAggregationKeysEntry:
    key: str
    value: UnsignedInt128AsBase16


@dataclass
class AttributionReportingEventReportWindows:
    start: int
    ends: list


@dataclass
class AttributionReportingFilterDataEntry:
    key: str
    values: list


@dataclass
class AttributionReportingSourceRegistration:
    time: TimeSinceEpoch
    expiry: int
    eventReportWindow: int
    eventReportWindows: AttributionReportingEventReportWindows
    aggregatableReportWindow: int
    type: AttributionReportingSourceType
    sourceOrigin: str
    reportingOrigin: str
    destinationSites: list
    eventId: UnsignedInt64AsBase10
    priority: SignedInt64AsBase10
    filterData: list
    aggregationKeys: list
    debugKey: UnsignedInt64AsBase10


@dataclass
class InterestGroupAd:
    renderUrl: str
    metadata: str


@dataclass
class InterestGroupDetails:
    ownerOrigin: str
    name: str
    expirationTime: TimeSinceEpoch
    joiningOrigin: str
    biddingUrl: str
    biddingWasmHelperUrl: str
    updateUrl: str
    trustedBiddingSignalsUrl: str
    trustedBiddingSignalsKeys: list
    userBiddingSignals: str
    ads: list
    adComponents: list


@dataclass
class SharedStorageAccessParams:
    scriptSourceUrl: str
    operationName: str
    serializedData: str
    urlsWithMetadata: list
    key: str
    value: str
    ignoreIfPresent: bool


@dataclass
class SharedStorageEntry:
    key: str
    value: str


@dataclass
class SharedStorageMetadata:
    creationTime: TimeSinceEpoch
    length: int
    remainingBudget: float


@dataclass
class SharedStorageReportingMetadata:
    eventType: str
    reportingUrl: str


@dataclass
class SharedStorageUrlWithMetadata:
    url: str
    reportingMetadata: list


@dataclass
class StorageBucket:
    storageKey: SerializedStorageKey
    name: str


@dataclass
class StorageBucketInfo:
    bucket: StorageBucket
    id: str
    expiration: TimeSinceEpoch
    quota: float
    persistent: bool
    durability: StorageBucketsDurability


@dataclass
class TrustTokens:
    issuerOrigin: str
    count: float


@dataclass
class UsageForType:
    storageType: StorageType
    usage: float
