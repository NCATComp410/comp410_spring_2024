import unittest
from pii_scan import show_aggie_pride


class TestPII(unittest.TestCase):
    def test_show_aggie_pride(self):
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")


if __name__ == '__main__':
    unittest.main()
