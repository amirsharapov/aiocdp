import asyncio
import time
from unittest import TestCase

from cdp.chrome import Chrome


class Tests(TestCase):
    def test_conn(self):
        async def _():
            chrome = Chrome.start()

            time.sleep(.5)

            targets = chrome.get_targets()
            target = targets[0]

            await target.connect()
            await target.open_session()

            await target.send_command(
                'Page.enable',
                {}
            )

            stream = await target.connection.open_stream(
                ['Page.loadEventFired']
            )

            await target.connection.send_request(
                'Page.navigate',
                {
                    'url': 'https://google.com'
                }
            )

            event = await stream.wait_until_next()

            await asyncio.sleep(2)

            print(event)

        asyncio.get_event_loop().run_until_complete(_())

    def test(self):
        async def _():
            chrome = Chrome.start()

            time.sleep(1)

            targets = chrome.get_targets()
            target = targets[0]

            await target.connect()
            await target.open_session()

            stream = await target.domains.page.open_event_stream('load_event_fired')

            await stream.wait_until_next()

            result = {
                'error_text': None
            }

            while 'error_text' in result:
                time.sleep(.3)
                result = await target.domains.page.navigate(
                    url='https://google.com'
                )

            result = await target.domains.runtime.evaluate(
                expression='r = document.querySelector("form"); console.log(r)'
            )

            print(result)

        asyncio.get_event_loop().run_until_complete(_())
