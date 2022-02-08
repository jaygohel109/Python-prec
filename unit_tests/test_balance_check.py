"""
Test file for balance_check.py
"""

import unittest
from balance_check import Account

class TestBalanceCheck(unittest.TestCase):

    def test_balance(self):
        bal1 = Account(5000)
        bal1.add_amount(1000)
        self.assertEqual(bal1.balance, 6000)
        bal1.subtract_amount(1000)
        self.assertEqual(bal1.balance, 5000)

        self.assertRaises(ValueError, bal1.add_amount, 0)
        self.assertRaises(ValueError, bal1.subtract_amount, -3000)
        self.assertRaises(ValueError, bal1.subtract_amount, 10000)

if __name__ == '__main__':
    unittest.main()