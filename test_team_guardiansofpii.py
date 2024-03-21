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
        #This is Positive Test Case
        #Define lists of different parts of the fiscal code.
        surname = ["MRT","MLL","RSS"]
        name = ["MTT","SNT","GPP"]
        birthdate_gender = ['25D09','82P65','85A15']
        town = ["F205","Z404","H517"]
        check_character = ["Z","U","J"]
#The lists are iterated through all combinations of the fiscal code.
        for s in surname:
            for n in name:
                for bd in birthdate_gender:
                    for t in town:
                        for c in check_character:
                            #Construc a string for testing.

                            text_string  = 'This is a Fiscal Code:' + s + n + bd + t + c
                            #Define expected output and test the anontmizer
                            expected = 'This is a Fiscal Code:<IT_FISCAL_CODE>'
                            output = anonymize_text(text_string, ['IT_FISCAL_CODE'])
                            #Check the anonymizer's results with the expected output.
                            self.assertEqual(expected, output)

        # Negative Test Case: Input does not contain any fiscal code.
        # Using a random string that will not resemble an IT_FISCAL_CODE pattern.
        text_string  = 'This is a random text without fiscal code.'
        expected = 'This is a random text without fiscal code.'
        output = anonymize_text(text_string, ['IT_FISCAL_CODE'])
        self.assertEqual(expected, output)

    def test_sg_nric_fin(self):
        """Test sg_nric_fin functionality"""
