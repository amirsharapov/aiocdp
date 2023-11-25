from .core.implementations import (
    Chrome,
    Target,
    Session,
    Connection,
    EventStream,
    EventStreamReader,
    TargetInfo
)
from .ioc import (
    set_chrome_class,
    set_target_class,
    set_target_info_class,
    set_session_class,
    set_connection_class,
    set_event_stream_class,
    set_event_stream_reader_class
)


def setup_default_factories():
    set_chrome_class(Chrome)
    set_target_class(Target)
    set_target_info_class(TargetInfo)
    set_session_class(Session)
    set_connection_class(Connection)
    set_event_stream_class(EventStream)
    set_event_stream_reader_class(EventStreamReader)
