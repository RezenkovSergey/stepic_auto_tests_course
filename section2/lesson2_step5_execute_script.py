import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from lesson1_step4_find_attribute_value import calc


if __name__ == '__main__':
    script = 'return arguments[0].scrollIntoView(true);'
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/execute_script.html')

    numberElement = driver.find_element(By.CSS_SELECTOR, '#input_value')
    answerElement = driver.find_element(By.CSS_SELECTOR, '#answer')
    robotCheckbox = driver.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    robotsRuleElement = driver.find_element(By.CSS_SELECTOR, '#robotsRule')
    submitBtn = driver.find_element(By.CSS_SELECTOR, '.btn')

    numberStr = numberElement.text
    print('X: ', numberStr)

    result = calc(numberStr)
    print('Result: ', result)

    answerElement.send_keys(result)

    driver.execute_script(script, submitBtn)
    robotCheckbox.click()
    robotsRuleElement.click()
    submitBtn.click()

    time.sleep(10)
    driver.quit()
    driver.close()
