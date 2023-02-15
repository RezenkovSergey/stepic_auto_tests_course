import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from section2.lesson1_step4_find_attribute_value import calc

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/explicit_wait2.html')

    price_element = WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100')
    )
    bookBtn = driver.find_element(By.CSS_SELECTOR, '#book')
    bookBtn.click()

    inputValueElement = driver.find_element(By.CSS_SELECTOR, '#input_value')
    answerElement = driver.find_element(By.CSS_SELECTOR, '#answer')
    submitBtn = driver.find_element(By.CSS_SELECTOR, '#solve')

    inputValue = inputValueElement.text
    result = calc(inputValue)
    print('Input value: ', inputValue)
    print('Result: ', result)

    answerElement.send_keys(result)
    submitBtn.click()

    time.sleep(10)

    driver.close()
