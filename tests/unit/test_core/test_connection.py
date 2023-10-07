from unittest import TestCase

from pycdp import Connection


class TestConnection(TestCase):
    connection = Connection('ws://localhost:9222')

    stream = connection.open_stream(['lol'])
    stream = connection.open_stream(['lol'])
    stream.close()
