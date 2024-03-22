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
        # positive testcase
        test_string = "I am from 123 Blueberry Ave"
        expected = "I am from <LOCATION>"
        actual = anonymize_text(expected, ['LOCATION'])
        self.assertEqual(expected, actual)

        #positive testcase
        test_string = "I am from New York"
        expected = "I am from <LOCATION>"
        actual = anonymize_text(expected, ['LOCATION'])
        self.assertEqual(expected, actual)

        #positive testcase
        test_string = "I am from Montana"
        expected = "I am from <LOCATION>"
        actual = anonymize_text(expected, ['LOCATION'])
        self.assertEqual(expected, actual)

        #positive testcase
        test_string = "I am from Indiana"
        expected = "I am from <LOCATION>"
        actual = anonymize_text(expected, ['LOCATION'])
        self.assertEqual(expected, actual)

        #positive testcase
        test_string = "I am from 324 Maple Lane"
        expected = "I am from <LOCATION>"
        actual = anonymize_text(expected, ['LOCATION'])
        self.assertEqual(expected, actual)

        #negative testcase
        test_string = 'I live in the house'
        expected = 'I live in the house'
        actual = anonymize_text(test_string, ['LOCATION'])
        self.assertEqual(expected, actual)

        #negative testcase
        test_string = 'I do not live in the house'
        expected = 'I do not live in the house'
        actual = anonymize_text(test_string, ['LOCATION'])
        self.assertEqual(expected, actual)

    def test_us_bank_number(self):
        """Test us_bank_number functionality"""

    def test_es_nif(self):
        """Test es_nif functionality"""

    def test_it_identity_card(self):
        """Test it_identity_card functionality"""
