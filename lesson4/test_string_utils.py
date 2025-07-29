import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


def test_capitalize_positive(string_utils):
    assert string_utils.capitalize("oleg") == "Oleg"
    assert string_utils.capitalize("Oleg") == "Oleg"
    assert string_utils.capitalize("") == ""


def test_capitalize_negative(string_utils):
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


# Переписал тест на удаление пробелов с использованием параметризации
@pytest.mark.parametrize("input_string, expected", [
    ("   oleg", "oleg"),
    ("oleg", "oleg"),
    ("   ", "")
])
def test_trim_positive(string_utils, input_string, expected):
    assert string_utils.trim(input_string) == expected


def test_trim_negative(string_utils):
    assert string_utils.trim("") == ""
    with pytest.raises(AttributeError):
        string_utils.trim(None)


def test_contains_positive(string_utils):
    assert string_utils.contains("Oleg", "O") is True
    assert string_utils.contains("Oleg", "K") is False
    assert string_utils.contains("", "S") is False


def test_contains_negative(string_utils):
    assert string_utils.contains("", "O") is False
    assert string_utils.contains("Oleg", "") is True
    with pytest.raises(TypeError):
        string_utils.contains("Oleg", None)

def test_delete_symbol_positive(string_utils):
    assert string_utils.delete_symbol("Oleg", "O") == "leg"
    assert string_utils.delete_symbol("Oleg", "Pro") == "Oleg"
    assert string_utils.delete_symbol("Oleg", "Ol") == "eg"


def test_delete_symbol_negative(string_utils):
    assert string_utils.delete_symbol("Oleg", "X") == "Oleg"  # Попытка удалить несуществующий символ
    assert string_utils.delete_symbol("", "O") == ""
    with pytest.raises(TypeError):
        string_utils.delete_symbol("Oleg", None)
