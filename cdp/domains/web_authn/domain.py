from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.web_authn.types import (
    VirtualAuthenticatorOptions,
    Credential,
    AuthenticatorId,
    AuthenticatorTransport,
    AuthenticatorProtocol,
    Ctap2Version
)


@dataclass
class WebAuthn(BaseDomain):
    def enable(
        self,
        enable_ui: MaybeUndefined[bool]
    ):
        params = {}

        if is_defined(
            enable_ui
        ):
            params["enableUI"] = enable_ui

        return self._send_command(
            "WebAuthn.enable",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "WebAuthn.disable",
            params
        )

    def add_virtual_authenticator(
        self,
        options: VirtualAuthenticatorOptions
    ):
        params = {
            "options": options,
        }

        return self._send_command(
            "WebAuthn.addVirtualAuthenticator",
            params
        )

    def set_response_override_bits(
        self,
        authenticator_id: AuthenticatorId,
        is_bogus_signature: MaybeUndefined[bool],
        is_bad_uv: MaybeUndefined[bool],
        is_bad_up: MaybeUndefined[bool]
    ):
        params = {
            "authenticatorId": authenticator_id,
        }

        if is_defined(
            is_bogus_signature
        ):
            params["isBogusSignature"] = is_bogus_signature

        if is_defined(
            is_bad_uv
        ):
            params["isBadUV"] = is_bad_uv

        if is_defined(
            is_bad_up
        ):
            params["isBadUP"] = is_bad_up

        return self._send_command(
            "WebAuthn.setResponseOverrideBits",
            params
        )

    def remove_virtual_authenticator(
        self,
        authenticator_id: AuthenticatorId
    ):
        params = {
            "authenticatorId": authenticator_id,
        }

        return self._send_command(
            "WebAuthn.removeVirtualAuthenticator",
            params
        )

    def add_credential(
        self,
        authenticator_id: AuthenticatorId,
        credential: Credential
    ):
        params = {
            "authenticatorId": authenticator_id,
            "credential": credential,
        }

        return self._send_command(
            "WebAuthn.addCredential",
            params
        )

    def get_credential(
        self,
        authenticator_id: AuthenticatorId,
        credential_id: str
    ):
        params = {
            "authenticatorId": authenticator_id,
            "credentialId": credential_id,
        }

        return self._send_command(
            "WebAuthn.getCredential",
            params
        )

    def get_credentials(
        self,
        authenticator_id: AuthenticatorId
    ):
        params = {
            "authenticatorId": authenticator_id,
        }

        return self._send_command(
            "WebAuthn.getCredentials",
            params
        )

    def remove_credential(
        self,
        authenticator_id: AuthenticatorId,
        credential_id: str
    ):
        params = {
            "authenticatorId": authenticator_id,
            "credentialId": credential_id,
        }

        return self._send_command(
            "WebAuthn.removeCredential",
            params
        )

    def clear_credentials(
        self,
        authenticator_id: AuthenticatorId
    ):
        params = {
            "authenticatorId": authenticator_id,
        }

        return self._send_command(
            "WebAuthn.clearCredentials",
            params
        )

    def set_user_verified(
        self,
        authenticator_id: AuthenticatorId,
        is_user_verified: bool
    ):
        params = {
            "authenticatorId": authenticator_id,
            "isUserVerified": is_user_verified,
        }

        return self._send_command(
            "WebAuthn.setUserVerified",
            params
        )

    def set_automatic_presence_simulation(
        self,
        authenticator_id: AuthenticatorId,
        enabled: bool
    ):
        params = {
            "authenticatorId": authenticator_id,
            "enabled": enabled,
        }

        return self._send_command(
            "WebAuthn.setAutomaticPresenceSimulation",
            params
        )

