import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_slow_calculator():
    # Инициализация Chrome WebDriver
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 50)  # Увеличиваем таймаут до 50 секунд для 45-секундной задержки


    try:
        # Открытие страницы
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        driver.maximize_window()

        # Установка задержки
        delay_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys("45")


        # Нажатие кнопок 7 + 8 =
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))).click()


        # Ожидание результата и проверка
        result = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        assert result, "Результат 15 не отобразился после 45 секунд ожидания"


    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    pytest.main(["-v", __file__])
