from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from section3.lesson6_step4_login.base_page import BasePage
from section3.lesson6_step4_login.login_page import LoginPage


class MainPage(BasePage):
    login_link_selector = (By.ID, 'ember33')
    answer_textarea_selector = (By.CLASS_NAME, 'string-quiz__textarea')
    submit_btn_selector = (By.CLASS_NAME, 'submit-submission')
    hint_selector = (By.CLASS_NAME, 'smart-hints')

    def go_to_login(self):

        login_lnk = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.login_link_selector)
        )
        login_lnk.click()
        return LoginPage(self.driver)

    def send_answer(self, answer):
        answer_textarea_elt = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(self.answer_textarea_selector)
        )
        answer_textarea_elt.click()
        answer_textarea_elt.send_keys(answer)
        return self

    def submit_answer(self):
        submit_btn = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.submit_btn_selector)
        )
        submit_btn.click()

    def get_hint_text(self):
        hint_elt = self.driver.find_element(*self.hint_selector)
        return hint_elt.text
