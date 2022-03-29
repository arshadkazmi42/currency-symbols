# -*- coding: utf-8 -*-

import unittest
from . import CurrencySymbols


class TestSum(unittest.TestCase):
    def test_currency_symbols(self) -> None:
        self.assertEqual(
            CurrencySymbols.get_symbol("USD"),
            "$",
            "Should return dollars symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("nzd"),
            "$",
            "Should return dollars symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("INR"),
            "₹",
            "Should return indian ruppees symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("CNY"),
            "¥",
            "Should return CNY symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("KZT"),
            "₸",
            "Should return KZT symbol"
        )
