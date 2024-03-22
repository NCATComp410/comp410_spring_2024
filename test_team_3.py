"""Unit test file for Team Team3"""
import unittest
from pii_scan import anonymize_text


class TestTeam3(unittest.TestCase):
    """Test the Team Team3 PII functions"""
    def test_anonymize_text(self):
        """Test the anonymize_text function"""
        self.assertEqual('I live in <LOCATION>',
                         anonymize_text('I live in New York', ['LOCATION']))

    def test_date_time(self):
        """Test date_time functionality"""

    def test_location(self):
        """Test location functionality"""

    def test_us_bank_number(self):
        """Test US bank number detection and anonymization"""
        # positive test cases
        bank_numbers = [
            '12345678',
            '987654321',
            '0123456789',
            '1234567890123456'
        ]

        test_cases = [f"My bank account number is {bank_number}" for bank_number in bank_numbers]

        for test_string in test_cases:
            expected = 'My bank account number is <US_BANK_NUMBER>'
            actual = anonymize_text(test_string, ['US_BANK_NUMBER'])
            self.assertEqual(expected, actual)

        # negative test case - this will not be replaced
        test_string = 'My bank account number is ABC123456789' # Incorrect format
        expected = test_string
        actual = anonymize_text(test_string, ['US_BANK_NUMBER'])
        self.assertEqual(expected, actual)

        # another negative test case - this will not be replaced
        test_string = 'This is not a bank account number'
        expected = test_string
        actual = anonymize_text(test_string, ['US_BANK_NUMBER'])
        self.assertEqual(expected, actual)

    def test_es_nif(self):
        """Test es_nif functionality"""

    def test_it_identity_card(self):
        """Test it_identity_card functionality"""
