from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_elt = browser.find_element(By.CSS_SELECTOR, 'input[required=""].first')
    last_name_elt = browser.find_element(By.CSS_SELECTOR, 'input[required=""].second')
    email_elt = browser.find_element(By.CSS_SELECTOR, 'input[required=""].third')

    first_name_elt.send_keys('test')
    last_name_elt.send_keys('test')
    email_elt.send_keys('test')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
