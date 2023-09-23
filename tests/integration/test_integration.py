import time
from unittest import TestCase

from cdp.chrome import Chrome


class Tests(TestCase):
    def test(self):
        chrome = Chrome.start()

        time.sleep(1)

        targets = chrome.get_targets()
        target = targets[0]
        target.connect()
        target.open_session()

        result = target.domains.page.navigate(
            url='https://www.google.com'
        )

        result.get()

        x = {
            'node_id': 1
        }

        target.domains.accessibility.some_method(x)

        target.domains.accessibility.some_method({})
