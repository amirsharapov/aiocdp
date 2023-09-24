# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from typing import (
    Literal,
    NotRequired,
    TypedDict
)


class Sink(TypedDict):
    name: str
    id: str
    session: NotRequired[str]


class EnableParamsT(TypedDict):
    presentation_url: NotRequired[str]


class SetSinkToUseParamsT(TypedDict):
    sink_name: str


class StartDesktopMirroringParamsT(TypedDict):
    sink_name: str


class StartTabMirroringParamsT(TypedDict):
    sink_name: str


class StopCastingParamsT(TypedDict):
    sink_name: str


class SinksUpdatedEventT(TypedDict):
    name: Literal['sinks_updated']
    params: 'SinksUpdatedParamsT'


class IssueUpdatedEventT(TypedDict):
    name: Literal['issue_updated']
    params: 'IssueUpdatedParamsT'


class SinksUpdatedParamsT(TypedDict):
    sinks: list


class IssueUpdatedParamsT(TypedDict):
    issue_message: str