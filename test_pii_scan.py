"""Basic tests for the pii_scan module"""
import unittest
from pii_scan import show_aggie_pride,  anonymize_text


class TestPII(unittest.TestCase):
    """Test the pii_scan module"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_anonymize_location(self):
        """Test to make sure location is anonymized"""
        # Test to make sure text is anonymized
        self.assertEqual('I live in <LOCATION>',
                         anonymize_text('I live in New York', ['LOCATION']))
        # Test to make sure text is not anonymized
        self.assertEqual('I live in a house',
                         anonymize_text('I live in a house', ['LOCATION']))


if __name__ == '__main__':
    unittest.main()
