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
        #Negative Testcase
        test_string = "documento nacional de identidad B112345267A8A"
        expected = "documento nacional de identidad B112345267A8A"
        self.assertEqual(expected, anonymize_text(test_string, ['ES_NIF']))
        # positive testcase
        test_string = 'documento nacional de identidad 123452675A'
        expected = 'documento nacional de identidad <ES_NIF>'
        actual = anonymize_text(test_string, ['ES_NIF'])
        self.assertEqual(expected, actual)

        

    def test_it_identity_card(self):
        """Test it_identity_card functionality"""
