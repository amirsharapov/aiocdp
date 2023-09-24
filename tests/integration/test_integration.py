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
            await target.open_session()

            await target.io.send(
                'Debugger.enable',
            )

            await target.io.send(
                'Page.enable'
            )

            await target.io.send(
                'Network.enable'
            )

            result = {
                'error_text': None
            }

            while 'error_text' in result:
                time.sleep(.3)

                result = await target.io.send(
                    'Page.navigate',
                    {
                        'url': 'https://google.com'
                    }
                )

            result = await target.io.send(
                'Runtime.evaluate',
                {
                    'expression': 'document.querySelector("form")'
                }
            )

        asyncio.get_event_loop().run_until_complete(_())
