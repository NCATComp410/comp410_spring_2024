"""Unit test file for Team Team2"""
import unittest
import re
from urllib.parse import urlparse, parse_qs
from pii_scan import anonymize_text

def check_url(url):
    """Method for the URL"""
    #Creating function to determine if pii is in URL
    private_info = r'password|passwd|pwd|secret|secret|token|api_key'

    qurey_url = urlparse(url)
    url_parameters = parse_qs(qurey_url.query)

    for _, values in url_parameters.items():
        if any(re.search(private_info, value, re.IGNORECASE) for value in values):
            return True
    return False



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


    def test_uk_nhs(self):
        """Test uk_nhs functionality"""

    def test_it_passport(self):
        """Test it_passport functionality"""
