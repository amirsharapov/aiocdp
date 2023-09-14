from unittest import TestCase

from cdp.chrome import Chrome


class Tests(TestCase):
    async def test(self):
        chrome = Chrome.connect()

        target = chrome.get_targets()[0]
        target.open_session()

        target.domains.runtime.enable()

        response = target.runtime.evaluate('console.log("Hello, world!")')
        print(response)

    async def test_2(self):
        pass
