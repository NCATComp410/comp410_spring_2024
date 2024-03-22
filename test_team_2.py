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
        # positive testcase
        nationality = ['American', 'Canadian', 'Russian']
        religion = ['Christianity', 'Islam', 'Hinduism']
        political_group = ['Liberal', 'Conservative', 'Socialist Parties']
        for n in nationality:
            for r in religion:
                for p in political_group:
                    test_string = "My NRP is " + n + "," + r + ", and" + p
                    expected = "My NRP is <NRP>"
                    actual = anonymize_text(test_string, ["NRP"])
                    self.assertEqual(expected, actual)

        # negative testcase - this will not be replaced
        test_string = "My nationality is American"
        expected = "My NRP is <NRP>"
        actual = anonymize_text(test_string, ["NRP"])
        self.assertEqual(expected, actual)

        # another negative testcase
        test_string = "My nationality is Russian"
        expected = "My NRP is <NRP>"
        actual = anonymize_text(test_string, ["NRP"])
        self.assertEqual(expected, actual)

    def test_url(self):
        """Test url functionality"""

    def test_uk_nhs(self):
        """Test uk_nhs functionality"""

    def test_it_passport(self):
        """Test it_passport functionality"""
