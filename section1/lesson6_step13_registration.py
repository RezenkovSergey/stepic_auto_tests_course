import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"


def calc_link():
    return str(math.ceil(math.pow(math.pi, math.e) * 10000))


if __name__ == '__main__':
    try:
        driver = webdriver.Chrome()
        driver.get(link)
        elements = driver.find_elements(By.TAG_NAME, 'input')
        for element in elements:
            element.send_keys('test')
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
        time.sleep(10)

    finally:
        driver.quit()
