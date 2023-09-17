import time
from unittest import TestCase

from cdp.chrome import Chrome


class Tests(TestCase):
    def test(self):
        chrome = Chrome.start()

        target = next(chrome.get_targets(), None)
        target.connect()
        target.open_session()

        result = target.domains.page.navigate('https://google.com')
        result.get()

    def test_2(self):
        pass
