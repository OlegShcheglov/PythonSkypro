from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.implicitly_wait(2)

driver.get("http://uitestingplayground.com/textinput")
driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")
driver.find_element(By.ID, "updatingButton").click()


print((driver.find_element(By.ID, "updatingButton")).text)

driver.quit()
