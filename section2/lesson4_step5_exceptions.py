from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/cats.html')

    driver.find_element(By.ID, 'button')

    driver.close()
