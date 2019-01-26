# currency-symbols :money_with_wings:

Get currency symbol by currency code `eg: USD -> $`

## Installation

```
$ pip3 install currency-symbols
```

## Usage

```python
from currency_symbols import CurrencySymbols

dollarSymbol = CurrencySymbols.get_symbol('USD');
print(dollarSymbol)

# Output:
# $
```

## Contributing

Interested in contributing to this project?
You can log any issues or suggestion related to this library [here](https://github.com/arshadkazmi42/currency-symbols/issues/new)

Read our contributing [guide](https://github.com/arshadkazmi42/currency-symbols/blob/master/CONTRIBUTING.md) on getting started with contributing to the codebase

## Credits
Inspired by work of [@bengourley](https://github.com/bengourley) of [currency-symbol-map](https://github.com/bengourley/currency-symbol-map#readme)