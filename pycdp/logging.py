from typing import Literal

LoggableEvents = Literal[
    'connection.handle_message',
    'connection.handle_event',
    'connection.handle_response',
    'connection.send'
]

events_to_log: dict[LoggableEvents, bool] = {}


def enable_logging(
    events: list[LoggableEvents] = None
):
    events = events or []

    for event in events:
        events_to_log[event] = True


def disable_logging(
    events: list[LoggableEvents] = None
):
    events = events or []

    for event in events:
        events_to_log[event] = False


def is_logging_enabled(
        event: LoggableEvents
):
    return events_to_log.get(
        event,
        False
    )
