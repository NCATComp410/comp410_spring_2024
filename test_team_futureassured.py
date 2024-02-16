"""Unit test file for Team TeamFutureAssured"""
import unittest
from pii_scan import anonymize_text


class TestTeamFutureAssured(unittest.TestCase):
    """Test the Team TeamFutureAssured PII functions"""
    def test_anonymize_text(self):
        """Test the anonymize_text function"""
        self.assertEqual('I live in <LOCATION>',
                         anonymize_text('I live in New York', ['LOCATION']))

    def test_iban_code(self):
        """Test iban_code functionality"""

    def test_phone_number(self):
        """Test phone_number functionality"""

    def test_us_itin(self):
        """Test us_itin functionality"""

    def test_it_driver_license(self):
        """Test it_driver_license functionality"""

    def test_au_abn(self):
        """Test au_abn functionality"""

    def test_au_medicare(self):
        """Test au_medicare functionality"""
