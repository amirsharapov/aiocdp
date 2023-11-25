from unittest import TestCase

from aiocdp import Connection, EventStreamReader


class TestConnection(TestCase):

    def test_open_and_close_stream(self):
        connection = Connection('ws://localhost:9222')

        connection.open_stream(['lol'])
        stream = connection.open_stream(['lol'])
        stream.close()

    def test_open_stream_context_manager(self):
        connection = Connection('ws://localhost:9222')

        with connection.open_stream(['lol']) as stream:
            self.assertIsInstance(
                stream,
                EventStreamReader
            )
            self.assertFalse(
                stream.is_closed
            )

        self.assertTrue(
            stream.is_closed
        )

        stream = connection.open_stream(['lol'])
        stream.close()

        self.assertIsInstance(
            stream,
            EventStreamReader
        )
        self.assertTrue(
            stream.is_closed
        )
