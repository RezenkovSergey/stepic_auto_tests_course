from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from section3.lesson6_step4_login.base_page import BasePage


class LoginPage(BasePage):
    email_selector = (By.ID, 'id_login_email')
    password_selector = (By.ID, 'id_login_password')
    login_btn_selector = (By.CLASS_NAME, 'sign-form__btn')

    def __init__(self, driver: WebDriver):
        super().__init__(driver, driver.current_url)

    def send_email(self, email_str):
        email_elt = self.driver.find_element(*self.email_selector)
        email_elt.send_keys(email_str)
        return self

    def send_password(self, password_str):
        password_elt = self.driver.find_element(*self.password_selector)
        password_elt.send_keys(password_str)
        return self

    def click_login_btn(self):
        login_btn = self.driver.find_element(*self.login_btn_selector)
        login_btn.click()


