import asyncio
import time
from unittest import TestCase

from aiocdp import Chrome, logging

logging.enable_logging(['*'])


class Tests(TestCase):
    def test_open_tab(self):
        async def _():
            chrome = Chrome()
            chrome.start()

            time.sleep(1)

            chrome.open_tab('https://yahoo.com')

            time.sleep(1)

            targets = chrome.get_targets()
            target = targets[0]

            await target.connect()

            print(await target.send_and_await_response(
                'Page.navigate',
                {
                    'url': 'https://google.com'
                }
            ))

        asyncio.get_event_loop().run_until_complete(_())

    def test(self):
        async def _():
            chrome = Chrome()
            chrome.start(
                extra_cli_args=[
                    '--guest'
                ],
                popen_kwargs={
                    'shell': True
                }
            )

            time.sleep(1)

            targets = chrome.get_targets()
            target = targets[0]

            await target.connect()

            session = await target.open_session()

            print(await session.send_and_await_response(
                'Page.enable'
            ))

            reader = session.open_stream(['Page.frameStoppedLoading'])

            await session.send_and_await_response(
                'Page.navigate',
                {
                    'url': 'https://google.com'
                }
            )

            async for event in reader.iterate():
                print(event)
                break

            result = await target.send_and_await_response(
                'Runtime.evaluate',
                {
                    'expression': 'document.querySelector("form")'
                }
            )

            print(result)

        asyncio.get_event_loop().run_until_complete(_())
