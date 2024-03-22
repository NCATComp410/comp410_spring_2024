"""Unit test file for Team Team2"""
import unittest
from pii_scan import anonymize_text


class TestTeam2(unittest.TestCase):
    """Test the Team Team2 PII functions"""
    def test_anonymize_text(self):
        """Test the anonymize_text function"""
        self.assertEqual('I live in <LOCATION>',
                         anonymize_text('I live in New York', ['LOCATION']))

    def test_crypto(self):
        """Test crypto functionality"""

    def test_nrp(self):
        """Test nrp functionality"""

    def test_url(self):
        """Test url functionality"""

    def test_uk_nhs(self):
        """Test uk_nhs functionality"""
        # positive testcases
        prefix = ['123', '245', '532']
        mid = ['333', '444', '555']
        suffix = ['6789', '2232', '4832']

        # Generates a testcase by utting the prefix, mid, and suffix together
        test_cases = [f"My NHS number is {p}-{m}-{s}" for p in prefix for m in mid for s in suffix]

        for test_string in test_cases:
            expected = 'My NHS number is <UK_NHS>'
            actual = anonymize_text(test_string, ['UK_NHS'])
            self.assertEqual(expected, actual)

        # negative testcase - this will not be replaced
        test_string = 'My NHS number is 123-456-7890'
        expected = 'My NHS number is 123-456-7890'
        actual = anonymize_text(test_string, ['UK_NHS'])
        self.assertEqual(expected, actual)

    def test_it_passport(self):
        """Test it_passport functionality"""
