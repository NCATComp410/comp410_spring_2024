"""Unit test file for Team Team2"""
import unittest
from pii_scan import anonymize_text
from pii_scan import check_url



class TestTeam2(unittest.TestCase):
    """Test the Team Team2 PII functions"""
    def test_anonymize_text(self):
        """Test the anonymize_text function"""
        self.assertEqual('I live in <LOCATION>',
                         anonymize_text('I live in New York', ['LOCATION']))

    def test_crypto(self):
        """Test crypto functionality"""

    def test_nrp(self):
        """Test nrp functionality"""

    def test_url(self):
        """Testing URL"""
        #Positive test case, has PII in URL
        test_url = "http://www.test.com/pageName?user=RealName&Password=TheRealPassword123"
        expected = True
        actual = check_url(test_url)
        self.assertEqual(expected, actual)

        #Negative test case, doesn't have PII in URL
        negative_url = "http://www.testExample.com/page?param1=val1&param2=val2"
        expected = True
        actual = check_url(negative_url)
        self.assertNotEqual(expected, actual)

        #Test Case to make sure only parameters are included
        parameter_test_url = "http://www.secret.com"
        expected = False
        actual= check_url (parameter_test_url)
        self.assertEqual(expected, actual)




    def test_uk_nhs(self):
        """Test uk_nhs functionality"""

    def test_it_passport(self):
        """Test it_passport functionality"""
        # Positive test cas
        prefix = ['CC', 'XX']
        sufix = ['0000000', '1111111']
        for p in prefix:
            for s in sufix:
                test_string = 'My passaportoy is ' + p + s
                expected = "My passaportoy is <IT_PASSPORT>"
                actual = anonymize_text(test_string, ['IT_PASSPORT'])
                self.assertEqual(expected, actual)
    # Negative test case
                #tooLong
        expected = 'My passaportoy is CC00000001'
        actual = anonymize_text('My passaportoy is CC00000001', ['IT_PASSPORT'])
        self.assertEqual(expected, actual)
        #tooShort
        expected = 'My passaportoy is CC000000'
        actual = anonymize_text('My passaportoy is CC000000', ['IT_PASSPORT'])
        self.assertEqual(expected, actual)
