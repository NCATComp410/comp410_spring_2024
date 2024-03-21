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
        #Positive Testcase
        prefix = ['192', '143', '101']
        mid1 = ['168', '88', '72']
        mid2 = ['23', '54', '200']
        suffix = ['98', '1', '196']
        for p in prefix:
            for m1 in mid1:
                for m2 in mid2:
                    for s in suffix:
                        test_string = 'My IP Address is ' + p + '.' + m1 + '.' + m2 + '.' + s
                        expected = "My IP Address is <IP_ADDRESS>"
        actual = anonymize_text(test_string, ["IP_ADDRESS"])
        self.assertEqual(expected, actual)

        #Negative Testcase
        test_string = "My IP Address is 192.168.256.45"
        expected = "My IP Address is 192.168.256.45"
        actual = anonymize_text(test_string, ["IP_ADDRESS"])
        self.assertEqual(expected, actual)

    def test_medical_license(self):
        """Test medical_license functionality"""

    def test_us_passport(self):
        """Test us_passport functionality"""

    def test_it_vat_code(self):
        """Test it_vat_code functionality"""
