import getpass
import time

from selenium import webdriver

from section3.lesson6_step4_login.main_page import MainPage

link = 'https://stepik.org/lesson/236895/step/1'
"""

"""
if __name__ == '__main__':
    email = getpass.getuser()
    password = getpass.getpass("Password: ", )

    driver = webdriver.Chrome()
    main_page = MainPage(driver, link)

    try:
        main_page.open().go_to_login()\
            .send_email(email)\
            .send_password(password)\
            .click_login_btn()
        time.sleep(10)
        print('Send keys')
        main_page.send_answer("test")
    finally:
        time.sleep(60)
        main_page.close()
        driver.quit()
