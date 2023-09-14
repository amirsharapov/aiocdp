from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

FillingStrategy = Literal[
    "autocompleteAttribute",
    "autofillInferred"
]


@dataclass
class Address:
    fields: list


@dataclass
class AddressField:
    name: str
    value: str


@dataclass
class AddressFields:
    fields: list


@dataclass
class AddressUI:
    addressFields: list


@dataclass
class CreditCard:
    number: str
    name: str
    expiryMonth: str
    expiryYear: str
    cvc: str


@dataclass
class FilledField:
    htmlType: str
    id: str
    name: str
    value: str
    autofillType: str
    fillingStrategy: FillingStrategy
