from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://pl-upgrade-customizer-stg.qstrike.net/")
#search_element = driver.find_element(By.XPATH, "//*[@title='Search']")
#search_element.send_keys("Hello World" + Keys.RETURN)
time.sleep(2)

click_element_ic = driver.find_element(By.CSS_SELECTOR, ".qx-login")
click_element_ic.click()

print(driver.title)

time.sleep(5)
driver.quit()







