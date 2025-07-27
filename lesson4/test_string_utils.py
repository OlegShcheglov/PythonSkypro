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


def test_capitalize_negative(string_utils):
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


def test_delete_symbol_negative(string_utils):
    assert string_utils.delete_symbol("Oleg", "X") == "Oleg"  # Попытка удалить несуществующий символ


# Переписал тест на удаление пробелов с использованием параметризации
@pytest.mark.parametrize("input_string, expected", [
    ("   oleg", "oleg"),
    ("oleg", "oleg"),
    ("   ", "")
])
def test_trim(string_utils, input_string, expected):
    assert string_utils.trim(input_string) == expected
