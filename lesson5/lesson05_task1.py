from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.maximize_window()     # открыть окно по размеру экрана
driver.get("http://uitestingplayground.com/classattr")

# Находим кнопку по классу и кликаем
button = driver.find_element(By.CSS_SELECTOR, ".btn-primary.btn-test")
button.click()
