"""
Test file for add_int.py
"""

import unittest
from add_int import add_int

class TestAddInt(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_int(5,3), 8)
        self.assertEqual(add_int(-2,1), -1)
        self.assertEqual(add_int(-2,-3), -5)

    def test_value(self):
        self.assertRaises(ValueError, add_int, 'hh', 3)

if __name__ == '__main__':
    unittest.main()
