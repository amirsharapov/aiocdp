from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

AuthenticatorProtocol = Literal[
    "u2f",
    "ctap2"
]

AuthenticatorTransport = Literal[
    "usb",
    "nfc",
    "ble",
    "cable",
    "internal"
]

Ctap2Version = Literal[
    "ctap2_0",
    "ctap2_1"
]


@dataclass
class Credential:
    credentialId: str
    isResidentCredential: bool
    rpId: str
    privateKey: str
    userHandle: str
    signCount: int
    largeBlob: str


@dataclass
class VirtualAuthenticatorOptions:
    protocol: AuthenticatorProtocol
    ctap2Version: Ctap2Version
    transport: AuthenticatorTransport
    hasResidentKey: bool
    hasUserVerification: bool
    hasLargeBlob: bool
    hasCredBlob: bool
    hasMinPinLength: bool
    hasPrf: bool
    automaticPresenceSimulation: bool
    isUserVerified: bool
