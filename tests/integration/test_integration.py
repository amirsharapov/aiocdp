import asyncio
import time
from unittest import TestCase

from pycdp.chrome import Chrome


class Tests(TestCase):
    def test_open_tab(self):
        async def _():
            chrome = Chrome.start()

            time.sleep(1)

            chrome.open_tab('https://google.com')

        asyncio.get_event_loop().run_until_complete(_())

    def test(self):
        async def _():
            chrome = Chrome.start()

            time.sleep(1)

            targets = chrome.get_targets()
            target = targets[0]

            await target.connect()
            await target.start_session()

            await target.send(
                'Debugger.enable',
            )

            await target.send(
                'Page.enable'
            )

            await target.send(
                'Network.enable'
            )

            stream = await target.open_stream(['Page.frameStoppedLoading'])
            future = stream.next

            await target.send(
                'Page.navigate',
                {
                    'url': 'https://google.com'
                }
            )

            result = await future

            print(result)

            result = await target.send(
                'Runtime.evaluate',
                {
                    'expression': 'document.querySelector("form")'
                }
            )

            print(result)
            print(await result)

        asyncio.get_event_loop().run_until_complete(_())
