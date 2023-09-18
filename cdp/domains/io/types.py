# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from typing import (
    Any,
    Literal,
    TYPE_CHECKING
)
from dataclasses import (
    dataclass
)

StreamHandle = str

@dataclass
class ReadReturnType:
    base64_encoded: bool
    data: str
    eof: bool


@dataclass
class ResolveBlobReturnType:
    uuid: str
