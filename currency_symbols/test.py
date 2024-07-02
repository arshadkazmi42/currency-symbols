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

    def test_currency_code(self) -> None:
        self.assertEqual(
            CurrencySymbols.get_currency_code("₹"),
            ['INR'],
            "Return a list containing INR"
        )

        self.assertEqual(
            CurrencySymbols.get_currency_code("$"),
            ['ARS', 'AUD', 'BBD', 'BMD', 'BND', 'BSD', 'CAD', 'CLP', 'COP', 'CUC', 'CVE', 'FJD', 'GYD', 'HKD', 'KYD',
             'LRD', 'MXN', 'NAD', 'NZD', 'SBD', 'SGD', 'SRD', 'SVC', 'TVD', 'USD', 'XCD'],
            "Return list containing ARS, AUD, BBD, BMD, BND, BSD, CAD, CLP, COP, CUC, CVE, FJD, GYD, HKD, KYD, LRD, MXN, NAD, NZD, SBD, SGD, SRD, SVC, TVD, USD, XCD"
        )

        self.assertEqual(
            CurrencySymbols.get_currency_code("£"),
            ['EGP', 'FKP', 'GBP', 'GGP', 'GIP', 'IMP', 'JEP', 'LBP', 'SHP', 'SSP', 'SYP'],
            "Return a list containing EGP, FKP, GBP, GGP, GIP, IMP, JEP, LBP, SHP, SSP, SYP"
        )

        self.assertEqual(
            CurrencySymbols.get_currency_code("¥"),
            ['CNY', 'JPY'],
            "Return a list containing CNY, JPY"
        )
