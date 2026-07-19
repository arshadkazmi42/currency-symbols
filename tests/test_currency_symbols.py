# -*- coding: utf-8 -*-

import pytest

from currency_symbols import CurrencySymbols
from currency_symbols._constants import CURRENCY_SYMBOLS_MAP


# Spot checks for well-known and recently added currencies
KNOWN_SYMBOLS = {
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "INR": "₹",
    "JPY": "¥",
    "CNY": "¥",
    "CNH": "¥",
    "KZT": "₸",
    "CLF": "UF",
    "DEM": "DM",
    "FRF": "₣",
    "SLE": "Le",
    "VES": "Bs.",
    "XAG": "Ag",
    "XAU": "Au",
    "XCG": "Cg",
    "XDR": "SDR",
    "ZMK": "ZK",
    "ZMW": "ZK",
    "ZWD": "Z$",
    "ZWG": "ZiG",
    "ZWL": "Z$",
    "ZWN": "Z$",
    "ZWR": "Z$",
}


@pytest.mark.parametrize("code,symbol", sorted(KNOWN_SYMBOLS.items()))
def test_known_symbols(code, symbol):
    assert CurrencySymbols.get_symbol(code) == symbol


@pytest.mark.parametrize("code", sorted(CURRENCY_SYMBOLS_MAP))
def test_every_code_returns_a_symbol(code):
    symbol = CurrencySymbols.get_symbol(code)
    assert isinstance(symbol, str)
    assert symbol.strip()


@pytest.mark.parametrize("code", ["usd", "UsD", "eur", "nzd"])
def test_input_is_case_insensitive(code):
    assert CurrencySymbols.get_symbol(code) == \
        CurrencySymbols.get_symbol(code.upper())


@pytest.mark.parametrize("code", ["ZZZ", "", "US", "USDD", "123"])
def test_unknown_code_returns_none(code):
    assert CurrencySymbols.get_symbol(code) is None


def test_map_keys_are_uppercase_three_letter_codes():
    for code in CURRENCY_SYMBOLS_MAP:
        assert len(code) == 3, f"{code!r} is not 3 characters"
        assert code.isalpha(), f"{code!r} is not alphabetic"
        assert code.isupper(), f"{code!r} is not uppercase"


def test_map_is_sorted_alphabetically():
    codes = list(CURRENCY_SYMBOLS_MAP)
    assert codes == sorted(codes)


def test_map_symbols_are_non_empty_strings():
    for code, symbol in CURRENCY_SYMBOLS_MAP.items():
        assert isinstance(symbol, str), f"{code} symbol is not a string"
        assert symbol.strip(), f"{code} symbol is empty"
