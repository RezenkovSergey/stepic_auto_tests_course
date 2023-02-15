import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from lesson1_step4_find_attribute_value import calc

if __name__ == '__main__':
    address = 'http://suninjuly.github.io/alert_accept.html'

    driver = webdriver.Chrome()
    driver.get(address)
    goToJourneyBtn = driver.find_element(By.CSS_SELECTOR, "[type='submit']")

    goToJourneyBtn.click()
    alert = driver.switch_to.alert
    alert.accept()

    inputValueElement = driver.find_element(By.CSS_SELECTOR, '#input_value')
    answerElement = driver.find_element(By.CSS_SELECTOR, '#answer')
    submitBtn = driver.find_element(By.CSS_SELECTOR, '.btn')

    inputValue = inputValueElement.text
    result = calc(inputValue)
    print('Input value: ', inputValue)
    print('Result: ', result)

    answerElement.send_keys(result)
    submitBtn.click()

    time.sleep(10)

    driver.close()
