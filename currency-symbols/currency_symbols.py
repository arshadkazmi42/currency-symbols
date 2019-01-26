from constants import CURRENCY_SYMBOLS_MAP

class CurrencySymbols(object):

    # Checks if the input currency name exists in the map
    # If it exists, return the symbbol
    @staticmethod
    def get_symbol(currency):
        if not currency:
            return None

        if currency not in CURRENCY_SYMBOLS_MAP:
            return None
        
        return CURRENCY_SYMBOLS_MAP[currency]

