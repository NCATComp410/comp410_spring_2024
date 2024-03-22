"""Unit test file for Team Team2"""
import unittest
import re
from pii_scan import anonymize_text
from urllib.parse import urlparse, parse_qs

def url(URL):
    privateInfo = r'password|passwd|pwd|secret|secret|token|api_key'

    qureyUrl = urlparse(URL)
    urlParameters = parse_qs(qureyUrl.query)

    for i in urlParameters:
        if any(re.search(privateInfo, value, re.IGNORECASE) for value in urlParameters[i]):
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
        #Positive test case, has PII in URL
        testURL = "http://www.test.com/pageName?user=RealName&Password=TheRealPassword123"
        expected = True
        actual = url(testURL)
        self.assertEqual(expected, actual)

        #Negative test case, doesn't have PII in URL
        negativeTestURL = "http://www.testExample.com/page?param1=val1&param2=val2"
        expected = True
        actual = url(negativeTestURL)
        self.assertNotEqual(expected, actual)


    def test_uk_nhs(self):
        """Test uk_nhs functionality"""

    def test_it_passport(self):
        """Test it_passport functionality"""
