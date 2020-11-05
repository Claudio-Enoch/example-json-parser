import pytest

from json_parser import json_parser


@pytest.fixture(scope="session")
def json_parse():
    """Adding fixture simply to demonstrate fixture knowledge (added benefit of not needing to import in test files)"""
    return json_parser
