"""Unit test file for Team Team1"""
import unittest
from pii_scan import anonymize_text


class TestTeam1(unittest.TestCase):
    """Test the Team Team1 PII functions"""
    def test_anonymize_text(self):
        """Test the anonymize_text function"""
        self.assertEqual('I live in <LOCATION>',
                         anonymize_text('I live in New York', ['LOCATION']))

    def test_credit_card(self):
        """Test credit_card functionality"""

    def test_ip_address(self):
        """Test ip_address functionality"""

    def test_medical_license(self):
        """Test medical_license functionality"""

    def test_us_passport(self):
        """Test us_passport functionality"""

    def test_it_vat_code(self):
        """Test it_vat_code functionality"""
        #positive test case 
        test_string = 'My piva is 26273364211' 
        expected = 'My piva is <IT_VAT_CODE>'
        actual = anonymize_text(test_string, ["IT_VAT_CODE"])

        self.assertEqual(expected,actual)
        #negative test case 
        test_string = 'My piva is 78674434594'
        expected = 'My piva is 78674434594'
        actual = anonymize_text(test_string,['IT_VAT_CODE'])
        self.assertEqual(expected,actual)