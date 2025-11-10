# Загрузка файлов

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
    browser.find_element(By.NAME, "email").send_keys("Ivan@ivanov.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.NAME, "file").send_keys(file_path)

    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(8)
    browser.quit()