from unittest import TestCase

from pycdp.extras.http_listener import HTTPListener


class Tests(TestCase):
    def test_http_listener(self):
        listener = HTTPListener()
