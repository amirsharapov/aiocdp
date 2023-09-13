from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.runtime.types import (
    RemoteObject,
    ScriptId,
    RemoteObjectId
)
from cdp.domains.dom.types import (
    BackendNodeId,
    NodeId
)
from cdp.domains.dom_debugger.types import (
    DOMBreakpointType
)


@dataclass
class DOMDebugger(BaseDomain):
    def get_event_listeners(
        self,
        object_id: RemoteObjectId,
        depth: MaybeUndefined[int],
        pierce: MaybeUndefined[bool]
    ):
        params = {
            "objectId": object_id,
        }

        if is_defined(
            depth
        ):
            params["depth"] = depth

        if is_defined(
            pierce
        ):
            params["pierce"] = pierce

        return self._send_command(
            "DOMDebugger.getEventListeners",
            params
        )

    def remove_dom_breakpoint(
        self,
        node_id: NodeId,
        type_: DOMBreakpointType
    ):
        params = {
            "nodeId": node_id,
            "type": type_,
        }

        return self._send_command(
            "DOMDebugger.removeDOMBreakpoint",
            params
        )

    def remove_event_listener_breakpoint(
        self,
        event_name: str,
        target_name: MaybeUndefined[str]
    ):
        params = {
            "eventName": event_name,
        }

        if is_defined(
            target_name
        ):
            params["targetName"] = target_name

        return self._send_command(
            "DOMDebugger.removeEventListenerBreakpoint",
            params
        )

    def remove_instrumentation_breakpoint(
        self,
        event_name: str
    ):
        params = {
            "eventName": event_name,
        }

        return self._send_command(
            "DOMDebugger.removeInstrumentationBreakpoint",
            params
        )

    def remove_xhr_breakpoint(
        self,
        url: str
    ):
        params = {
            "url": url,
        }

        return self._send_command(
            "DOMDebugger.removeXHRBreakpoint",
            params
        )

    def set_break_on_csp_violation(
        self,
        violation_types: list
    ):
        params = {
            "violationTypes": violation_types,
        }

        return self._send_command(
            "DOMDebugger.setBreakOnCSPViolation",
            params
        )

    def set_dom_breakpoint(
        self,
        node_id: NodeId,
        type_: DOMBreakpointType
    ):
        params = {
            "nodeId": node_id,
            "type": type_,
        }

        return self._send_command(
            "DOMDebugger.setDOMBreakpoint",
            params
        )

    def set_event_listener_breakpoint(
        self,
        event_name: str,
        target_name: MaybeUndefined[str]
    ):
        params = {
            "eventName": event_name,
        }

        if is_defined(
            target_name
        ):
            params["targetName"] = target_name

        return self._send_command(
            "DOMDebugger.setEventListenerBreakpoint",
            params
        )

    def set_instrumentation_breakpoint(
        self,
        event_name: str
    ):
        params = {
            "eventName": event_name,
        }

        return self._send_command(
            "DOMDebugger.setInstrumentationBreakpoint",
            params
        )

    def set_xhr_breakpoint(
        self,
        url: str
    ):
        params = {
            "url": url,
        }

        return self._send_command(
            "DOMDebugger.setXHRBreakpoint",
            params
        )

