import math

def square(side):
    """
    Вычисляет площадь квадрата.

    :param side: Длина стороны квадрата (число)
    :return: Площадь квадрата (число), округленная вверх, если необходимо
    """
    area = side * side  # Вычисление площади квадрата
    return math.ceil(area)  # Округление вверх

# Пример использования функции
side_length = 4.5  # Замените это значение на нужное вам
area_result = square(side_length)

# Вывод результата
print(f"Площадь квадрата со стороной {side_length}: {area_result}")
