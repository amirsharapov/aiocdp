from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.accessibility.types import (
    AXValue,
    AXNodeId,
    AXValueNativeSourceType,
    AXValueType,
    AXValueSourceType,
    AXNode,
    AXPropertyName
)
from cdp.domains.dom.types import (
    NodeId,
    BackendNodeId
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.runtime.types import (
    RemoteObjectId
)


@dataclass
class Accessibility(BaseDomain):
    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Accessibility.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Accessibility.enable",
            params
        )

    def get_partial_ax_tree(
        self,
        node_id: MaybeUndefined[NodeId],
        backend_node_id: MaybeUndefined[BackendNodeId],
        object_id: MaybeUndefined[RemoteObjectId],
        fetch_relatives: MaybeUndefined[bool]
    ):
        params = {}

        if is_defined(
            node_id
        ):
            params["nodeId"] = node_id

        if is_defined(
            backend_node_id
        ):
            params["backendNodeId"] = backend_node_id

        if is_defined(
            object_id
        ):
            params["objectId"] = object_id

        if is_defined(
            fetch_relatives
        ):
            params["fetchRelatives"] = fetch_relatives

        return self._send_command(
            "Accessibility.getPartialAXTree",
            params
        )

    def get_full_ax_tree(
        self,
        depth: MaybeUndefined[int],
        frame_id: MaybeUndefined[FrameId]
    ):
        params = {}

        if is_defined(
            depth
        ):
            params["depth"] = depth

        if is_defined(
            frame_id
        ):
            params["frameId"] = frame_id

        return self._send_command(
            "Accessibility.getFullAXTree",
            params
        )

    def get_root_ax_node(
        self,
        frame_id: MaybeUndefined[FrameId]
    ):
        params = {}

        if is_defined(
            frame_id
        ):
            params["frameId"] = frame_id

        return self._send_command(
            "Accessibility.getRootAXNode",
            params
        )

    def get_ax_node_and_ancestors(
        self,
        node_id: MaybeUndefined[NodeId],
        backend_node_id: MaybeUndefined[BackendNodeId],
        object_id: MaybeUndefined[RemoteObjectId]
    ):
        params = {}

        if is_defined(
            node_id
        ):
            params["nodeId"] = node_id

        if is_defined(
            backend_node_id
        ):
            params["backendNodeId"] = backend_node_id

        if is_defined(
            object_id
        ):
            params["objectId"] = object_id

        return self._send_command(
            "Accessibility.getAXNodeAndAncestors",
            params
        )

    def get_child_ax_nodes(
        self,
        id_: AXNodeId,
        frame_id: MaybeUndefined[FrameId]
    ):
        params = {
            "id": id_,
        }

        if is_defined(
            frame_id
        ):
            params["frameId"] = frame_id

        return self._send_command(
            "Accessibility.getChildAXNodes",
            params
        )

    def query_ax_tree(
        self,
        node_id: MaybeUndefined[NodeId],
        backend_node_id: MaybeUndefined[BackendNodeId],
        object_id: MaybeUndefined[RemoteObjectId],
        accessible_name: MaybeUndefined[str],
        role: MaybeUndefined[str]
    ):
        params = {}

        if is_defined(
            node_id
        ):
            params["nodeId"] = node_id

        if is_defined(
            backend_node_id
        ):
            params["backendNodeId"] = backend_node_id

        if is_defined(
            object_id
        ):
            params["objectId"] = object_id

        if is_defined(
            accessible_name
        ):
            params["accessibleName"] = accessible_name

        if is_defined(
            role
        ):
            params["role"] = role

        return self._send_command(
            "Accessibility.queryAXTree",
            params
        )

