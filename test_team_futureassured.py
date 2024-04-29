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
        instance = ['GB33BUKB20201555555555', 'MT31MALT01100000000000000000123',
                    'DO22ACAU00000000000123456789']
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
        # Positive test case
        post = ['0175','0180', '0101']
        for p in post:
            test_string = 'My phone number is 800-555‑' + p
            expected = 'My phone number is <PHONE_NUMBER>'
            actual = anonymize_text(test_string, ['PHONE_NUMBER'])
            self.assertEqual(expected, actual)

        # Negative case - this will not be replaced, regional code can not be outside 0-3
        test_string = 'My phone number is 4-800-555‑0175'
        expected = 'My phone number is 4-800-555‑0175'
        actual = anonymize_text(test_string, ['PHONE_NUMBER'])
        self.assertEqual(expected, actual)


    def test_us_itin(self):
        """Test us_itin functionality"""
        # positive test case
        start = ['912', '958', '999']
        middle = ['51', '85', '91']
        end = ['1234', '5484', '6543']

        test_cases = [f"My ITIN is {s}-{m}-{e}" for s in start for m in middle for e in end]

        for test_string in test_cases:
            expected = "My ITIN is <US_ITIN>"
            actual = anonymize_text(test_string, ['US_ITIN'])
            self.assertEqual(expected, actual)

        # negative test case - will not be replaced
        test_string = "My ITIN is 912-42-1234"
        expected = "My ITIN is 912-42-1234"
        actual = anonymize_text(test_string, ['US_ITIN'])
        self.assertEqual(expected, actual)

    def test_it_driver_license(self):
        """Test it_driver_license functionality"""
        # Positive test case
        test_string = 'My driver license code is RR4912349J'
        expected = 'My driver license code is <IT_DRIVER_LICENSE>'
        actual = anonymize_text(test_string, ['IT_DRIVER_LICENSE'])
        self.assertEqual(expected, actual)

        # Negative Test Case - will not be replaced
        test_string = 'My driver license code is R1053121X'
        expected = 'My driver license code is R1053121X'
        actual = anonymize_text(test_string, ['IT_DRIVER_LICENSE'])
        self.assertEqual(expected, actual)

    def test_au_abn(self):
        """Test case for AU_ABN"""     
        #positive testcase
        test_string = "My ABN is 51824753556"
        expected = "My ABN is <AU_ABN>"
        actual = anonymize_text(test_string, ["AU_ABN"])
        self.assertEqual(expected,actual)

        #negative testcase
        test_string = "My ABN is 1234334345678"
        expected = "My ABN is <AU_ABN>"
        actual = anonymize_text(test_string, ["AU_ABN"])
        self.assertNotEqual(expected,actual)




    def test_au_medicare(self):
        """Test au_medicare functionality"""
        #format
        #First digit and must be in the range 2–6
        #8th digit is check sum
        #Last digit (issue number) and can't be 0
        #positive test case example
        test_string  = 'My AU Medicare Number is 2835467857'
        expected = 'My AU Medicare Number is <AU_MEDICARE>'
        actual = anonymize_text(test_string, ['AU_MEDICARE'])
        self.assertEqual(expected, actual)

        #negative test case example
        #check sum digit is not calculated correctly in this example
        test_string  = 'My AU Medicare Number is 2835467897'
        expected = 'My AU Medicare Number is 2835467897'
        actual = anonymize_text(test_string, ['AU_MEDICARE'])
        self.assertEqual(expected, actual)
