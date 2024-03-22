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
     test_string = "My email address is example@example.com"
    actual = anonymize_text(test_string, ['EMAIL'])
    expected = "My email address is <EMAIL>"
    self.assertEqual(expected, actual)

    # Negative Testcase - should not replace other text
    test_string = "This is not an email address"
    expected = "This is not an email address"
    actual = anonymize_text(test_string, ['EMAIL'])
    self.assertEqual(expected, actual)

    # Negative Testcase - should not replace other text
    test_string = "Email addresses can have special characters like this: email@example.co.uk"
    expected = "Email addresses can have special characters like this: <EMAIL>"
    actual = anonymize_text(test_string, ['EMAIL'])
    self.assertEqual(expected, actual)

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
        # positive test case 1
        #using the first public FIN of the first president of Singapore
        positive_test_string = 'My NRIC number is S0000001I'
        positive_expected_string = 'My NRIC number is <SG_NRIC_FIN>'
        positive_actual_string = anonymize_text(positive_test_string, ['SG_NRIC_FIN'])

        self.assertEqual(positive_expected_string, positive_actual_string)

        #positive test case 2
        #public FIN of the first chief justice of Singapore
        positive_test_string = 'S0000002G is my FIN'
        positive_expected_string = '<SG_NRIC_FIN> is my FIN'
        positive_actual_string = anonymize_text(positive_test_string, ['SG_NRIC_FIN'])

        self.assertEqual(positive_expected_string, positive_actual_string)

        #negative test case 1
        #replaced zeros with letter O's
        negative_test_string = 'My NRIC number is SOOOOOO1I'
        negative_expected_string = 'My NRIC number is SOOOOOO1I'
        negative_actual_string = anonymize_text(negative_test_string, ['SG_NRIC_FIN'])

        self.assertEqual(negative_expected_string, negative_actual_string)

        #negative test case 2
        #switched the checksum character and the last digit
        negative_test_string = 'S000000G2 is my FIN'
        negative_expected_string = 'S000000G2 is my FIN'
        negative_actual_string = anonymize_text(negative_test_string, ['SG_NRIC_FIN'])

        self.assertEqual(negative_expected_string, negative_actual_string)
