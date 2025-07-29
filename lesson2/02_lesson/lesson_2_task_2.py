def is_year_leap(year):
    """
    Проверяет, является ли год високосным.

    :param year: Год (число)
    :return: True, если год високосный, иначе False
    """
    return year % 4 == 0


# Выберите год для проверки
year_to_check = 2024  # Замените на нужный вам год

# Вызов функции и сохранение результата
is_leap = is_year_leap(year_to_check)

# Вывод результата
print(f"год {year_to_check}: {is_leap}")


def is_year_leap(year):
    """
    Проверяет, является ли год високосным.

    :param year: Год (число)
    :return: True, если год високосный, иначе False
    """
    return year % 4 == 0


# Выберите год для проверки
year_to_check = 2023  # Замените на нужный вам год

# Вызов функции и сохранение результата
is_leap = is_year_leap(year_to_check)

# Вывод результата
print(f"год {year_to_check}: {is_leap}")


