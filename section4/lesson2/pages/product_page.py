from section4.lesson2.pages.base_page import BasePage
from section4.lesson2.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON_LOCATOR)
        add_button.click()

    def should_be_message_with_added_product(self):
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME_LOCATOR).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LOCATOR).text
        assert product_name == added_product_name, f'Expected product name: {product_name}, got: {product_name}'

    def check_basket_value(self):
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE_LOCATOR).text
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_LOCATOR).text
        assert basket_value == product_cost, f'Expected basket value: {product_cost}, got: {basket_value}'
