import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_form_validation():
    # Инициализация Edge WebDriver
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    wait = WebDriverWait(driver, 10)  # Ожидание до 10 секунд


    try:
        # Открытие страницы
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        driver.maximize_window()


        # Ожидание доступности формы
        form = wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))


        # Заполнение формы
        test_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            # "zip-code" оставляем пустым
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }


        for field_name, value in test_data.items():
            field = wait.until(EC.element_to_be_clickable((By.NAME, field_name)))
            field.clear()
            field.send_keys(value)


        # Нажатие кнопки Submit
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()


        # Проверка подсветки полей
        # Zip code должен быть красным
        zip_code = wait.until(EC.visibility_of_element_located((By.ID, "zip-code")))
        assert "alert-danger" in zip_code.get_attribute("class"), "Поле Zip code должно быть подсвечено красным"


        # Остальные поля должны быть зелеными
        for field_name in test_data.keys():
            field = wait.until(EC.visibility_of_element_located((By.ID, field_name)))
            assert "alert-success" in field.get_attribute("class"), f"Поле {field_name} должно быть подсвечено зеленым"


    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    pytest.main(["-v", __file__])
