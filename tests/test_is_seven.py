import unittest
from is_seven import is_seven

class TestIsSeven(unittest.TestCase):
    def test_is_seven(self):
        self.assertTrue(is_seven(7))
        self.assertTrue(is_seven(7.0))
        self.assertTrue(is_seven("7"))
        self.assertFalse(is_seven(8))
        self.assertFalse(is_seven(-7))
        self.assertFalse(is_seven(0))
        self.assertFalse(is_seven("6"))

if __name__ == '__main__':
    unittest.main() 