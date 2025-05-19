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
        self.assertEqual(
            CurrencySymbols.get_symbol("CLF"),
            "UF",
            "Should return CLF symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("CNH"),
            "¥",
            "Should return CNH symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("DEM"),
            "DM",
            "Should return DEM symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("FRF"),
            "₣",
            "Should return FRF symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("SLE"),
            "Le",
            "Should return SLE symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("VES"),
            "Bs.",
            "Should return VES symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("XAG"),
            "Ag",
            "Should return XAG symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("XAU"),
            "Au",
            "Should return XAU symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("XCG"),
            "Cg",
            "Should return XCG symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("XDR"),
            "SDR",
            "Should return XDR symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("ZMK"),
            "ZK",
            "Should return ZMK symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("ZMW"),
            "ZK",
            "Should return ZMW symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("ZWD"),
            "Z$",
            "Should return ZWD symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("ZWG"),
            "ZiG",
            "Should return ZWG symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("ZWL"),
            "Z$",
            "Should return ZWL symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("ZWN"),
            "Z$",
            "Should return ZWN symbol"
        )
        self.assertEqual(
            CurrencySymbols.get_symbol("ZWR"),
            "Z$",
            "Should return ZWR symbol"
        )