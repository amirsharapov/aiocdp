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
from cdp.domains.input.types import (
    GestureSourceType,
    DragData,
    TimeSinceEpoch,
    MouseButton
)


@dataclass
class Input(BaseDomain):
    def dispatch_drag_event(
        self,
        type_: str,
        x: float,
        y: float,
        data: DragData,
        modifiers: MaybeUndefined[]
    ):
        params = {
            "type": type_,
            "x": x,
            "y": y,
            "data": data,
        }

        if is_defined(
            modifiers
        ):
            params[] = modifiers

        return self._send_command(
            "Input.dispatchDragEvent",
            params
        )

    def dispatch_key_event(
        self,
        type_: str,
        modifiers: MaybeUndefined[],
        timestamp: MaybeUndefined[],
        text: MaybeUndefined[],
        unmodified_text: MaybeUndefined[],
        key_identifier: MaybeUndefined[],
        code: MaybeUndefined[],
        key: MaybeUndefined[],
        windows_virtual_key_code: MaybeUndefined[],
        native_virtual_key_code: MaybeUndefined[],
        auto_repeat: MaybeUndefined[],
        is_keypad: MaybeUndefined[],
        is_system_key: MaybeUndefined[],
        location: MaybeUndefined[],
        commands: MaybeUndefined[]
    ):
        params = {
            "type": type_,
        }

        if is_defined(
            modifiers
        ):
            params[] = modifiers

        if is_defined(
            timestamp
        ):
            params[] = timestamp

        if is_defined(
            text
        ):
            params[] = text

        if is_defined(
            unmodified_text
        ):
            params[] = unmodified_text

        if is_defined(
            key_identifier
        ):
            params[] = key_identifier

        if is_defined(
            code
        ):
            params[] = code

        if is_defined(
            key
        ):
            params[] = key

        if is_defined(
            windows_virtual_key_code
        ):
            params[] = windows_virtual_key_code

        if is_defined(
            native_virtual_key_code
        ):
            params[] = native_virtual_key_code

        if is_defined(
            auto_repeat
        ):
            params[] = auto_repeat

        if is_defined(
            is_keypad
        ):
            params[] = is_keypad

        if is_defined(
            is_system_key
        ):
            params[] = is_system_key

        if is_defined(
            location
        ):
            params[] = location

        if is_defined(
            commands
        ):
            params[] = commands

        return self._send_command(
            "Input.dispatchKeyEvent",
            params
        )

    def insert_text(
        self,
        text: str
    ):
        params = {
            "text": text,
        }

        return self._send_command(
            "Input.insertText",
            params
        )

    def ime_set_composition(
        self,
        text: str,
        selection_start: int,
        selection_end: int,
        replacement_start: MaybeUndefined[],
        replacement_end: MaybeUndefined[]
    ):
        params = {
            "text": text,
            "selectionStart": selection_start,
            "selectionEnd": selection_end,
        }

        if is_defined(
            replacement_start
        ):
            params[] = replacement_start

        if is_defined(
            replacement_end
        ):
            params[] = replacement_end

        return self._send_command(
            "Input.imeSetComposition",
            params
        )

    def dispatch_mouse_event(
        self,
        type_: str,
        x: float,
        y: float,
        modifiers: MaybeUndefined[],
        timestamp: MaybeUndefined[],
        button: MaybeUndefined[],
        buttons: MaybeUndefined[],
        click_count: MaybeUndefined[],
        force: MaybeUndefined[],
        tangential_pressure: MaybeUndefined[],
        tilt_x: MaybeUndefined[],
        tilt_y: MaybeUndefined[],
        twist: MaybeUndefined[],
        delta_x: MaybeUndefined[],
        delta_y: MaybeUndefined[],
        pointer_type: MaybeUndefined[]
    ):
        params = {
            "type": type_,
            "x": x,
            "y": y,
        }

        if is_defined(
            modifiers
        ):
            params[] = modifiers

        if is_defined(
            timestamp
        ):
            params[] = timestamp

        if is_defined(
            button
        ):
            params[] = button

        if is_defined(
            buttons
        ):
            params[] = buttons

        if is_defined(
            click_count
        ):
            params[] = click_count

        if is_defined(
            force
        ):
            params[] = force

        if is_defined(
            tangential_pressure
        ):
            params[] = tangential_pressure

        if is_defined(
            tilt_x
        ):
            params[] = tilt_x

        if is_defined(
            tilt_y
        ):
            params[] = tilt_y

        if is_defined(
            twist
        ):
            params[] = twist

        if is_defined(
            delta_x
        ):
            params[] = delta_x

        if is_defined(
            delta_y
        ):
            params[] = delta_y

        if is_defined(
            pointer_type
        ):
            params[] = pointer_type

        return self._send_command(
            "Input.dispatchMouseEvent",
            params
        )

    def dispatch_touch_event(
        self,
        type_: str,
        touch_points: list,
        modifiers: MaybeUndefined[],
        timestamp: MaybeUndefined[]
    ):
        params = {
            "type": type_,
            "touchPoints": touch_points,
        }

        if is_defined(
            modifiers
        ):
            params[] = modifiers

        if is_defined(
            timestamp
        ):
            params[] = timestamp

        return self._send_command(
            "Input.dispatchTouchEvent",
            params
        )

    def cancel_dragging(
        self
    ):
        params = {}

        return self._send_command(
            "Input.cancelDragging",
            params
        )

    def emulate_touch_from_mouse_event(
        self,
        type_: str,
        x: int,
        y: int,
        button: MouseButton,
        timestamp: MaybeUndefined[],
        delta_x: MaybeUndefined[],
        delta_y: MaybeUndefined[],
        modifiers: MaybeUndefined[],
        click_count: MaybeUndefined[]
    ):
        params = {
            "type": type_,
            "x": x,
            "y": y,
            "button": button,
        }

        if is_defined(
            timestamp
        ):
            params[] = timestamp

        if is_defined(
            delta_x
        ):
            params[] = delta_x

        if is_defined(
            delta_y
        ):
            params[] = delta_y

        if is_defined(
            modifiers
        ):
            params[] = modifiers

        if is_defined(
            click_count
        ):
            params[] = click_count

        return self._send_command(
            "Input.emulateTouchFromMouseEvent",
            params
        )

    def set_ignore_input_events(
        self,
        ignore: bool
    ):
        params = {
            "ignore": ignore,
        }

        return self._send_command(
            "Input.setIgnoreInputEvents",
            params
        )

    def set_intercept_drags(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Input.setInterceptDrags",
            params
        )

    def synthesize_pinch_gesture(
        self,
        x: float,
        y: float,
        scale_factor: float,
        relative_speed: MaybeUndefined[],
        gesture_source_type: MaybeUndefined[]
    ):
        params = {
            "x": x,
            "y": y,
            "scaleFactor": scale_factor,
        }

        if is_defined(
            relative_speed
        ):
            params[] = relative_speed

        if is_defined(
            gesture_source_type
        ):
            params[] = gesture_source_type

        return self._send_command(
            "Input.synthesizePinchGesture",
            params
        )

    def synthesize_scroll_gesture(
        self,
        x: float,
        y: float,
        x_distance: MaybeUndefined[],
        y_distance: MaybeUndefined[],
        x_overscroll: MaybeUndefined[],
        y_overscroll: MaybeUndefined[],
        prevent_fling: MaybeUndefined[],
        speed: MaybeUndefined[],
        gesture_source_type: MaybeUndefined[],
        repeat_count: MaybeUndefined[],
        repeat_delay_ms: MaybeUndefined[],
        interaction_marker_name: MaybeUndefined[]
    ):
        params = {
            "x": x,
            "y": y,
        }

        if is_defined(
            x_distance
        ):
            params[] = x_distance

        if is_defined(
            y_distance
        ):
            params[] = y_distance

        if is_defined(
            x_overscroll
        ):
            params[] = x_overscroll

        if is_defined(
            y_overscroll
        ):
            params[] = y_overscroll

        if is_defined(
            prevent_fling
        ):
            params[] = prevent_fling

        if is_defined(
            speed
        ):
            params[] = speed

        if is_defined(
            gesture_source_type
        ):
            params[] = gesture_source_type

        if is_defined(
            repeat_count
        ):
            params[] = repeat_count

        if is_defined(
            repeat_delay_ms
        ):
            params[] = repeat_delay_ms

        if is_defined(
            interaction_marker_name
        ):
            params[] = interaction_marker_name

        return self._send_command(
            "Input.synthesizeScrollGesture",
            params
        )

    def synthesize_tap_gesture(
        self,
        x: float,
        y: float,
        duration: MaybeUndefined[],
        tap_count: MaybeUndefined[],
        gesture_source_type: MaybeUndefined[]
    ):
        params = {
            "x": x,
            "y": y,
        }

        if is_defined(
            duration
        ):
            params[] = duration

        if is_defined(
            tap_count
        ):
            params[] = tap_count

        if is_defined(
            gesture_source_type
        ):
            params[] = gesture_source_type

        return self._send_command(
            "Input.synthesizeTapGesture",
            params
        )

