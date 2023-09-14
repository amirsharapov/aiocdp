from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.network.types import (
    TimeSinceEpoch
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.browser.types import (
    BrowserContextID
)

SerializedStorageKey = str

UnsignedInt64AsBase10 = str

UnsignedInt128AsBase16 = str

SignedInt64AsBase10 = str

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

AttributionReportingSourceType = Literal[
    "navigation",
    "event"
]

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


@dataclass
class UsageForType:
    storage_type: "StorageType"
    usage: float


@dataclass
class TrustTokens:
    issuer_origin: str
    count: float


@dataclass
class InterestGroupAd:
    render_url: str
    metadata: str


@dataclass
class InterestGroupDetails:
    owner_origin: str
    name: str
    expiration_time: "TimeSinceEpoch"
    joining_origin: str
    bidding_url: str
    bidding_wasm_helper_url: str
    update_url: str
    trusted_bidding_signals_url: str
    trusted_bidding_signals_keys: list
    user_bidding_signals: str
    ads: list
    ad_components: list


@dataclass
class SharedStorageEntry:
    key: str
    value: str


@dataclass
class SharedStorageMetadata:
    creation_time: "TimeSinceEpoch"
    length: int
    remaining_budget: float


@dataclass
class SharedStorageReportingMetadata:
    event_type: str
    reporting_url: str


@dataclass
class SharedStorageUrlWithMetadata:
    url: str
    reporting_metadata: list


@dataclass
class SharedStorageAccessParams:
    script_source_url: str
    operation_name: str
    serialized_data: str
    urls_with_metadata: list
    key: str
    value: str
    ignore_if_present: bool


@dataclass
class StorageBucket:
    storage_key: "SerializedStorageKey"
    name: str


@dataclass
class StorageBucketInfo:
    bucket: "StorageBucket"
    id: str
    expiration: "TimeSinceEpoch"
    quota: float
    persistent: bool
    durability: "StorageBucketsDurability"


@dataclass
class AttributionReportingFilterDataEntry:
    key: str
    values: list


@dataclass
class AttributionReportingAggregationKeysEntry:
    key: str
    value: "UnsignedInt128AsBase16"


@dataclass
class AttributionReportingEventReportWindows:
    start: int
    ends: list


@dataclass
class AttributionReportingSourceRegistration:
    time: "TimeSinceEpoch"
    expiry: int
    event_report_window: int
    event_report_windows: "AttributionReportingEventReportWindows"
    aggregatable_report_window: int
    type: "AttributionReportingSourceType"
    source_origin: str
    reporting_origin: str
    destination_sites: list
    event_id: "UnsignedInt64AsBase10"
    priority: "SignedInt64AsBase10"
    filter_data: list
    aggregation_keys: list
    debug_key: "UnsignedInt64AsBase10"


@dataclass
class GetStorageKeyForFrameReturnT:
    storage_key: "SerializedStorageKey"


@dataclass
class GetCookiesReturnT:
    cookies: list


@dataclass
class GetUsageAndQuotaReturnT:
    usage: float
    quota: float
    override_active: bool
    usage_breakdown: list


@dataclass
class GetTrustTokensReturnT:
    tokens: list


@dataclass
class ClearTrustTokensReturnT:
    did_delete_tokens: bool


@dataclass
class GetInterestGroupDetailsReturnT:
    details: "InterestGroupDetails"


@dataclass
class GetSharedStorageMetadataReturnT:
    metadata: "SharedStorageMetadata"


@dataclass
class GetSharedStorageEntriesReturnT:
    entries: list


@dataclass
class RunBounceTrackingMitigationsReturnT:
    deleted_sites: list
