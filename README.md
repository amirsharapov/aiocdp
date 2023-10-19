# PYCDP

### ** STATUS: UNDER DEVELOPMENT **

This library provides an async wrapper around the Chrome DevTools Protocol.

## About

### Scope

This library is built to be "one and done" with the exception of performance optimizations or bug fixes.
This library should limit the dependencies it has on the CDP spec with the exception of
starting / stopping sessions and other core functionality.

### Motivation

I hope this library becomes the underlying engine for any projects using Chrome DevTools Protocol.
With that in mind, we need to achieve the following points:

1. Flexibility
2. Minimal external dependencies / Compatible with built-in python libraries. No unnecessary dependencies.
3. Quality code and documentation. No hacks, workarounds, or spaghetti code.

## Package

### Organization

- `pycdp` - Root package. Contains core and utility modules
- `pycdp.core` - Core functionality for communicating with the Chrome DevTools Protocol

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

- `pycdp.core.chrome.Chrome` -> Represents the Chrome instance / process.
- `pycdp.core.target.Target` -> Represents a chrome devtools protocol target (Page, Frame, Worker, etc)
- `pycdp.core.connection.Connection` -> Represents a websocket connection to a target
- `pycdp.core.session.TargetSession` -> Represents a session to a specific target.
- `pycdp.core.stream.EventStream` -> Represents a stream of events from a connection.
- `pycdp.core.stream.EventStreamReader` -> Readonly reader to an event stream.

## Notes:

- The `pycdp` package will be published to PyPI
