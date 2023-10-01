import contextlib
import contextvars

from pycdp import Target
from pycdp.extras.web_scraper import query_by_xpath

target_context_var = contextvars.ContextVar(
    'target'
)


@contextlib.contextmanager
def setup_target_context(target: Target):
    token = target_context_var.set(target)

    try:
        yield

    finally:
        target_context_var.reset(
            token
        )


async def click_xy(x: int, y: int):
    await press(x, y)
    await release(x, y)

async def click_xpath(self, xpath: str):
    result = await query_by_xpath(
        xpath
    )


async def click_node_id(self, node_id: int):
    pass


async def click_object_id(self, object_id: str):
    pass


async def press(x: int, y: int):
    target = target_context_var.get()

    await target.send_and_await_response(
        'Input.dispatchMouseEvent',
        {
            'type': 'mousePressed',
            'x': x,
            'y': y,
            'button': 'left',
            'clickCount': 1
        }
    )


async def release(x: int, y: int):
    target = target_context_var.get()

    await target.send_and_await_response(
        'Input.dispatchMouseEvent',
        {
            'type': 'mouseReleased',
            'x': x,
            'y': y,
            'button': 'left',
            'clickCount': 1
        }
    )
