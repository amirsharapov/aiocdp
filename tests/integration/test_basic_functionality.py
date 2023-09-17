import time
from unittest import TestCase

from cdp.chrome import Chrome


class Tests(TestCase):
    def test(self):
        chrome = Chrome.start()

        time.sleep(1)

        target = chrome.get_targets()[0]
        target.connect()
        target.open_session()

        target.domains.runtime.enable()

        result = target.domains.page.navigate('https://google.com')
        result.get()

        print(result)

    def test_2(self):
        pass
