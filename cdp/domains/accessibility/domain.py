from dataclasses import (
    dataclass
)
from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.accessibility.types import (
    AXPropertyName,
    AXValueType,
    AXValue,
    AXValueSourceType,
    AXValueNativeSourceType,
    AXNode,
    AXNodeId
)
from cdp.domains.dom.types import (
    BackendNodeId,
    NodeId
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
        node_id: MaybeUndefined[],
        backend_node_id: MaybeUndefined[],
        object_id: MaybeUndefined[],
        fetch_relatives: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            node_id
        ):
            params[] = node_id

        if is_defined(
            backend_node_id
        ):
            params[] = backend_node_id

        if is_defined(
            object_id
        ):
            params[] = object_id

        if is_defined(
            fetch_relatives
        ):
            params[] = fetch_relatives

        return self._send_command(
            "Accessibility.getPartialAXTree",
            params
        )

    def get_full_ax_tree(
        self,
        depth: MaybeUndefined[],
        frame_id: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            depth
        ):
            params[] = depth

        if is_defined(
            frame_id
        ):
            params[] = frame_id

        return self._send_command(
            "Accessibility.getFullAXTree",
            params
        )

    def get_root_ax_node(
        self,
        frame_id: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            frame_id
        ):
            params[] = frame_id

        return self._send_command(
            "Accessibility.getRootAXNode",
            params
        )

    def get_ax_node_and_ancestors(
        self,
        node_id: MaybeUndefined[],
        backend_node_id: MaybeUndefined[],
        object_id: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            node_id
        ):
            params[] = node_id

        if is_defined(
            backend_node_id
        ):
            params[] = backend_node_id

        if is_defined(
            object_id
        ):
            params[] = object_id

        return self._send_command(
            "Accessibility.getAXNodeAndAncestors",
            params
        )

    def get_child_ax_nodes(
        self,
        id_: AXNodeId,
        frame_id: MaybeUndefined[]
    ):
        params = {
            "id": id_,
        }

        if is_defined(
            frame_id
        ):
            params[] = frame_id

        return self._send_command(
            "Accessibility.getChildAXNodes",
            params
        )

    def query_ax_tree(
        self,
        node_id: MaybeUndefined[],
        backend_node_id: MaybeUndefined[],
        object_id: MaybeUndefined[],
        accessible_name: MaybeUndefined[],
        role: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            node_id
        ):
            params[] = node_id

        if is_defined(
            backend_node_id
        ):
            params[] = backend_node_id

        if is_defined(
            object_id
        ):
            params[] = object_id

        if is_defined(
            accessible_name
        ):
            params[] = accessible_name

        if is_defined(
            role
        ):
            params[] = role

        return self._send_command(
            "Accessibility.queryAXTree",
            params
        )

