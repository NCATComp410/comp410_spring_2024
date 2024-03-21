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
        # positive test case
        start = ['912', '958', '999']
        middle = ['51', '85', '91']
        end = ['1234', '5484', '6543']

        test_cases = [f"My ITIN is {s}-{m}-{e}" for s in start for m in middle for e in end]

        for test_string in test_cases:
            expected = "My ITIN is <US_ITIN>"
            actual = anonymize_text(test_string, ['US_ITIN'])
            self.assertEqual(expected, actual)

        # negative test case - will not be replaced
        test_string = "My ITIN is 912-42-1234"
        expected = "My ITIN is 912-42-1234"
        actual = anonymize_text(test_string, ['US_ITIN'])
        self.assertEqual(expected, actual)

    def test_it_driver_license(self):
        """Test it_driver_license functionality"""

    def test_au_abn(self):
        """Test au_abn functionality"""

    def test_au_medicare(self):
        """Test au_medicare functionality"""
