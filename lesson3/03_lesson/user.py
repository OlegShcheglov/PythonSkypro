class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        print(self.first_name)

    def print_last_name(self):
        print(self.last_name)

    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")

    def print_all(self):
        pass


# Пример использования класса User
if __name__ == "__main__":
    user = User("Иван", "Иванов")
    user.print_first_name()  # Выводит: Иван
    user.print_last_name()   # Выводит: Иванов
    user.print_full_name()   # Выводит: Иван Иванов
