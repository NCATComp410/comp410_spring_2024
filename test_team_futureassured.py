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
        #Positive Test Case
                   
        instance = ['GB33BUKB20201555555555', 'MT31MALT01100000000000000000123', 'DO22ACAU00000000000123456789']
        for p in instance:
            test_string = 'My IBAN code is ' + p
            excpected = "My IBAN code is <IBAN_CODE>"
            actual = anonymize_text(test_string, ['IBAN_CODE'])
            self.assertEqual(excpected, actual)

        #Negative Test Case - will not be replaced
        test_string = "My IBAN code is GB14WXYZ220562325648978"
        excpected = "My IBAN code is GB14WXYZ220562325648978"
        actual = anonymize_text(test_string, ['IBAN_CODE'])
        self.assertEqual(excpected, actual)


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
