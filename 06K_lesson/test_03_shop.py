import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


def test_sauce_demo_purchase():
    # Инициализация Firefox WebDriver
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    wait = WebDriverWait(driver, 10)


    try:
        # 1. Открытие сайта магазина
        driver.get("https://www.saucedemo.com/")


        # 2. Авторизация
        username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        username.send_keys("standard_user")


        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")


        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()


        # 3. Добавление товаров в корзину
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]


        for item_name in items_to_add:
            item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
            add_button = wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
            add_button.click()


        # 4. Переход в корзину
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_icon.click()


        # 5. Нажатие Checkout
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()


        # 6. Заполнение формы
        checkout_info = {
            "first-name": "Иван",
            "last-name": "Петров",
            "postal-code": "123456"
        }


        for field_id, value in checkout_info.items():
            field = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            field.send_keys(value)


        # 7. Нажатие Continue
        continue_button = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        continue_button.click()


        # 8. Проверка итоговой суммы
        total_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_text = total_element.text
        assert total_text == "Total: $58.29", f"Итоговая сумма {total_text} не соответствует ожидаемой $58.29"


    finally:
        # 9. Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    pytest.main(["-v", __file__])
