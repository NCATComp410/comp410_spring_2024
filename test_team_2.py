"""Unit test file for Team Team2"""
import unittest
from pii_scan import anonymize_text


class TestTeam2(unittest.TestCase):
    """Test the Team Team2 PII functions"""
    def test_anonymize_text(self):
        """Test the anonymize_text function"""
        self.assertEqual('I live in <LOCATION>',
                         anonymize_text('I live in New York', ['LOCATION']))

    def test_crypto(self):
        """Test crypto functionality"""
        #positive test case, should replace the address with <CRPYTO> 
        prefix = ['3', '1']
        end = ['QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC', 'C7zdTfnkzmr13HfA2vNm5SJYRK6nEKyq8']
        #use for loop to create addresses that won't flag detection systems
        for index, value in enumerate(prefix):
            expected = 'My bitcoin wallet address is <CRYPTO>'
            actual = 'My bitcoin wallet address is ' + value + end[index]
            self.assertEqual(anonymize_text(actual, ['CRYPTO']), expected)
            #negative test case 1: Will not be replaced due to invalid format
            invalid = 'My bitcoin wallet address is 24qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq'
            self.assertEqual(anonymize_text(invalid, ['CRYPTO']), invalid)


    def test_nrp(self):
        """Test nrp functionality"""

    def test_url(self):
        """Test url functionality"""

    def test_uk_nhs(self):
        """Test uk_nhs functionality"""

    def test_it_passport(self):
        """Test it_passport functionality"""