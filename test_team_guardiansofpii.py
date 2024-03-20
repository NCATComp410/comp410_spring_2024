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

    def test_us_driver_license(self):
        """Test us_driver_license functionality"""

    def test_it_fiscal_code(self):
        """Test it_fiscal_code functionality"""

    def test_sg_nric_fin(self):
        """Test sg_nric_fin functionality"""
        # positive test case 1
        positive_test_string = 'My NRIC number is S0000001I' #using the first public FIN of the first president of Singapore
        positive_expected_string = 'My NRIC number is <SG_NRIC_FIN>'
        positive_actual_string = anonymize_text(positive_test_string, {'SG_NRIC_FIN'})

        self.assertEqual(positive_expected_string, positive_actual_string)

        #positive test case 2
        positive_test_string = 'S0000002G is my FIN' # public FIN of the first chief justice of Singapore
        positive_expected_string = '<SG_NRIC_FIN> is my FIN'
        positive_actual_string = anonymize_text(positive_test_string, {'SG_NRIC_FIN'})

        self.assertEqual(positive_expected_string, positive_actual_string)

        #negative test case 1
        negative_test_string = 'My NRIC number is SOOOOOO1I' #replaced zeros with letter O's 
        negative_expected_string = 'My NRIC number is SOOOOOO1I'
        negative_actual_string = anonymize_text(negative_test_string, {'SG_NRIC_FIN'})

        self.assertEqual(negative_expected_string, negative_actual_string)

        #negative test case 2
        negative_test_string = 'S000000G2 is my FIN' #switched the checksum character and the last digit
        negative_expected_string = 'S000000G2 is my FIN'
        negative_actual_string = anonymize_text(negative_test_string, {'SG_NRIC_FIN'})

        self.assertEqual(negative_expected_string, negative_actual_string)
