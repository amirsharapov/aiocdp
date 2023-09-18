# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.domains.base import (
    BaseDomain
)
from cdp.domains import (
    mappers
)
from cdp.utils import (
    UNDEFINED,
    is_defined
)
from dataclasses import (
    dataclass
)
from typing import (
    TYPE_CHECKING
)
from cdp.domains.network.types import (
    AuthChallengeResponse,
    CanClearBrowserCacheReturnType,
    CanClearBrowserCookiesReturnType,
    CanEmulateNetworkConditionsReturnType,
    ConnectionType,
    CookiePriority,
    CookieSameSite,
    CookieSourceScheme,
    ErrorReason,
    FrameId,
    GetAllCookiesReturnType,
    GetCertificateReturnType,
    GetCookiesReturnType,
    GetRequestPostDataReturnType,
    GetResponseBodyForInterceptionReturnType,
    GetResponseBodyReturnType,
    GetSecurityIsolationStatusReturnType,
    Headers,
    InterceptionId,
    LoadNetworkResourceOptions,
    LoadNetworkResourceReturnType,
    RequestId,
    SearchInResponseBodyReturnType,
    SetCookieReturnType,
    TakeResponseBodyForInterceptionAsStreamReturnType,
    TimeSinceEpoch,
    UserAgentMetadata
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IFutureResponse
    )


@dataclass
class Network(BaseDomain):
    def set_accepted_encodings(
            self,
            encodings: 'list'
    ) -> 'IFutureResponse[None]':
        params = {
            'encodings': encodings,
        }

        return self._send_command(
            'Network.setAcceptedEncodings',
            params,
            False
        )

    def clear_accepted_encodings_override(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Network.clearAcceptedEncodingsOverride',
            params,
            False
        )

    def can_clear_browser_cache(
            self
    ) -> 'IFutureResponse[CanClearBrowserCacheReturnType]':
        params = {}

        return self._send_command(
            'Network.canClearBrowserCache',
            params,
            True,
            lambda data: from_dict(
                CanClearBrowserCacheReturnType,
                data,
                'camel'
            )
        )

    def can_clear_browser_cookies(
            self
    ) -> 'IFutureResponse[CanClearBrowserCookiesReturnType]':
        params = {}

        return self._send_command(
            'Network.canClearBrowserCookies',
            params,
            True,
            lambda data: from_dict(
                CanClearBrowserCookiesReturnType,
                data,
                'camel'
            )
        )

    def can_emulate_network_conditions(
            self
    ) -> 'IFutureResponse[CanEmulateNetworkConditionsReturnType]':
        params = {}

        return self._send_command(
            'Network.canEmulateNetworkConditions',
            params,
            True,
            lambda data: from_dict(
                CanEmulateNetworkConditionsReturnType,
                data,
                'camel'
            )
        )

    def clear_browser_cache(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Network.clearBrowserCache',
            params,
            False
        )

    def clear_browser_cookies(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Network.clearBrowserCookies',
            params,
            False
        )

    def continue_intercepted_request(
            self,
            interception_id: 'InterceptionId',
            error_reason: 'ErrorReason' = UNDEFINED,
            raw_response: 'str' = UNDEFINED,
            url: 'str' = UNDEFINED,
            method: 'str' = UNDEFINED,
            post_data: 'str' = UNDEFINED,
            headers: 'Headers' = UNDEFINED,
            auth_challenge_response: 'AuthChallengeResponse' = UNDEFINED
    ) -> 'IFutureResponse[None]':
        params = {
            'interceptionId': to_dict(
                interception_id,
                'camel'
            ),
        }

        if is_defined(error_reason):
            params['errorReason'] = to_dict(
                error_reason,
                'camel'
            )

        if is_defined(raw_response):
            params['rawResponse'] = raw_response

        if is_defined(url):
            params['url'] = url

        if is_defined(method):
            params['method'] = method

        if is_defined(post_data):
            params['postData'] = post_data

        if is_defined(headers):
            params['headers'] = to_dict(
                headers,
                'camel'
            )

        if is_defined(auth_challenge_response):
            params['authChallengeResponse'] = to_dict(
                auth_challenge_response,
                'camel'
            )

        return self._send_command(
            'Network.continueInterceptedRequest',
            params,
            False
        )

    def delete_cookies(
            self,
            name: 'str',
            url: 'str' = UNDEFINED,
            domain: 'str' = UNDEFINED,
            path: 'str' = UNDEFINED
    ) -> 'IFutureResponse[None]':
        params = {
            'name': name,
        }

        if is_defined(url):
            params['url'] = url

        if is_defined(domain):
            params['domain'] = domain

        if is_defined(path):
            params['path'] = path

        return self._send_command(
            'Network.deleteCookies',
            params,
            False
        )

    def disable(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Network.disable',
            params,
            False
        )

    def emulate_network_conditions(
            self,
            offline: 'bool',
            latency: 'float',
            download_throughput: 'float',
            upload_throughput: 'float',
            connection_type: 'ConnectionType' = UNDEFINED
    ) -> 'IFutureResponse[None]':
        params = {
            'offline': offline,
            'latency': latency,
            'downloadThroughput': download_throughput,
            'uploadThroughput': upload_throughput,
        }

        if is_defined(connection_type):
            params['connectionType'] = to_dict(
                connection_type,
                'camel'
            )

        return self._send_command(
            'Network.emulateNetworkConditions',
            params,
            False
        )

    def enable(
            self,
            max_total_buffer_size: 'int' = UNDEFINED,
            max_resource_buffer_size: 'int' = UNDEFINED,
            max_post_data_size: 'int' = UNDEFINED
    ) -> 'IFutureResponse[None]':
        params = {}

        if is_defined(max_total_buffer_size):
            params['maxTotalBufferSize'] = max_total_buffer_size

        if is_defined(max_resource_buffer_size):
            params['maxResourceBufferSize'] = max_resource_buffer_size

        if is_defined(max_post_data_size):
            params['maxPostDataSize'] = max_post_data_size

        return self._send_command(
            'Network.enable',
            params,
            False
        )

    def get_all_cookies(
            self
    ) -> 'IFutureResponse[GetAllCookiesReturnType]':
        params = {}

        return self._send_command(
            'Network.getAllCookies',
            params,
            True,
            lambda data: from_dict(
                GetAllCookiesReturnType,
                data,
                'camel'
            )
        )

    def get_certificate(
            self,
            origin: 'str'
    ) -> 'IFutureResponse[GetCertificateReturnType]':
        params = {
            'origin': origin,
        }

        return self._send_command(
            'Network.getCertificate',
            params,
            True,
            lambda data: from_dict(
                GetCertificateReturnType,
                data,
                'camel'
            )
        )

    def get_cookies(
            self,
            urls: 'list' = UNDEFINED
    ) -> 'IFutureResponse[GetCookiesReturnType]':
        params = {}

        if is_defined(urls):
            params['urls'] = urls

        return self._send_command(
            'Network.getCookies',
            params,
            True,
            lambda data: from_dict(
                GetCookiesReturnType,
                data,
                'camel'
            )
        )

    def get_response_body(
            self,
            request_id: 'RequestId'
    ) -> 'IFutureResponse[GetResponseBodyReturnType]':
        params = {
            'requestId': to_dict(
                request_id,
                'camel'
            ),
        }

        return self._send_command(
            'Network.getResponseBody',
            params,
            True,
            lambda data: from_dict(
                GetResponseBodyReturnType,
                data,
                'camel'
            )
        )

    def get_request_post_data(
            self,
            request_id: 'RequestId'
    ) -> 'IFutureResponse[GetRequestPostDataReturnType]':
        params = {
            'requestId': to_dict(
                request_id,
                'camel'
            ),
        }

        return self._send_command(
            'Network.getRequestPostData',
            params,
            True,
            lambda data: from_dict(
                GetRequestPostDataReturnType,
                data,
                'camel'
            )
        )

    def get_response_body_for_interception(
            self,
            interception_id: 'InterceptionId'
    ) -> 'IFutureResponse[GetResponseBodyForInterceptionReturnType]':
        params = {
            'interceptionId': to_dict(
                interception_id,
                'camel'
            ),
        }

        return self._send_command(
            'Network.getResponseBodyForInterception',
            params,
            True,
            lambda data: from_dict(
                GetResponseBodyForInterceptionReturnType,
                data,
                'camel'
            )
        )

    def take_response_body_for_interception_as_stream(
            self,
            interception_id: 'InterceptionId'
    ) -> 'IFutureResponse[TakeResponseBodyForInterceptionAsStreamReturnType]':
        params = {
            'interceptionId': to_dict(
                interception_id,
                'camel'
            ),
        }

        return self._send_command(
            'Network.takeResponseBodyForInterceptionAsStream',
            params,
            True,
            lambda data: from_dict(
                TakeResponseBodyForInterceptionAsStreamReturnType,
                data,
                'camel'
            )
        )

    def replay_xhr(
            self,
            request_id: 'RequestId'
    ) -> 'IFutureResponse[None]':
        params = {
            'requestId': to_dict(
                request_id,
                'camel'
            ),
        }

        return self._send_command(
            'Network.replayXHR',
            params,
            False
        )

    def search_in_response_body(
            self,
            request_id: 'RequestId',
            query: 'str',
            case_sensitive: 'bool' = UNDEFINED,
            is_regex: 'bool' = UNDEFINED
    ) -> 'IFutureResponse[SearchInResponseBodyReturnType]':
        params = {
            'requestId': to_dict(
                request_id,
                'camel'
            ),
            'query': query,
        }

        if is_defined(case_sensitive):
            params['caseSensitive'] = case_sensitive

        if is_defined(is_regex):
            params['isRegex'] = is_regex

        return self._send_command(
            'Network.searchInResponseBody',
            params,
            True,
            lambda data: from_dict(
                SearchInResponseBodyReturnType,
                data,
                'camel'
            )
        )

    def set_blocked_ur_ls(
            self,
            urls: 'list'
    ) -> 'IFutureResponse[None]':
        params = {
            'urls': urls,
        }

        return self._send_command(
            'Network.setBlockedURLs',
            params,
            False
        )

    def set_bypass_service_worker(
            self,
            bypass: 'bool'
    ) -> 'IFutureResponse[None]':
        params = {
            'bypass': bypass,
        }

        return self._send_command(
            'Network.setBypassServiceWorker',
            params,
            False
        )

    def set_cache_disabled(
            self,
            cache_disabled: 'bool'
    ) -> 'IFutureResponse[None]':
        params = {
            'cacheDisabled': cache_disabled,
        }

        return self._send_command(
            'Network.setCacheDisabled',
            params,
            False
        )

    def set_cookie(
            self,
            name: 'str',
            value: 'str',
            url: 'str' = UNDEFINED,
            domain: 'str' = UNDEFINED,
            path: 'str' = UNDEFINED,
            secure: 'bool' = UNDEFINED,
            http_only: 'bool' = UNDEFINED,
            same_site: 'CookieSameSite' = UNDEFINED,
            expires: 'TimeSinceEpoch' = UNDEFINED,
            priority: 'CookiePriority' = UNDEFINED,
            same_party: 'bool' = UNDEFINED,
            source_scheme: 'CookieSourceScheme' = UNDEFINED,
            source_port: 'int' = UNDEFINED,
            partition_key: 'str' = UNDEFINED
    ) -> 'IFutureResponse[SetCookieReturnType]':
        params = {
            'name': name,
            'value': value,
        }

        if is_defined(url):
            params['url'] = url

        if is_defined(domain):
            params['domain'] = domain

        if is_defined(path):
            params['path'] = path

        if is_defined(secure):
            params['secure'] = secure

        if is_defined(http_only):
            params['httpOnly'] = http_only

        if is_defined(same_site):
            params['sameSite'] = to_dict(
                same_site,
                'camel'
            )

        if is_defined(expires):
            params['expires'] = to_dict(
                expires,
                'camel'
            )

        if is_defined(priority):
            params['priority'] = to_dict(
                priority,
                'camel'
            )

        if is_defined(same_party):
            params['sameParty'] = same_party

        if is_defined(source_scheme):
            params['sourceScheme'] = to_dict(
                source_scheme,
                'camel'
            )

        if is_defined(source_port):
            params['sourcePort'] = source_port

        if is_defined(partition_key):
            params['partitionKey'] = partition_key

        return self._send_command(
            'Network.setCookie',
            params,
            True,
            lambda data: from_dict(
                SetCookieReturnType,
                data,
                'camel'
            )
        )

    def set_cookies(
            self,
            cookies: 'list'
    ) -> 'IFutureResponse[None]':
        params = {
            'cookies': cookies,
        }

        return self._send_command(
            'Network.setCookies',
            params,
            False
        )

    def set_extra_http_headers(
            self,
            headers: 'Headers'
    ) -> 'IFutureResponse[None]':
        params = {
            'headers': to_dict(
                headers,
                'camel'
            ),
        }

        return self._send_command(
            'Network.setExtraHTTPHeaders',
            params,
            False
        )

    def set_attach_debug_stack(
            self,
            enabled: 'bool'
    ) -> 'IFutureResponse[None]':
        params = {
            'enabled': enabled,
        }

        return self._send_command(
            'Network.setAttachDebugStack',
            params,
            False
        )

    def set_request_interception(
            self,
            patterns: 'list'
    ) -> 'IFutureResponse[None]':
        params = {
            'patterns': patterns,
        }

        return self._send_command(
            'Network.setRequestInterception',
            params,
            False
        )

    def set_user_agent_override(
            self,
            user_agent: 'str',
            accept_language: 'str' = UNDEFINED,
            platform: 'str' = UNDEFINED,
            user_agent_metadata: 'UserAgentMetadata' = UNDEFINED
    ) -> 'IFutureResponse[None]':
        params = {
            'userAgent': user_agent,
        }

        if is_defined(accept_language):
            params['acceptLanguage'] = accept_language

        if is_defined(platform):
            params['platform'] = platform

        if is_defined(user_agent_metadata):
            params['userAgentMetadata'] = to_dict(
                user_agent_metadata,
                'camel'
            )

        return self._send_command(
            'Network.setUserAgentOverride',
            params,
            False
        )

    def get_security_isolation_status(
            self,
            frame_id: 'FrameId' = UNDEFINED
    ) -> 'IFutureResponse[GetSecurityIsolationStatusReturnType]':
        params = {}

        if is_defined(frame_id):
            params['frameId'] = to_dict(
                frame_id,
                'camel'
            )

        return self._send_command(
            'Network.getSecurityIsolationStatus',
            params,
            True,
            lambda data: from_dict(
                GetSecurityIsolationStatusReturnType,
                data,
                'camel'
            )
        )

    def enable_reporting_api(
            self,
            enable: 'bool'
    ) -> 'IFutureResponse[None]':
        params = {
            'enable': enable,
        }

        return self._send_command(
            'Network.enableReportingApi',
            params,
            False
        )

    def load_network_resource(
            self,
            url: 'str',
            options: 'LoadNetworkResourceOptions',
            frame_id: 'FrameId' = UNDEFINED
    ) -> 'IFutureResponse[LoadNetworkResourceReturnType]':
        params = {
            'url': url,
            'options': to_dict(
                options,
                'camel'
            ),
        }

        if is_defined(frame_id):
            params['frameId'] = to_dict(
                frame_id,
                'camel'
            )

        return self._send_command(
            'Network.loadNetworkResource',
            params,
            True,
            lambda data: from_dict(
                LoadNetworkResourceReturnType,
                data,
                'camel'
            )
        )
