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
                'Debugger.enable'
            )

            await target.io.send(
                'Debugger.setBreakpointsActive',
                {
                    'active': True
                }
            )

            await target.domains.runtime.enable()
            await target.domains.page.enable()
            await target.domains.network.enable()

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
