# currency-symbols :money_with_wings:

[![CI](https://github.com/arshadkazmi42/currency-symbols/actions/workflows/pytest.yml/badge.svg)](https://github.com/arshadkazmi42/currency-symbols/actions/workflows/pytest.yml)
[![Version](https://img.shields.io/pypi/v/currency-symbols.svg)](https://pypi.org/project/currency-symbols/)
[![Downloads](https://img.shields.io/pypi/dm/currency-symbols.svg)](https://pypi.org/project/currency-symbols/)
[![LICENSE](https://img.shields.io/pypi/l/currency-symbols.svg)](https://github.com/arshadkazmi42/currency-symbols/blob/master/LICENSE)

Get the currency symbol for an [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) currency code — `USD → $`, `EUR → €`, `INR → ₹`.

- Covers all active ISO 4217 codes, plus common historical, crypto and commodity codes
- Zero dependencies
- Fully typed ([PEP 561](https://peps.python.org/pep-0561/), ships `py.typed`)
- Python 3.9+

## Installation

```console
pip install currency-symbols
```

## Usage

```python
from currency_symbols import CurrencySymbols

CurrencySymbols.get_symbol("USD")
# '$'

CurrencySymbols.get_symbol("EUR")
# '€'

CurrencySymbols.get_symbol("gbp")
# '£' — codes are case-insensitive

CurrencySymbols.get_symbol("XYZ")
# None — unknown codes return None
```

## Changelog

All notable changes are documented in the [CHANGELOG](https://github.com/arshadkazmi42/currency-symbols/blob/master/CHANGELOG.md).

## Contributing

Interested in contributing to this project?
You can log any issues or suggestions related to this library [here](https://github.com/arshadkazmi42/currency-symbols/issues/new)

Read our contributing [guide](https://github.com/arshadkazmi42/currency-symbols/blob/master/CONTRIBUTING.md) on getting started with contributing to the codebase

## Credits

Inspired by work of [@bengourley](https://github.com/bengourley) on [currency-symbol-map](https://github.com/bengourley/currency-symbol-map#readme)

## License

[MIT](https://github.com/arshadkazmi42/currency-symbols/blob/master/LICENSE)
