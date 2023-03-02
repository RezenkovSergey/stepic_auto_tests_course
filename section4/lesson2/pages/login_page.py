from section4.lesson2.pages.base_page import BasePage
from section4.lesson2.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, f'Expected "login" in url, got {current_url}'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Not found Login Form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Not found Registration Form'
