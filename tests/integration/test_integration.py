import time
from dataclasses import dataclass
from typing import TypedDict
from unittest import TestCase

from cdp.chrome import Chrome
from cdp.domains.domains import Domains


class Tests(TestCase):
    def test(self):
        chrome = Chrome.start()

        time.sleep(1)

        targets = chrome.get_targets()
        target = targets[0]
        target.connect()

        result = target.domains.page.navigate(
            url='https://www.google.com'
        )

        result.get()

        x = {
            'node_id': 1
        }

        target.domains.accessibility.some_method(x)

        target.domains.accessibility.some_method(
            {'node_id': 1},
            node_id=''
        )
