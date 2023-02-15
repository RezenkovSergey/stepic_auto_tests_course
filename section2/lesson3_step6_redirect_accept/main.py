import time

from selenium import webdriver
from main_page import MainPage

if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = 'http://suninjuly.github.io/redirect_accept.html'
    main_page = MainPage(driver, url)
    main_page.open()
    redirect_page = main_page.go_to_next_page()
    redirect_page.send_result()

    time.sleep(5)
    redirect_page.close()
