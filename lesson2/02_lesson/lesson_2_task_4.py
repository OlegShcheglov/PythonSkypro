def fizz_buzz(n):
    """
    Печатает числа от 1 до n с заменой:
    - "Fizz" для чисел, делящихся на 3
    - "Buzz" для чисел, делящихся на 5
    - "FizzBuzz" для чисел, делящихся на 3 и 5
    :param n: Целое число, до которого печатать
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Пример использования функции
fizz_buzz(17)
