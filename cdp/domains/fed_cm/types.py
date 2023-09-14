from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

DialogType = Literal[
    "AccountChooser",
    "AutoReauthn",
    "ConfirmIdpSignin"
]

LoginState = Literal[
    "SignIn",
    "SignUp"
]


@dataclass
class Account:
    accountId: str
    email: str
    name: str
    givenName: str
    pictureUrl: str
    idpConfigUrl: str
    idpSigninUrl: str
    loginState: LoginState
    termsOfServiceUrl: str
    privacyPolicyUrl: str
