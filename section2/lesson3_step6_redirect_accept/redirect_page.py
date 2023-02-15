from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base_page import BasePage
from section2.lesson1_step4_find_attribute_value import calc


class RedirectPage(BasePage):

    input_value_selector = (By.CSS_SELECTOR, '#input_value')
    answer_field_selector = (By.CSS_SELECTOR, '#answer')
    submit_btn_selector = (By.CSS_SELECTOR, '.btn')

    def __init__(self, driver: WebDriver):
        super().__init__(driver, driver.current_url)
        self.input_value_element = self.driver.find_element(*self.input_value_selector)
        self.answer_field_element = self.driver.find_element(*self.answer_field_selector)
        self.submit_btn_element = self.driver.find_element(*self.submit_btn_selector)

    def send_result(self):
        input_value = self.input_value_element.text
        result = calc(input_value)
        print('Input value: ', input_value)
        print('Result: ', result)

        self.answer_field_element.send_keys(result)
        self.submit_btn_element.click()




