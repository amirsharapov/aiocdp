# AIOCDP

This library provides an async wrapper around the Chrome DevTools Protocol.

## About

To be the underlying engine for any projects using Chrome DevTools Protocol. This library should embody the following:

1. **Flexibility**: Allow for any use case that the CDP supports.
2. **Minimal external dependencies**: Opt for built-in python libraries where possible.
3. **Clean code**: No hacks, workarounds, or spaghetti code.

## Usage

TBD

## Package

You can find the AIOCDP package published to pypi.org/project/aiocdp

### Organization

- `aiocdp` - Root package. Contains core and utility modules
- `aiocdp.core` - Core functionality for communicating with the Chrome DevTools Protocol

# For Developers

## Scope

This library is built to be "one and done" except for performance optimizations or design changes.
This library should limit the dependencies it has on the CDP unless it's a core feature (opening sessions, etc.).

## Dependencies

- Built-in `dataclasses` module for classes
- Built-in `typing` module for type hints, enum literals, and other goodies
- Built-in `json` module for JSON serialization
- Built-in `asyncio` module for async functionality
- External `requests` module for HTTP communication
- External `websockets` module for websocket communication
## Internals

### Module Organization

- `aiocdp` - Root package. Contains core and utility modules
- `aiocdp.core` - Core functionality for communicating with the Chrome DevTools Protocol
- `aiocdp.core.chrome.Chrome` -> Represents the Chrome instance / process.
- `aiocdp.core.target.Target` -> Represents a chrome devtools protocol target (Page, Frame, Worker, etc)
- `aiocdp.core.connection.Connection` -> Represents a websocket connection to a target
- `aiocdp.core.session.TargetSession` -> Represents a session to a specific target.
- `aiocdp.core.stream.EventStream` -> Represents a stream of events from a connection.
- `aiocdp.core.stream.EventStreamReader` -> Readonly reader to an event stream.
