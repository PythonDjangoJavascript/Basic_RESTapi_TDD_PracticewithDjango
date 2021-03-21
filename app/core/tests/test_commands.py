
from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandsTestCase(TestCase):
    """Tests Commands of core app"""

    def test_wait_for_db_ready(self):
        """Test wait for db command working"""

        with patch("django.db.utils.ConnectionHandler.__getitem__") as gi:
            gi.return_value = True      # setting connection true (moking)

            # calling our commads from core to check database conn
            call_command('wait_for_db')

            self.assertEqual(gi.call_count, 1)

    # moking default time funtion to avaoid waiting time
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):  # here ts is for patch decoration
        """test if connection failed for 5 times"""

        with patch("django.db.utils.ConnectionHandler.__getitem__") as gi:
            # Setting error as side effect array
            gi.side_effect = [OperationalError] * 5 + [True]

            # So it should raise operati... error 5 times
            call_command('wait_for_db')

            self.assertEqual(gi.call_count, 6)
