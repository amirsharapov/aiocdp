from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.dom.types import (
    NodeId,
    BackendNode,
    ShadowRootType,
    PhysicalAxes,
    Quad,
    BackendNodeId,
    ShapeOutsideInfo,
    LogicalAxes,
    CompatibilityMode,
    BoxModel,
    Node,
    Rect,
    PseudoType
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.runtime.types import (
    ExecutionContextId,
    StackTrace,
    RemoteObject,
    RemoteObjectId
)


@dataclass
class DOM(BaseDomain):
    def collect_class_names_from_subtree(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "DOM.collectClassNamesFromSubtree",
            params
        )

    def copy_to(
        self,
        node_id: NodeId,
        target_node_id: NodeId,
        insert_before_node_id: MaybeUndefined[NodeId]
    ):
        params = {
            "nodeId": node_id,
            "targetNodeId": target_node_id,
        }

        if is_defined(
            insert_before_node_id
        ):
            params["insertBeforeNodeId"] = insert_before_node_id

        return self._send_command(
            "DOM.copyTo",
            params
        )

    def describe_node(
        self,
        node_id: MaybeUndefined[NodeId],
        backend_node_id: MaybeUndefined[BackendNodeId],
        object_id: MaybeUndefined[RemoteObjectId],
        depth: MaybeUndefined[int],
        pierce: MaybeUndefined[bool]
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
            depth
        ):
            params["depth"] = depth

        if is_defined(
            pierce
        ):
            params["pierce"] = pierce

        return self._send_command(
            "DOM.describeNode",
            params
        )

    def scroll_into_view_if_needed(
        self,
        node_id: MaybeUndefined[NodeId],
        backend_node_id: MaybeUndefined[BackendNodeId],
        object_id: MaybeUndefined[RemoteObjectId],
        rect: MaybeUndefined[Rect]
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
            rect
        ):
            params["rect"] = rect

        return self._send_command(
            "DOM.scrollIntoViewIfNeeded",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "DOM.disable",
            params
        )

    def discard_search_results(
        self,
        search_id: str
    ):
        params = {
            "searchId": search_id,
        }

        return self._send_command(
            "DOM.discardSearchResults",
            params
        )

    def enable(
        self,
        include_whitespace: MaybeUndefined[str]
    ):
        params = {}

        if is_defined(
            include_whitespace
        ):
            params["includeWhitespace"] = include_whitespace

        return self._send_command(
            "DOM.enable",
            params
        )

    def focus(
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
            "DOM.focus",
            params
        )

    def get_attributes(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "DOM.getAttributes",
            params
        )

    def get_box_model(
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
            "DOM.getBoxModel",
            params
        )

    def get_content_quads(
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
            "DOM.getContentQuads",
            params
        )

    def get_document(
        self,
        depth: MaybeUndefined[int],
        pierce: MaybeUndefined[bool]
    ):
        params = {}

        if is_defined(
            depth
        ):
            params["depth"] = depth

        if is_defined(
            pierce
        ):
            params["pierce"] = pierce

        return self._send_command(
            "DOM.getDocument",
            params
        )

    def get_flattened_document(
        self,
        depth: MaybeUndefined[int],
        pierce: MaybeUndefined[bool]
    ):
        params = {}

        if is_defined(
            depth
        ):
            params["depth"] = depth

        if is_defined(
            pierce
        ):
            params["pierce"] = pierce

        return self._send_command(
            "DOM.getFlattenedDocument",
            params
        )

    def get_nodes_for_subtree_by_style(
        self,
        node_id: NodeId,
        computed_styles: list,
        pierce: MaybeUndefined[bool]
    ):
        params = {
            "nodeId": node_id,
            "computedStyles": computed_styles,
        }

        if is_defined(
            pierce
        ):
            params["pierce"] = pierce

        return self._send_command(
            "DOM.getNodesForSubtreeByStyle",
            params
        )

    def get_node_for_location(
        self,
        x: int,
        y: int,
        include_user_agent_shadow_dom: MaybeUndefined[bool],
        ignore_pointer_events_none: MaybeUndefined[bool]
    ):
        params = {
            "x": x,
            "y": y,
        }

        if is_defined(
            include_user_agent_shadow_dom
        ):
            params["includeUserAgentShadowDOM"] = include_user_agent_shadow_dom

        if is_defined(
            ignore_pointer_events_none
        ):
            params["ignorePointerEventsNone"] = ignore_pointer_events_none

        return self._send_command(
            "DOM.getNodeForLocation",
            params
        )

    def get_outer_html(
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
            "DOM.getOuterHTML",
            params
        )

    def get_relayout_boundary(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "DOM.getRelayoutBoundary",
            params
        )

    def get_search_results(
        self,
        search_id: str,
        from_index: int,
        to_index: int
    ):
        params = {
            "searchId": search_id,
            "fromIndex": from_index,
            "toIndex": to_index,
        }

        return self._send_command(
            "DOM.getSearchResults",
            params
        )

    def hide_highlight(
        self
    ):
        params = {}

        return self._send_command(
            "DOM.hideHighlight",
            params
        )

    def highlight_node(
        self
    ):
        params = {}

        return self._send_command(
            "DOM.highlightNode",
            params
        )

    def highlight_rect(
        self
    ):
        params = {}

        return self._send_command(
            "DOM.highlightRect",
            params
        )

    def mark_undoable_state(
        self
    ):
        params = {}

        return self._send_command(
            "DOM.markUndoableState",
            params
        )

    def move_to(
        self,
        node_id: NodeId,
        target_node_id: NodeId,
        insert_before_node_id: MaybeUndefined[NodeId]
    ):
        params = {
            "nodeId": node_id,
            "targetNodeId": target_node_id,
        }

        if is_defined(
            insert_before_node_id
        ):
            params["insertBeforeNodeId"] = insert_before_node_id

        return self._send_command(
            "DOM.moveTo",
            params
        )

    def perform_search(
        self,
        query: str,
        include_user_agent_shadow_dom: MaybeUndefined[bool]
    ):
        params = {
            "query": query,
        }

        if is_defined(
            include_user_agent_shadow_dom
        ):
            params["includeUserAgentShadowDOM"] = include_user_agent_shadow_dom

        return self._send_command(
            "DOM.performSearch",
            params
        )

    def push_node_by_path_to_frontend(
        self,
        path: str
    ):
        params = {
            "path": path,
        }

        return self._send_command(
            "DOM.pushNodeByPathToFrontend",
            params
        )

    def push_nodes_by_backend_ids_to_frontend(
        self,
        backend_node_ids: list
    ):
        params = {
            "backendNodeIds": backend_node_ids,
        }

        return self._send_command(
            "DOM.pushNodesByBackendIdsToFrontend",
            params
        )

    def query_selector(
        self,
        node_id: NodeId,
        selector: str
    ):
        params = {
            "nodeId": node_id,
            "selector": selector,
        }

        return self._send_command(
            "DOM.querySelector",
            params
        )

    def query_selector_all(
        self,
        node_id: NodeId,
        selector: str
    ):
        params = {
            "nodeId": node_id,
            "selector": selector,
        }

        return self._send_command(
            "DOM.querySelectorAll",
            params
        )

    def get_top_layer_elements(
        self
    ):
        params = {}

        return self._send_command(
            "DOM.getTopLayerElements",
            params
        )

    def redo(
        self
    ):
        params = {}

        return self._send_command(
            "DOM.redo",
            params
        )

    def remove_attribute(
        self,
        node_id: NodeId,
        name: str
    ):
        params = {
            "nodeId": node_id,
            "name": name,
        }

        return self._send_command(
            "DOM.removeAttribute",
            params
        )

    def remove_node(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "DOM.removeNode",
            params
        )

    def request_child_nodes(
        self,
        node_id: NodeId,
        depth: MaybeUndefined[int],
        pierce: MaybeUndefined[bool]
    ):
        params = {
            "nodeId": node_id,
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
            "DOM.requestChildNodes",
            params
        )

    def request_node(
        self,
        object_id: RemoteObjectId
    ):
        params = {
            "objectId": object_id,
        }

        return self._send_command(
            "DOM.requestNode",
            params
        )

    def resolve_node(
        self,
        node_id: MaybeUndefined[NodeId],
        backend_node_id: MaybeUndefined[BackendNodeId],
        object_group: MaybeUndefined[str],
        execution_context_id: MaybeUndefined[ExecutionContextId]
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
            object_group
        ):
            params["objectGroup"] = object_group

        if is_defined(
            execution_context_id
        ):
            params["executionContextId"] = execution_context_id

        return self._send_command(
            "DOM.resolveNode",
            params
        )

    def set_attribute_value(
        self,
        node_id: NodeId,
        name: str,
        value: str
    ):
        params = {
            "nodeId": node_id,
            "name": name,
            "value": value,
        }

        return self._send_command(
            "DOM.setAttributeValue",
            params
        )

    def set_attributes_as_text(
        self,
        node_id: NodeId,
        text: str,
        name: MaybeUndefined[str]
    ):
        params = {
            "nodeId": node_id,
            "text": text,
        }

        if is_defined(
            name
        ):
            params["name"] = name

        return self._send_command(
            "DOM.setAttributesAsText",
            params
        )

    def set_file_input_files(
        self,
        files: list,
        node_id: MaybeUndefined[NodeId],
        backend_node_id: MaybeUndefined[BackendNodeId],
        object_id: MaybeUndefined[RemoteObjectId]
    ):
        params = {
            "files": files,
        }

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
            "DOM.setFileInputFiles",
            params
        )

    def set_node_stack_traces_enabled(
        self,
        enable: bool
    ):
        params = {
            "enable": enable,
        }

        return self._send_command(
            "DOM.setNodeStackTracesEnabled",
            params
        )

    def get_node_stack_traces(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "DOM.getNodeStackTraces",
            params
        )

    def get_file_info(
        self,
        object_id: RemoteObjectId
    ):
        params = {
            "objectId": object_id,
        }

        return self._send_command(
            "DOM.getFileInfo",
            params
        )

    def set_inspected_node(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "DOM.setInspectedNode",
            params
        )

    def set_node_name(
        self,
        node_id: NodeId,
        name: str
    ):
        params = {
            "nodeId": node_id,
            "name": name,
        }

        return self._send_command(
            "DOM.setNodeName",
            params
        )

    def set_node_value(
        self,
        node_id: NodeId,
        value: str
    ):
        params = {
            "nodeId": node_id,
            "value": value,
        }

        return self._send_command(
            "DOM.setNodeValue",
            params
        )

    def set_outer_html(
        self,
        node_id: NodeId,
        outer_html: str
    ):
        params = {
            "nodeId": node_id,
            "outerHTML": outer_html,
        }

        return self._send_command(
            "DOM.setOuterHTML",
            params
        )

    def undo(
        self
    ):
        params = {}

        return self._send_command(
            "DOM.undo",
            params
        )

    def get_frame_owner(
        self,
        frame_id: FrameId
    ):
        params = {
            "frameId": frame_id,
        }

        return self._send_command(
            "DOM.getFrameOwner",
            params
        )

    def get_container_for_node(
        self,
        node_id: NodeId,
        container_name: MaybeUndefined[str],
        physical_axes: MaybeUndefined[PhysicalAxes],
        logical_axes: MaybeUndefined[LogicalAxes]
    ):
        params = {
            "nodeId": node_id,
        }

        if is_defined(
            container_name
        ):
            params["containerName"] = container_name

        if is_defined(
            physical_axes
        ):
            params["physicalAxes"] = physical_axes

        if is_defined(
            logical_axes
        ):
            params["logicalAxes"] = logical_axes

        return self._send_command(
            "DOM.getContainerForNode",
            params
        )

    def get_querying_descendants_for_container(
        self,
        node_id: NodeId
    ):
        params = {
            "nodeId": node_id,
        }

        return self._send_command(
            "DOM.getQueryingDescendantsForContainer",
            params
        )

