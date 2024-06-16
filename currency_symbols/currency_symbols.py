# -*- coding: utf-8 -*-

from typing import Optional
from ._constants import CURRENCY_SYMBOLS_MAP


class CurrencySymbols:
    @staticmethod
    def get_symbol(currency: str) -> Optional[str]:
        """Converts provided currency into currency symbol.

        Parameters
        ----------
        currency : str
            ISO 4217 - Currency Codes

        Returns
        -------
        Optional[str]
            Currency symbol, None if not exists.
        """

        return CURRENCY_SYMBOLS_MAP.get(currency.upper(), None)

    @staticmethod
    def get_currency_code(currency_symbol: str) -> Optional[str]:
        """Converts provided currency symbol into currency code.

        Parameters
        ----------
        Currency symbol : str
            ISO 4217 - Currency Codes

        Returns
        -------
        Optional[str]
            Currency, None if not exists.
        """
        for currency_code, symbol in CURRENCY_SYMBOLS_MAP.items():
            if symbol == currency_symbol:
                return currency_code
            else:
                return None
