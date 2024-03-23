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
        #positive testcase
        month_prefix = ['12', '6', '7', '10']
        day_mid = ['9','20','23','12']
        year_suffix = ['2000', '1983', '2003', '1962']

        for month in month_prefix:
            for day in day_mid:
                for year in year_suffix:
                    test_string = f'My birthday is {month}/{day}/{year}'
                    expected = 'My birthday is <DATE_TIME>'
                    actual = anonymize_text(test_string, ['DATE_TIME'])
                    self.assertEqual(expected, actual)


        # negative testcase - will not be replaced
        test_string = 'My birthday is 12123000' # mmddyyyy is not a date recognizing pattern
        expected = 'My birthday is 12123000'
        actual = anonymize_text(test_string, ['DATE_TIME'])
        self.assertEqual(expected, actual)

        # negative testcase - will not be replaced
        test_string = 'My birthday is 00-00-0' # yy-mm-dd is not a date recognizing pattern
        expected = 'My birthday is 00-00-0'
        actual = anonymize_text(test_string, ['DATE_TIME'])
        self.assertEqual(expected, actual)

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
        