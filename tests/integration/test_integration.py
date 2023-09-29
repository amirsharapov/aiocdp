import asyncio
import time
from unittest import TestCase

from pycdp.chrome import Chrome


class Tests(TestCase):
    def test_open_tab(self):
        async def _():
            chrome = Chrome.create().start()

            time.sleep(1)

            chrome.open_tab('https://google.com')

        asyncio.get_event_loop().run_until_complete(_())

    def test(self):
        async def _():
            chrome = Chrome.create().start()

            time.sleep(1)

            targets = chrome.get_targets()
            target = targets[0]

            await target.connect()
            await target.start_session()

            print(await target.send_and_await_response(
                'Page.enable'
            ))

            print(await target.send_and_await_response(
                'Network.enable'
            ))

            await target.send(
                'Debugger.enable',
            )

            stream = await target.open_stream(['Page.frameStoppedLoading'])
            future = stream.next

            await target.send_and_await_response(
                'Page.navigate',
                {
                    'url': 'https://google.com'
                }
            )

            result = await future

            print(result)

            result = await target.send_and_await_response(
                'Runtime.evaluate',
                {
                    'expression': 'document.querySelector("form")'
                }
            )

            print(result)

        asyncio.get_event_loop().run_until_complete(_())
