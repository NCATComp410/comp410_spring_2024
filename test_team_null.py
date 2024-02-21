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
        # Test a valid SSN
        prefix = ['123']
        mid = ['44']
        suffix = ['6789']
        ssn = prefix[0] + '-' + mid[0] + '-' + suffix[0]
        self.assertEqual('SSN <US_SSN>',
                         anonymize_text('SSN ' + ssn, ['US_SSN']))
        
        # test an invalid ssn
        prefix = ['123']
        mid = ['00']
        suffix = ['6789']
        ssn = prefix[0] + '-' + mid[0] + '-' + suffix[0]
        self.assertEqual('SSN 123-00-6789',
                         anonymize_text('SSN ' + ssn, ['US_SSN']))
