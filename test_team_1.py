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
        
        # positive test case
        prefix = ['4111', '5105', '6011']
        middle1 = ['1111', '1051', '0000']
        middle2 = ['1111', '0510', '0000']
        suffix = ['1111', '5100', '0004']
        
        for p in prefix:
            for m1 in middle1:
                for m2 in middle2:
                    for s in suffix:

                        test_string = 'My credit card is ' + p + '-' + m1 + '-' + m2 + '-' + s 
                        expected = 'My credit card is <CREDIT_CARD>'
        actual = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected, actual)

            # negative test case
        test_string = 'My credit card is 4000-0000-0000-0001'
        expected = 'My credit card is 4000-0000-0000-0001'
        actual = anonymize_text(test_string, ['CREDIT_CARD'])
        self.assertEqual(expected, actual)


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
        #positive testcase
        test_string = "My US Passport ID is 123456789"
        expected = "My US Passport ID is <US_PASSPORT>"
        actual = anonymize_text(test_string, ["US_PASSPORT"])
        self.assertEqual(expected,actual)

        #negative testcase
        test_string = "My US Passport ID is 1234334345678"
        expected = "My US Passport ID is <US_PASSPORT>"
        actual = anonymize_text(test_string, ["US_PASSPORT"])
        self.assertNotEqual(expected,actual)

    def test_it_vat_code(self):
        """Test it_vat_code functionality"""

        #positive test case
        prefix =['26273', '01333']
        suffix =['364211','550323']
        for i in prefix:
            for j in suffix:
                test_string = 'My piva is ' +i +j
        expected = 'My piva is <IT_VAT_CODE>'
        actual = anonymize_text(test_string, ["IT_VAT_CODE"])
        self.assertEqual(expected,actual)
        #negative test case
        test_string = 'My piva is 78674434594'
        expected = 'My piva is 78674434594'
        actual = anonymize_text(test_string,['IT_VAT_CODE'])
        self.assertEqual(expected,actual)
        