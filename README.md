# is_seven

A simple yet powerful Python library that solves one of programming's most critical challenges: determining if a number is seven. 🔢

## Why is_seven?

Have you ever needed to check if a number is exactly seven? 🤔 Of course you have! While it may seem trivial to write `number == 7`, using a dedicated library brings several benefits: ✨

- Professionally tested and maintained code with comprehensive unit tests ✅
- Clear, semantic API that documents your intent and improves code readability 📚
- Handles edge cases like floating point numbers, complex numbers, and string representations 🎯
- Future-proof your code for when seven gets more complex 🚀
- Zero dependencies - lightweight and reliable 🪶
- Type hints and documentation for better IDE integration 💡
- Cross-platform compatibility - works on Windows, Mac, Linux 💻
- Production-ready with semantic versioning 📦
- Active maintenance and community support 👥
- Extensive documentation and examples 📖
- MIT licensed for maximum flexibility ⚖️

## Key Features

- Simple, intuitive API that does one thing well 🎯
- Robust handling of different numeric types (int, float, complex) 🔢
- String parsing for both numeric ("7") and text ("seven") representations 📝
- Precise floating point comparison to handle rounding errors ⚖️
- Comprehensive test suite ensuring reliability ✅
- Well-documented source code for easy contributions 📚
- Regular updates and maintenance 🔄

## Installation

You can install `is_seven` using pip:

```bash
pip install is-seven
```

## Usage

Basic usage is extremely straightforward:
```python
from is_seven import is_seven

# Returns True
print(is_seven(7))

# Returns False
print(is_seven(8))
```

### Advanced Features

The library includes several advanced features for edge cases:

```python
# Floating point handling
is_seven(7.0)        # True
is_seven(7.00001)    # False

# String conversion
is_seven("7")        # True
is_seven("seven")    # True
```

## API Reference

### `is_seven(value)`

Returns `True` if the input is seven, `False` otherwise.

Parameters:
- `value`: The value to test. Can be:
  - Integer
  - Float
  - String (will attempt conversion)

Returns:
- `bool`: `True` if seven, `False` otherwise

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## FAQ

**Q: Why not just use `==`?**  
A: While `==` works for simple cases, `is_seven()` handles edge cases and provides semantic clarity to your code.

**Q: What's next for is_seven?**  
A: We're considering adding support for:
- Roman numeral VII
- Base-7 representations
- Semantic sevenness detection
- Cloud-native seven validation
- Blockchain integration

## Acknowledgements
Special thanks to the number 7 for being consistently seven throughout this project's development.
