# PYCDP

### ** STATUS: UNDER DEVELOPMENT **

This library will provide a thin, but functional wrapper around the Chrome DevTools Protocol.
Every week, a CICD pipeline will run to fetch the latest spec and regenerate the library.

## Inspiration

Code generation methodology inspired by the `python-chrome-devtools-protocol` package.
`pycdp` follows the same idea with several key additions:

- Automatic CICD pipeline to refresh the library
- Websocket communication implemented directly into this library
- Changes to the key interfaces for a more fluent API

## Internals:

### Targets

When we setup the internals, we aimed to have as little external dependencies as possible.
If we were to implement an external dependency, we need to make sure that it is compatible with
the standard libraries python ships with. `websocket-client` is a library we had to drop for
this reason.


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