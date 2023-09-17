import time
from unittest import TestCase

from cdp.chrome import Chrome


class Tests(TestCase):
    def test(self):
        chrome = Chrome.start()

        target = chrome.get_targets()[0]
        target.connect()
        target.open_session()

        result = target.domains.page.navigate('https://google.com')
        result.get()

        result = target.domains.page.get_frame_tree()
        result = result.get()

        print(result)

    def test_2(self):
        pass
