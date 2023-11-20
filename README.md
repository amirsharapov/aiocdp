# AIOCDP

### ** STATUS: UNDER DEVELOPMENT **

This library provides an async wrapper around the Chrome DevTools Protocol.

## About

### Scope

This library is built to be "one and done" with the exception of performance optimizations or bug fixes.
This library should limit the dependencies it has on the CDP spec with the exception of
starting / stopping sessions and other generic functionality.

### Vision

To be the underlying engine for any projects using Chrome DevTools Protocol.

### Key Values

1. Flexibility
2. Minimal external dependencies / Compatible with built-in python libraries. No unnecessary dependencies.
3. Quality code and documentation. No hacks, workarounds, or spaghetti code.

## Package

You can find the AIOCDP package published to pypi.org/project/aiocdp

### Organization

- `aiocdp` - Root package. Contains core and utility modules
- `aiocdp.core` - Core functionality for communicating with the Chrome DevTools Protocol

### Dependencies

#### Built-in
- Python `dataclasses` module for classes
- Python `typing` module for type hints, enum literals, and other goodies
- Python `asyncio` module for async functionality

#### External
- Python `requests` module for HTTP communication
- Python `websockets` module for websocket communication

## Internals

### Main Components

- `aiocdp.core.chrome.Chrome` -> Represents the Chrome instance / process.
- `aiocdp.core.target.Target` -> Represents a chrome devtools protocol target (Page, Frame, Worker, etc)
- `aiocdp.core.connection.Connection` -> Represents a websocket connection to a target
- `aiocdp.core.session.TargetSession` -> Represents a session to a specific target.
- `aiocdp.core.stream.EventStream` -> Represents a stream of events from a connection.
- `aiocdp.core.stream.EventStreamReader` -> Readonly reader to an event stream.

## Notes:

- The `aiocdp` package will be published to PyPI
