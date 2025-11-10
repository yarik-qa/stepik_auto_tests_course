# Модальные окна

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/alert_accept.html")

    browser.find_element(By.TAG_NAME, "button").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value").text
    calc = str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element(By.ID, "answer").send_keys(calc)
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(8)
    browser.quit()