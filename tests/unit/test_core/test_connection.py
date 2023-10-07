from unittest import TestCase

from pycdp import Connection, EventStreamReader


class TestConnection(TestCase):

    def test_open_and_close_stream(self):
        connection = Connection('ws://localhost:9222')

        connection.open_stream(['lol'])
        stream = connection.open_stream(['lol'])
        stream.close()

    def test_open_stream_context_manager(self):
        connection = Connection('ws://localhost:9222')

        with connection.open_stream(['lol']) as reader:
            self.assertIsInstance(
                reader,
                EventStreamReader
            )
            self.assertFalse(
                reader.is_closed
            )

        self.assertTrue(
            reader.is_closed
        )

        reader = connection.open_stream(['lol'])
        reader.close()

        self.assertIsInstance(
            reader,
            EventStreamReader
        )
        self.assertTrue(
            reader.is_closed
        )
