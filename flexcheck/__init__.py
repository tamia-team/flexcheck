#
# flexcheck/__init__.py
#
# Part of the FlexCheck project.
# License: MIT
# © 2023-2024 🐿️ [Tamia Team](https://tamia.team)
#
# This module handles the dynamic loading of plugins for data validation.
# It allows FlexCheck to load, validate, and localize data using various plugins.
#

import pkg_resources

class PluginManager:
    """Plugin Manager for dynamically loading and managing validation plugins."""

    def __init__(self):
        self.plugins = {}

    def load_plugins(self):
        """Load all available plugins via entry points.

        Iterates through all defined entry points under 'data_validators.plugins' and loads
        each plugin dynamically, adding it to the plugins dictionary.
        """
        for entry_point in pkg_resources.iter_entry_points('data_validators.plugins'):
            plugin_class = entry_point.load()
            self.plugins[entry_point.name] = plugin_class()

    def validate(self, data_type, data):
        """Validate data using the appropriate plugin.

        Args:
            data_type (str): The type of data to validate (e.g., 'email', 'url').
            data (any): The actual data to validate.

        Returns:
            bool: True if validation succeeds, False otherwise.

        Raises:
            ValueError: If the specified data type is not supported by any plugin.
        """
        if data_type in self.plugins:
            validator = self.plugins[data_type]
            return validator.validate(data)
        else:
            raise ValueError(f"Type of validation '{data_type}' not supported.")

    def localize(self, data_type, data):
        """Localize the data using the appropriate plugin, if localization is needed.

        Args:
            data_type (str): The type of data to localize (e.g., 'date', 'number').
            data (any): The actual data to localize.

        Returns:
            any: The localized version of the data, or the original data if no localization is needed.

        Raises:
            ValueError: If the specified data type is not supported by any plugin.
        """
        if data_type in self.plugins:
            validator = self.plugins[data_type]
            return validator.localize(data)
        else:
            raise ValueError(f"Type of validation '{data_type}' not supported.")
