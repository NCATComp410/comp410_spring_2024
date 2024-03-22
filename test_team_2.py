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

    def test_nrp(self):
        """Test nrp functionality"""

    def test_url(self):
        """Test url functionality"""

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
