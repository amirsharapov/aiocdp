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
from cdp.domains.runtime.types import (
    CallArgument,
    ExecutionContextId,
    ScriptId,
    TimeDelta,
    StackTrace,
    RemoteObjectId,
    ExceptionDetails,
    UniqueDebuggerId,
    StackTraceId,
    RemoteObject
)
from cdp.domains.debugger.types import (
    Location,
    CallFrameId,
    BreakpointId
)


@dataclass
class Debugger(BaseDomain):
    def continue_to_location(
        self,
        location: Location,
        target_call_frames: MaybeUndefined[]
    ):
        params = {
            "location": location,
        }

        if is_defined(
            target_call_frames
        ):
            params[] = target_call_frames

        return self._send_command(
            "Debugger.continueToLocation",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Debugger.disable",
            params
        )

    def enable(
        self,
        max_scripts_cache_size: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            max_scripts_cache_size
        ):
            params[] = max_scripts_cache_size

        return self._send_command(
            "Debugger.enable",
            params
        )

    def evaluate_on_call_frame(
        self,
        call_frame_id: CallFrameId,
        expression: str,
        object_group: MaybeUndefined[],
        include_command_line_api: MaybeUndefined[],
        silent: MaybeUndefined[],
        return_by_value: MaybeUndefined[],
        generate_preview: MaybeUndefined[],
        throw_on_side_effect: MaybeUndefined[],
        timeout: MaybeUndefined[]
    ):
        params = {
            "callFrameId": call_frame_id,
            "expression": expression,
        }

        if is_defined(
            object_group
        ):
            params[] = object_group

        if is_defined(
            include_command_line_api
        ):
            params[] = include_command_line_api

        if is_defined(
            silent
        ):
            params[] = silent

        if is_defined(
            return_by_value
        ):
            params[] = return_by_value

        if is_defined(
            generate_preview
        ):
            params[] = generate_preview

        if is_defined(
            throw_on_side_effect
        ):
            params[] = throw_on_side_effect

        if is_defined(
            timeout
        ):
            params[] = timeout

        return self._send_command(
            "Debugger.evaluateOnCallFrame",
            params
        )

    def get_possible_breakpoints(
        self,
        start: Location,
        end: MaybeUndefined[],
        restrict_to_function: MaybeUndefined[]
    ):
        params = {
            "start": start,
        }

        if is_defined(
            end
        ):
            params[] = end

        if is_defined(
            restrict_to_function
        ):
            params[] = restrict_to_function

        return self._send_command(
            "Debugger.getPossibleBreakpoints",
            params
        )

    def get_script_source(
        self,
        script_id: ScriptId
    ):
        params = {
            "scriptId": script_id,
        }

        return self._send_command(
            "Debugger.getScriptSource",
            params
        )

    def get_stack_trace(
        self,
        stack_trace_id: StackTraceId
    ):
        params = {
            "stackTraceId": stack_trace_id,
        }

        return self._send_command(
            "Debugger.getStackTrace",
            params
        )

    def pause(
        self
    ):
        params = {}

        return self._send_command(
            "Debugger.pause",
            params
        )

    def pause_on_async_call(
        self,
        parent_stack_trace_id: StackTraceId
    ):
        params = {
            "parentStackTraceId": parent_stack_trace_id,
        }

        return self._send_command(
            "Debugger.pauseOnAsyncCall",
            params
        )

    def remove_breakpoint(
        self,
        breakpoint_id: BreakpointId
    ):
        params = {
            "breakpointId": breakpoint_id,
        }

        return self._send_command(
            "Debugger.removeBreakpoint",
            params
        )

    def restart_frame(
        self,
        call_frame_id: CallFrameId
    ):
        params = {
            "callFrameId": call_frame_id,
        }

        return self._send_command(
            "Debugger.restartFrame",
            params
        )

    def resume(
        self
    ):
        params = {}

        return self._send_command(
            "Debugger.resume",
            params
        )

    def search_in_content(
        self,
        script_id: ScriptId,
        query: str,
        case_sensitive: MaybeUndefined[],
        is_regex: MaybeUndefined[]
    ):
        params = {
            "scriptId": script_id,
            "query": query,
        }

        if is_defined(
            case_sensitive
        ):
            params[] = case_sensitive

        if is_defined(
            is_regex
        ):
            params[] = is_regex

        return self._send_command(
            "Debugger.searchInContent",
            params
        )

    def set_async_call_stack_depth(
        self,
        max_depth: int
    ):
        params = {
            "maxDepth": max_depth,
        }

        return self._send_command(
            "Debugger.setAsyncCallStackDepth",
            params
        )

    def set_blackbox_patterns(
        self,
        patterns: list
    ):
        params = {
            "patterns": patterns,
        }

        return self._send_command(
            "Debugger.setBlackboxPatterns",
            params
        )

    def set_blackboxed_ranges(
        self,
        script_id: ScriptId,
        positions: list
    ):
        params = {
            "scriptId": script_id,
            "positions": positions,
        }

        return self._send_command(
            "Debugger.setBlackboxedRanges",
            params
        )

    def set_breakpoint(
        self,
        location: Location,
        condition: MaybeUndefined[]
    ):
        params = {
            "location": location,
        }

        if is_defined(
            condition
        ):
            params[] = condition

        return self._send_command(
            "Debugger.setBreakpoint",
            params
        )

    def set_instrumentation_breakpoint(
        self,
        instrumentation: str
    ):
        params = {
            "instrumentation": instrumentation,
        }

        return self._send_command(
            "Debugger.setInstrumentationBreakpoint",
            params
        )

    def set_breakpoint_by_url(
        self,
        line_number: int,
        url: MaybeUndefined[],
        url_regex: MaybeUndefined[],
        script_hash: MaybeUndefined[],
        column_number: MaybeUndefined[],
        condition: MaybeUndefined[]
    ):
        params = {
            "lineNumber": line_number,
        }

        if is_defined(
            url
        ):
            params[] = url

        if is_defined(
            url_regex
        ):
            params[] = url_regex

        if is_defined(
            script_hash
        ):
            params[] = script_hash

        if is_defined(
            column_number
        ):
            params[] = column_number

        if is_defined(
            condition
        ):
            params[] = condition

        return self._send_command(
            "Debugger.setBreakpointByUrl",
            params
        )

    def set_breakpoint_on_function_call(
        self,
        object_id: RemoteObjectId,
        condition: MaybeUndefined[]
    ):
        params = {
            "objectId": object_id,
        }

        if is_defined(
            condition
        ):
            params[] = condition

        return self._send_command(
            "Debugger.setBreakpointOnFunctionCall",
            params
        )

    def set_breakpoints_active(
        self,
        active: bool
    ):
        params = {
            "active": active,
        }

        return self._send_command(
            "Debugger.setBreakpointsActive",
            params
        )

    def set_pause_on_exceptions(
        self,
        state: str
    ):
        params = {
            "state": state,
        }

        return self._send_command(
            "Debugger.setPauseOnExceptions",
            params
        )

    def set_return_value(
        self,
        new_value: CallArgument
    ):
        params = {
            "newValue": new_value,
        }

        return self._send_command(
            "Debugger.setReturnValue",
            params
        )

    def set_script_source(
        self,
        script_id: ScriptId,
        script_source: str,
        dry_run: MaybeUndefined[]
    ):
        params = {
            "scriptId": script_id,
            "scriptSource": script_source,
        }

        if is_defined(
            dry_run
        ):
            params[] = dry_run

        return self._send_command(
            "Debugger.setScriptSource",
            params
        )

    def set_skip_all_pauses(
        self,
        skip: bool
    ):
        params = {
            "skip": skip,
        }

        return self._send_command(
            "Debugger.setSkipAllPauses",
            params
        )

    def set_variable_value(
        self,
        scope_number: int,
        variable_name: str,
        new_value: CallArgument,
        call_frame_id: CallFrameId
    ):
        params = {
            "scopeNumber": scope_number,
            "variableName": variable_name,
            "newValue": new_value,
            "callFrameId": call_frame_id,
        }

        return self._send_command(
            "Debugger.setVariableValue",
            params
        )

    def step_into(
        self,
        break_on_async_call: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            break_on_async_call
        ):
            params[] = break_on_async_call

        return self._send_command(
            "Debugger.stepInto",
            params
        )

    def step_out(
        self
    ):
        params = {}

        return self._send_command(
            "Debugger.stepOut",
            params
        )

    def step_over(
        self
    ):
        params = {}

        return self._send_command(
            "Debugger.stepOver",
            params
        )

