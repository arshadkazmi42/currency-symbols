# -*- coding: utf-8 -*- 

import unittest
from currency_symbols import CurrencySymbols


class TestSum(unittest.TestCase):

    def test_currency_symbols(self):
        self.assertEqual(CurrencySymbols.get_symbol('USD'), '$', "Should return dollars symbol")
        self.assertEqual(CurrencySymbols.get_symbol('INR'), '₹', "Should return indian ruppees symbol")
        self.assertEqual(CurrencySymbols.get_symbol('CNY'), '¥', "Should return CNY symbol")


if __name__ == '__main__':
    unittest.main()

