# 🚀 FlexCheck

>
> **FlexCheck** is a modular, extensible data validation library for Python. 
>    
> 🚀 Powered by [Tamia Team](https://tamia.team)
>

## <a name="table-of-content" />Table of Contents

[Synopsis](#synopsis)
[Features](#features)
[Installation](#installation)
[Getting Started](#getting-started)
   - [Loading Validators](#loading-validators)
   - [Writing Your Own Plugin](#writing-your-own-plugin)
   - [Localization Support](#localization-support)
[Contributing](#contributing)
[License](#license)

## <a name="synopsis" />Synopsis

> **FlexCheck** is a modular, extensible data validation library for Python. It allows you to validate various types of data (emails, URLs, dates, phone numbers, GPS coordinates, etc.) with flexible, plugin-based architecture. You can easily extend the library by adding new validators as separate modules.


## <a name="features"></a> Features

- **Modular design**: Validators are organized as plugins, allowing for easy addition and removal of validation types.
- **Extensible**: Create your own validators as plugins without modifying the core library.
- **Multi-language support**: FlexCheck can adapt validation messages and data formatting based on locale.
- **Pre-built validators**: Comes with out-of-the-box validators for common types like email, URL, dates, and more.
- **Lightweight**: Only load the validators you need.

## <a name="installation"></a> Installation

Install the core library using pip:

```bash
pip install flexcheck
```

You can also install additional plugins:

```bash
pip install flexcheck-email
pip install flexcheck-url
```

## <a name="getting-started"></a> Getting Started

### <a name="loading-validators"></a> Loading Validators

First, import and initialize the plugin manager to load available validators:

```python
from flexcheck.plugin_manager import PluginManager

# Initialize the manager and load plugins
manager = PluginManager()
manager.load_plugins()

# Example usage
email = "test@example.com"
print(manager.validate("email", email))  # True or False

url = "https://www.example.com"
print(manager.validate("url", url))  # True or False
```

### <a name="writing-your-own-plugin"></a> Writing Your Own Plugin

You can easily extend **FlexCheck** by writing your own plugin. For example, to add a new validator for postal codes, create a Python package and add an entry point in `pyproject.toml`:

```toml
[tool.poetry.plugins."flexcheck.plugins"]
postal_code = "postal_code_validator:PostalCodeValidator"
```

Then, define your validator class:

```python
class PostalCodeValidator:
    def validate(self, postal_code):
        return bool(re.match(r'^\d{5}$', postal_code))  # Example for French postal codes

    def localize(self, postal_code):
        return postal_code  # No localization needed for postal codes
```

### <a name="localization-support"></a> Localization Support

FlexCheck supports localization for dates, numbers, and other data types. Set the locale when initializing the plugin manager:

```python
manager = PluginManager(locale="fr_FR")
```

This will adjust date formats, error messages, and other locale-sensitive operations accordingly.

## <a name="contributing"></a> Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Add your changes.
4. Submit a pull request.

## <a name="license"></a> License

>
> [The MIT License](https://opensource.org/licenses/MIT)
>
> 🐿️ Copyright (c) 2023-2024 [Tamia SAS](https://tamia.team/), 🇫🇷 🇪🇺
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
>
