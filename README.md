# PYCDP

### ** STATUS: UNDER DEVELOPMENT **

This library will provide a thin, but functional wrapper around the Chrome DevTools Protocol.
Every week, a CICD pipeline will run to fetch the latest spec and regenerate the library.

## Inspiration

Heavy inspiration comes from the `python-chrome-devtools-protocol` package.
This library follows the same idea (generating wrapper layer from the JSON spec),
but uses a different approach and changes developer-facing interfaces.

## Internals:

### Generator

- Python `requests` module for downloading the latest JSON files (TODO)
- Python `json` module for parsing the JSON
- Python `ast` module for code structure and generation

### Package

- Python `dataclass` decorator for complex types
- Python `typing` module for type hints, enum literals, and other goodies

### Releases

- Github actions (or GitLab CI/CD - whichever is more cost effective) (TODO)