import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(str_n):
    return str(math.log(abs(12 * math.sin(int(str_n)))))


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/get_attribute.html")

    treasure_element = driver.find_element(By.CSS_SELECTOR, "#treasure")
    x = treasure_element.get_attribute("valuex")
    print("x: {fx}".format(fx=x))
    result = calc(x)
    print("Result: {f_result}".format(f_result=result))
    answerInput = driver.find_element(By.CSS_SELECTOR, "#answer")
    answerInput.send_keys(result)
    time.sleep(3)

    robotCheckbox = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robotCheckbox.click()

    robotRadio = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
    robotRadio.click()

    submitButton = driver.find_element(By.CSS_SELECTOR, ".btn-default")
    submitButton.click()

    time.sleep(10)
    driver.close()
