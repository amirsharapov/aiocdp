from unittest import TestCase

from cdp.chrome import Chrome


class Tests(TestCase):
    def test(self):
        chrome = Chrome.start()

        target = next(chrome.get_targets(), None)
        # target.open_session()
        target.connect()

        target.domains.runtime.enable()

        result = target.domains.runtime.release_object('test')
        result.get()

        result = target.domains.page.navigate('https://google.com')
        target.domains.runtime.call_function_on()
        result.get()

    def test_2(self):
        pass
