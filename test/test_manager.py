#
# flexcheck/test_manager.py
#
# Part of the FlexCheck project.
# License: MIT
# © 2023-2024 🐿️ [Tamia Team](https://tamia.team)
#
# This module handles the dynamic loading of plugins for data validation.
# It allows FlexCheck to load, validate, and localize data using various plugins.
#
# This file contains unit tests for the PluginManager class using pytest.

import pytest
from unittest.mock import Mock, patch
from flexcheck import PluginManager

def test_load_plugins():
    """Test that the load_plugins method correctly loads plugins."""
    manager = PluginManager()

    # Mocking pkg_resources.iter_entry_points to simulate loaded plugins
    mock_entry_point = Mock()
    mock_entry_point.name = 'test_plugin'
    mock_entry_point.load.return_value = Mock(validate=Mock(), localize=Mock())

    with patch('pkg_resources.iter_entry_points', return_value=[mock_entry_point]):
        manager.load_plugins()

    assert 'test_plugin' in manager.plugins
    assert callable(manager.plugins['test_plugin'].validate)
    assert callable(manager.plugins['test_plugin'].localize)

def test_validate_success():
    """Test that the validate method calls the correct plugin and returns True."""
    mock_validator = Mock(validate=Mock(return_value=True))
    manager = PluginManager()
    manager.plugins['test_plugin'] = mock_validator

    result = manager.validate('test_plugin', 'test_data')

    assert result is True
    mock_validator.validate.assert_called_once_with('test_data')

def test_validate_failure():
    """Test that the validate method raises an error for unsupported data types."""
    manager = PluginManager()

    with pytest.raises(ValueError, match="Type of validation 'invalid_plugin' not supported."):
        manager.validate('invalid_plugin', 'test_data')

def test_localize_success():
    """Test that the localize method calls the correct plugin and returns localized data."""
    mock_validator = Mock(localize=Mock(return_value='localized_data'))
    manager = PluginManager()
    manager.plugins['test_plugin'] = mock_validator

    result = manager.localize('test_plugin', 'test_data')

    assert result == 'localized_data'
    mock_validator.localize.assert_called_once_with('test_data')

def test_localize_failure():
    """Test that the localize method raises an error for unsupported data types."""
    manager = PluginManager()

    with pytest.raises(ValueError, match="Type of validation 'invalid_plugin' not supported."):
        manager.localize('invalid_plugin', 'test_data')
