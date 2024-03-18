"""Basic tests for the pii_scan module"""
import unittest
from pii_scan import show_aggie_pride,  anonymize_text


class TestPII(unittest.TestCase):
    """Test the pii_scan module"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_anonymize_location(self):
        """Test to make sure location is anonymized"""

        # The first positive test case expects the Presido library to anonymize the location
        # with "New York" replaced with "<LOCATION>"
        self.assertEqual('I live in <LOCATION>',
                         anonymize_text('I live in New York', ['LOCATION']))

        # This negative test case expects the Presido library to not anonymize the location
        # so anonymize_text should return the original text without any replacements
        self.assertEqual('I live in a house',
                         anonymize_text('I live in a house', ['LOCATION']))

    def test_language_specific(self):
        """Test to make sure languange specific entities are loaded correctly"""
        entities = ('ES_NIF, IT_DRIVER_LICENSE, IT_VAT_CODE, IT_FISCAL_CODE, IT_IDENTITY_CARD, '
                    'IT_PASSPORT, PL_PESEL, SG_NRIC_FIN')
        for e in entities.split(', '):
            # make sure an exception is not raised
            anonymize_text('my name is John Doe', [e])


if __name__ == '__main__':
    unittest.main()
