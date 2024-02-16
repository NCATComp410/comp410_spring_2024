"""Unit test file for Team TeamGuardiansOfPII"""
import unittest
from pii_scan import anonymize_text


class TestTeamGuardiansOfPII(unittest.TestCase):
    """Test the Team TeamGuardiansOfPII PII functions"""
    def test_anonymize_text(self):
        """Test the anonymize_text function"""
        self.assertEqual('I live in <LOCATION>',
                         anonymize_text('I live in New York', ['LOCATION']))

    def test_email_address(self):
        """Test email_address functionality"""

    def test_person(self):
        """Test person functionality"""

    def test_us_driver_license(self):
        """Test us_driver_license functionality"""

    def test_it_fiscal_code(self):
        """Test it_fiscal_code functionality"""

    def test_sg_nric_fin(self):
        """Test sg_nric_fin functionality"""
