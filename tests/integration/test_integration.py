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

            await target.domains.network.enable()

            result = await target.domains.page.navigate(
                url='https://youtube.com'
            )

            print(result)

            time.sleep(1)

        asyncio.run(_())
