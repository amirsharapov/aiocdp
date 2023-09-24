import asyncio
import time
from unittest import TestCase

from cdp.chrome import Chrome


class Tests(TestCase):
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

            await target.send(
                'Page.navigate',
                {
                    'url': 'https://google.com'
                }
            )

            result = await target.send(
                'Runtime.evaluate',
                {
                    'expression': 'document.querySelector("form")'
                }
            )

            print(result)
            print(await result)

        asyncio.get_event_loop().run_until_complete(_())
