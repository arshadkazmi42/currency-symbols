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
