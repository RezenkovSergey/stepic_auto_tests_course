from section4.lesson2.pages.base_page import BasePage
from section4.lesson2.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, f'Expected "login" in url, got {current_url}'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LOCATOR), 'Not found Login Form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_LOCATOR), 'Not found Registration Form'

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_LOCATOR)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_LOCATOR)
        confirm_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PWD_LOCATOR)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BTN_LOCATOR)

        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_field.send_keys(password)
        register_btn.click()
        test_email = 'test-20230307190659@test.ru'
        test_password = 'eW7TZXupnMt6ayk'
