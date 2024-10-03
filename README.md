# AIOCDP

This library provides an async wrapper around the Chrome DevTools Protocol.

## About

To be the underlying engine for any projects using Chrome DevTools Protocol. This library should embody the following:

1. **Flexibility**: Allow for any use case that the CDP supports.
2. **Minimal external dependencies**: Opt for built-in python libraries where possible.
3. **Clean code**: No hacks, workarounds, or spaghetti code.

## Usage

### Starting Chrome

The following will launch chrome through the command line.

```python
import asyncio

from aiocdp import Chrome


async def setup_chrome():
    chrome = Chrome.init(
        host="localhost",
        port=9222,
    )
    
    chrome.start()
    
    # run your logic here
    

if __name__ == "__main__":
    asyncio.run(setup_chrome())
```

_**NOTE:** If you had chrome open previously, you may run into connection issues.
If this is the case, close your tabs, run the script to relaunch chrome, and then reopen your tabs._

### Opening a tab

```python
import asyncio

from aiocdp import Chrome


async def setup_tabs():
    chrome = Chrome.init(
        host="localhost",
        port=9222,
    )

    chrome.start()

    # opens a new tab. Return aiocdp.ITarget instance.
    target = chrome.new_tab("https://www.google.com")
    target = chrome.new_tab("https://www.yahoo.com")
    target = chrome.new_tab("https://www.github.com/amirdevstudio/aiocdp")

    # opens a new tab. The parameter is optional
    target = chrome.new_tab()


if __name__ == "__main__":
    asyncio.run(setup_tabs())
```

## Package

You can find the AIOCDP package published to pypi.org/project/aiocdp

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

## TODO:

- Setup proper typehints for setting subclasses. (use a type var in a shared module)
- documentation

## Publishing to PyPi

1. Update the version in `setup.py`
2. Run `python -m pip install build twine`
3. Run `python -m build`
4. Run `twine check dist/*`
5. Run `twine upload dist/aiocdp-<MAJOR>.<MINOR>.<PATCH>*`