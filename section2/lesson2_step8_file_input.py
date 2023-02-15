import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    address = 'http://suninjuly.github.io/file_input.html'
    firstName = 'Ivan'
    lastName = 'Ivanov'
    email = 'ivanov@test.ru'

    filename = 'empty_file.txt'
    currentDir = os.path.abspath(os.path.dirname(__file__))
    filePath = os.path.join(currentDir, filename)

    driver = webdriver.Chrome()
    driver.get(address)

    firstNameInput = driver.find_element(By.CSS_SELECTOR, "[name='firstname']")
    lastNameInput = driver.find_element(By.CSS_SELECTOR, "[name='lastname']")
    emailInput = driver.find_element(By.CSS_SELECTOR, "[name='email']")
    fileInput = driver.find_element(By.CSS_SELECTOR, "[name='file']")
    submitBtn = driver.find_element(By.CSS_SELECTOR, '.btn')

    firstNameInput.send_keys(firstName)
    lastNameInput.send_keys(lastName)
    emailInput.send_keys(email)
    fileInput.send_keys(filePath)
    submitBtn.click()

    time.sleep(10)

    driver.quit()
    driver.close()
