from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from shop_page import SauceDemoPage
from selenium.webdriver.firefox.service import Service as FirefoxService


def test_sauce_demo_purchase():
    # Инициализация Firefox WebDriver
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    #driver = webdriver.Edge()

    shop = SauceDemoPage(driver)
    shop.login("standard_user", "secret_sauce")

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items_to_add:
        shop.add_product(item)

    shop.go_to_cart()
    shop.go_to_checkout()

    shop.fill_checkout_form("Иван", "Петров", "123456")

    total_text = shop.return_sum()

    assert total_text == "Total: $58.29", f"Итоговая сумма {total_text} не соответствует ожидаемой $58.29"

    driver.quit()
