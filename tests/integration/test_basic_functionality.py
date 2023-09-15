from unittest import TestCase

from cdp.chrome import Chrome


class Tests(TestCase):
    def test(self):
        chrome = Chrome.start()

        target = chrome.get_targets()[0]
        target.open_session()

        target.domains.runtime.enable()

        result = target.domains.runtime.release_object('test')
        result.wait()

        result = target.domains.page.navigate('https://google.com')
        result.wait()

    def test_2(self):
        pass
