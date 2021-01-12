from .constants import CURRENCY_SYMBOLS_MAP

class CurrencySymbols(object):

    # Checks if the input currency name exists in the map
    # If it exists, return the symbbol
    @staticmethod
    def get_symbol(currency):
        if not currency:
            return None
        else:
            return CURRENCY_SYMBOLS_MAP.get(currency)
