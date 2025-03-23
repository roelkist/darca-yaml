# tests/conftest.py

import pytest


@pytest.fixture(scope="session")
def valid_yaml_data():
    return {
        "name": "darca-yaml",
        "version": "1.0.0",
        "enabled": True,
        "items": ["a", "b", "c"],
    }


@pytest.fixture(scope="session")
def valid_yaml_schema():
    return {
        "name": {"type": "string", "required": True},
        "version": {"type": "string", "required": True},
        "enabled": {"type": "boolean", "required": True},
        "items": {"type": "list", "schema": {"type": "string"}},
    }
