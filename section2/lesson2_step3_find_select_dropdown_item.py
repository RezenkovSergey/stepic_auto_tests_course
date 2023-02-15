import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/selects1.html")

    numberElement1 = driver.find_element(By.CSS_SELECTOR, '#num1')
    numberElement2 = driver.find_element(By.CSS_SELECTOR, '#num2')
    select = Select(driver.find_element(By.CSS_SELECTOR, '#dropdown'))
    btnSubmit = driver.find_element(By.CSS_SELECTOR, '.btn')

    number1 = numberElement1.text
    number2 = numberElement2.text
    result = int(number1) + int(number2)

    print('Number 1: ', number1)
    print('Number 2: ', number2)
    print('Result: ')

    select.select_by_value(str(result))
    btnSubmit.click()

    time.sleep(10)
    driver.close()
