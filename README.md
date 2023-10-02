# PYCDP

### ** STATUS: UNDER DEVELOPMENT **

This library will provide wrapper around the Chrome DevTools Protocol.

## Scope

This library is built to be "one and done" with the exception of performance optimizations or bug fixes.
This library should NOT depend on the CDP spec as the spec is subject to change.

## Motivation

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

## Notes:

- The `pycdp` package will be published to PyPI
