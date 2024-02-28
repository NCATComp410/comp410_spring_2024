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
        # positive testcases
        prefix = ['123', '245', '532']
        mid = ['44', '55', '66']
        suffix = ['6789', '2233', '3344']

        # generate test cases using list comprehension
        test_cases = [f"My SSN is {p}-{m}-{s}" for p in prefix for m in mid for s in suffix]

        for test_string in test_cases:
            expected = 'My SSN is <US_SSN>'
            actual = anonymize_text(test_string, ['US_SSN'])
            self.assertEqual(expected, actual)

        # negative testcase - this will not be replaced
        test_string = 'My SSN is 123-45-6789'
        expected = 'My SSN is 123-45-6789'
        actual = anonymize_text(test_string, ['US_SSN'])
        self.assertEqual(expected, actual)

        # another negative testcase - this will not be replaced
        test_string = 'My SSN is 245-00-6789'
        expected = 'My SSN is 245-00-6789'
        actual = anonymize_text(test_string, ['US_SSN'])
        self.assertEqual(expected, actual)
