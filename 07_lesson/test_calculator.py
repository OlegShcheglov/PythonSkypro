from selenium import webdriver
from calculator_page import CalculatorPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def test_slow_calculator():
    # Инициализация Chrome WebDriver

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    calculator = CalculatorPage(driver)
    # Увеличиваем таймаут до 50 секунд для 45-секундной задержки

    calculator.set_delay("45")  # Установка задержки в 45 секунд
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    # Ожидание результата и проверка
    assert calculator.get_result() == '15', "Результат 15 не отобразился после 45 секунд ожидания"

    # Закрытие браузера
    driver.quit()
