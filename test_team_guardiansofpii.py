"""Unit test file for Team TeamGuardiansOfPII"""
import unittest
from pii_scan import anonymize_text


class TestTeamGuardiansOfPII(unittest.TestCase):
    """Test the Team TeamGuardiansOfPII PII functions"""
    def test_anonymize_text(self):
        """Test the anonymize_text function"""
        self.assertEqual('I live in <LOCATION>',
                         anonymize_text('I live in New York', ['LOCATION']))

    def test_email_address(self):
        """Test email_address functionality"""

    def test_person(self):
        """Test person functionality"""
        # Positive Testcase
        test_string = "The PERSON is Jasmine Johnson"
        actual = anonymize_text(test_string, ['PERSON'])
        expected = "The PERSON is <PERSON>"
        self.assertEqual(expected, actual)

        # Negative Testcase - should not replace other testcases
        test_string = "The PERSON is modern family"
        expected = "The PERSON is modern family"
        actual = anonymize_text(test_string, ['PERSON'])
        self.assertEqual(expected, actual)

        # Negative Testcase - should not replace other testcases
        test_string = "The PERSON is here! puppy"
        expected = "The PERSON is here! puppy"
        actual = anonymize_text(test_string, ['PERSON'])
        self.assertEqual(expected, actual)

    def test_us_driver_license(self):
        """Test us_driver_license functionality"""

    def test_it_fiscal_code(self):
        """Test it_fiscal_code functionality"""

    def test_sg_nric_fin(self):
        """Test sg_nric_fin functionality"""
