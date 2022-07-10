# currency-symbols :money_with_wings:

[![Build](https://github.com/arshadkazmi42/currency-symbols/actions/workflows/pytest.yml/badge.svg)](https://github.com/arshadkazmi42/currency-symbols/actions/workflows/pytest.yml)
[![Downloads](https://img.shields.io/pypi/dm/currency-symbols.svg)](https://pypi.org/project/currency-symbols/)
[![Repo Size](https://img.shields.io/github/languages/code-size/arshadkazmi42/currency-symbols.svg)](https://github.com/arshadkazmi42/currency-symbols)
[![LICENSE](https://img.shields.io/pypi/l/currency-symbols.svg)](https://pypi.org/project/currency-symbols/)
[![Version](https://img.shields.io/pypi/v/currency-symbols.svg)](https://pypi.org/project/currency-symbols/)
[![Last Commit](https://img.shields.io/github/last-commit/arshadkazmi42/currency-symbols.svg)](https://github.com/arshadkazmi42/currency-symbols)

Get currency symbol by currency code `eg: USD -> $`

## References
[ISO 4217 - Currency Codes](https://www.iso.org/iso-4217-currency-codes.html)

## Installation

```
$ pip3 install currency-symbols
```

## Usage

```python
from currency_symbols import CurrencySymbols

dollarSymbol = CurrencySymbols.get_symbol('USD')
print(dollarSymbol)

# Output:
# $

euroSymbol = CurrencySymbols.get_symbol('EUR')
print(euroSymbol)

# Output:
# €

britishPoundSymbol = CurrencySymbols.get_symbol('GBP')
print(britishPoundSymbol)

# Output:
# £

bitcoinSymbol = CurrencySymbols.get_symbol('BTC')
print(bitcoinSymbol)

# Output:
# ฿
```

## Contributing

Interested in contributing to this project?
You can log any issues or suggestion related to this library [here](https://github.com/arshadkazmi42/currency-symbols/issues/new)

Read our contributing [guide](https://github.com/arshadkazmi42/currency-symbols/blob/master/CONTRIBUTING.md) on getting started with contributing to the codebase


## Credits

Inspired by work of [@bengourley](https://github.com/bengourley) on [currency-symbol-map](https://github.com/bengourley/currency-symbol-map#readme)
