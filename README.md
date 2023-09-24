# PYCDP

### ** STATUS: UNDER DEVELOPMENT **

This library will provide a thin, but functional wrapper around the Chrome DevTools Protocol.
Every week, a CICD pipeline will run to fetch the latest spec and regenerate the library.

## Inspiration

Code generation methodology inspired by the `python-chrome-devtools-protocol` package.
This library (`pycdp`) follows the same idea with several key additions:

- Code generation is for stub files and constants only
- Automatic CICD pipeline to refresh the library
- Websocket communication implementation
- Updates to interfaces for better type hints and code completion

## Internals:

### Goals

We aim to be the underlying engine for any libraries or projects using Chrome DevTools Protocol.

With that in mind, we need to achieve the following points:

1. Flexibility
2. Minimal external dependencies
3. Compatible with built-in python libraries

### Generator

- Python `requests` module for downloading the latest JSON files (TODO)
- Python `json` module for parsing the JSON
- Python `ast` module for code structure and generation

### Package

- Python `dataclass` decorator for complex types
- Python `typing` module for type hints, enum literals, and other goodies
- Python `asyncio` module for async futures (Support for other async libraries is TBD)
- Python `websockets` module for websocket communication (Support for other WS libraries is TBD)

### Releases

- Github actions (or GitLab CI/CD - whichever is more cost effective) (TODO)

## Notes:

- The `pycdp` package will be published to PyPI
- The internal `cdp.domains.mapper` function contains all the mapping functions due the the nature of the
  Chrome DevTools Protocol. This is a temporary solution until we can find a better way to handle this.