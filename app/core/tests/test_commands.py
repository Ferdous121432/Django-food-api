from django.core.management import call_command
from django.test import TestCase
from unittest.mock import patch, MagicMock
from psycopg2 import OperationalError as Psycopg2OpError


class CommandTests(TestCase):

    @patch('core.management.commands.wait_for_db.time.sleep')
    def test_wait_for_db_ready(self, sleep_mock):
        """Should return immediately when DB available."""
        with patch('core.management.commands.wait_for_db.connections') as conn_mock:
            conn_mock.__getitem__.return_value.cursor.return_value = MagicMock()
            call_command('wait_for_db')
            self.assertEqual(sleep_mock.call_count, 0)

    @patch('core.management.commands.wait_for_db.time.sleep')
    def test_wait_for_db_delay(self, sleep_mock):
        """Should retry until DB is available."""
        with patch('core.management.commands.wait_for_db.connections') as conn_mock:
            # Raise exception 3 times, then succeed
            conn_mock.__getitem__.return_value.cursor.side_effect = [
                Psycopg2OpError('DB unavailable'),
                Psycopg2OpError('DB unavailable'),
                Psycopg2OpError('DB unavailable'),
                MagicMock()
            ]
            call_command('wait_for_db')
            self.assertEqual(sleep_mock.call_count, 3)
