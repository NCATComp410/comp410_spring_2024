"""Unit test file for Team TeamNull"""
import unittest
from pii_scan import anonymize_text


class TestTeamNull(unittest.TestCase):
    """Test the Team TeamNull PII functions"""
    def test_anonymize_text(self):
        """Test the anonymize_text function"""
        self.assertEqual('I live in <LOCATION>',
                         anonymize_text('I live in New York', ['LOCATION']))

    def test_us_ssn(self):
        """Test us_ssn functionality"""
