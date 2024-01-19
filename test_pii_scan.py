"""Tests for pii_scan.py"""
import unittest
from pii_scan import show_aggie_pride


class TestPII(unittest.TestCase):
    """Tests for pii_scan.py"""
    def test_show_aggie_pride(self):
        """Test show_aggie_pride"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")


if __name__ == '__main__':
    unittest.main()
