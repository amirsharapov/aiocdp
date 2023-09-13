This library parses the Chrome DevTools Protocol JSON files and generates a
thin wrapper around the API.

The goal of the generator is to generate production ready package releases
on a consistent interval based on the latest spec.

### Internals:

#### Generator
- Python `requests` module for downloading the latest JSON files
- Python `json` module for parsing the JSON
- Custom algorithm to define dependencies between domains
- Python `ast` module for code structure
- Custom algorithm to walk the AST tree and generate the files

#### Package
- Python `dataclass` decorator for mapped types
- Python `typing` module for type hints and other goodies
