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
        """Test us_bank_number functionality"""

    def test_es_nif(self):
        """Test es_nif functionality"""

    def test_it_identity_card(self):
        """Test it_identity_card functionality"""
        # positive test cases
        prefixes = ['AB', 'CD', 'EF']
        digits = ['1234567', '7654321', '9876543']

        test_cases = [f"My ID is {prefix} {digit}" for prefix in prefixes for digit in digits]

        for test_string in test_cases:
            expected = 'My ID is <IT_IDENTITY_CARD>'
            actual = anonymize_text(test_string, ['IT_IDENTITY_CARD'])
            self.assertEqual(expected, actual)

        # negative test case - this will not be replaced
        test_string = 'My ID is ABC123456789' #Incorrect format
        expected = test_string
        actual = anonymize_text(test_string, ['IT_IDENTITY_CARD'])
        self.assertEqual(expected, actual)

        # another negative test case - this will not be replaced
        test_string = 'This is not an identity card number'
        expected = test_string
        actual = anonymize_text(test_string, ['IT_IDENTITY_CARD'])
        self.assertEqual(expected, actual)
        