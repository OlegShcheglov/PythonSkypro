import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

def test_capitalize(string_utils):
    assert string_utils.capitalize("oleg") == "Oleg"
    assert string_utils.capitalize("Oleg") == "Oleg"
    assert string_utils.capitalize("") == ""

def test_trim(string_utils):
    assert string_utils.trim("   oleg") == "oleg"
    assert string_utils.trim("oleg") == "oleg"
    assert string_utils.trim("   ") == ""

def test_contains(string_utils):
    assert string_utils.contains("Oleg", "O") is True
    assert string_utils.contains("Oleg", "K") is False
    assert string_utils.contains("", "S") is False

def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("Oleg", "O") == "leg"
    assert string_utils.delete_symbol("Oleg", "Pro") == "Oleg"
    assert string_utils.delete_symbol("Oleg", "Ol") == "eg"