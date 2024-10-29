# is-seven

A simple yet powerful Python library that solves one of programming's most critical challenges: determining if a number is seven. 🔢 This library provides a robust, production-ready solution for the common programming task of seven detection and validation.

## Why is-seven?

Have you ever needed to check if a number is exactly seven? 🤔 Of course you have! While it may seem trivial to write `number == 7`, using a dedicated library brings several benefits: ✨

The is-seven library offers numerous compelling advantages that make it the ideal choice for your seven-detection needs:

- Professionally tested and maintained code with comprehensive unit tests ✅ - Every release undergoes rigorous testing across multiple Python versions and platforms to ensure consistent behavior and reliability. Our test suite covers edge cases and validates core functionality.

- Clear, semantic API that documents your intent and improves code readability 📚 - The simple, expressive API makes code self-documenting. When other developers see `is_seven()` they immediately understand the validation being performed.

- Handles edge cases like strings and floating point numbers 🎯 - Beyond basic integer comparison, is-seven properly handles floating point precision, string parsing, and gracefully manages invalid inputs. No need to write your own type checking and conversion logic.

- Zero dependencies - lightweight and reliable 🪶 - The library has absolutely no external dependencies, making it extremely lightweight and eliminating potential compatibility issues or security vulnerabilities from third-party packages.

- Documentation with clear examples 📚 - Comprehensive documentation with usage examples helps you get started quickly. Code snippets demonstrate common use cases and proper implementation.

- Cross-platform compatibility - works on Windows, Mac, Linux 💻 - Extensively tested across all major operating systems to guarantee consistent behavior regardless of platform. Deploy with confidence knowing it will work everywhere.

- Production-ready with semantic versioning 📦 - Following semantic versioning ensures API stability and makes dependency management predictable. Breaking changes are clearly communicated through version numbers.

- MIT licensed for maximum flexibility ⚖️ - The permissive MIT license allows usage in both commercial and open source projects with minimal restrictions. You can freely use, modify and distribute the code.

## Key Features

The library provides a focused set of powerful features:

- Simple, intuitive API that does one thing well 🎯 - A single function with clear purpose and behavior makes the library easy to learn and use effectively. No complicated configuration or setup required.

- Handles integers, floats and strings 🔢 - Flexible input handling accepts multiple numeric types including integers, floating point numbers, and their string representations. No need for manual type conversion.

- String parsing for numeric values ("7") 📝 - Intelligent string parsing converts numeric strings like "7" to their corresponding number for comparison. Handles leading/trailing whitespace and invalid formats gracefully.

- Direct equality comparison for numbers 🎯 - Performs exact numeric equality comparison accounting for type and value. No fuzzy matching or approximate comparisons that could produce incorrect results.

- Comprehensive test suite ensuring reliability ✅ - Extensive unit tests verify behavior across input types, edge cases, and error conditions. High test coverage gives confidence in library stability.

- Well-documented source code 📚 - Clean, documented implementation makes it easy to understand how the library works. Docstrings and comments explain the logic and design decisions.

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
print(is_seven(7.0))
print(is_seven("7"))

# Returns False
print(is_seven(8))
print(is_seven(-7))
print(is_seven("eight"))
print(is_seven("7.1"))
print(is_seven(None))
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

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=cwingho/is-seven&type=Timeline)](https://star-history.com/#cwingho/is-seven&Timeline)
