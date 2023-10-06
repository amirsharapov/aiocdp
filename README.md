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
2. Minimal external dependencies
3. Compatible with built-in python libraries

## Package

### Organization

- `pycdp` - Root package. Contains core and utility modules
- `pycdp.core` - Core functionality for communicating with the Chrome DevTools Protocol

### Dependencies

- Python `typing` module for type hints, enum literals, and other goodies
- Python `asyncio` module for async futures (Support for other async libraries is TBD)
- Python `websockets` module for websocket communication (Support for other WS libraries is TBD)

## Internals

### Main Components

- `pycdp.core.chrome.Chrome`
- `pycdp.core.connection.Connection`
- `pycdp.core.connection.Session` # TODO
- `pycdp.core.target.Target`
- `pycdp.core.stream.EventStream`
- `pycdp.core.stream.EventStreamReader`

## Limitations

- Does not support multiple sessions per target. # TODO

## Notes:

- The `pycdp` package will be published to PyPI
