from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

AuthenticatorId = str

AuthenticatorProtocol = Literal[
    "u2f",
    "ctap2"
]

Ctap2Version = Literal[
    "ctap2_0",
    "ctap2_1"
]

AuthenticatorTransport = Literal[
    "usb",
    "nfc",
    "ble",
    "cable",
    "internal"
]


@dataclass
class VirtualAuthenticatorOptions:
    protocol: "AuthenticatorProtocol"
    ctap2_version: "Ctap2Version"
    transport: "AuthenticatorTransport"
    has_resident_key: bool
    has_user_verification: bool
    has_large_blob: bool
    has_cred_blob: bool
    has_min_pin_length: bool
    has_prf: bool
    automatic_presence_simulation: bool
    is_user_verified: bool


@dataclass
class Credential:
    credential_id: str
    is_resident_credential: bool
    rp_id: str
    private_key: str
    user_handle: str
    sign_count: int
    large_blob: str
