from section4.lesson2.pages.base_page import BasePage
from section4.lesson2.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON_LOCATOR)
        add_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LOCATOR).text

    def get_product_cost(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST_LOCATOR).text

    def should_be_message_with_added_product(self, product_name):
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME_LOCATOR).text
        assert product_name == added_product_name, f'Expected product name: {product_name}, got: {added_product_name}'

    def should_not_be_success_messages(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME_LOCATOR), \
            "Success message is presented, but should be not"

    def should_be_disappeared_success_msg(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NAME_LOCATOR), \
            "Success message is not disappeared, but should be"

    def check_basket_value(self, product_cost):
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE_LOCATOR).text
        assert basket_value == product_cost, f'Expected basket value: {product_cost}, got: {basket_value}'

    def check_added_product(self, product_name, product_cost):
        self.should_be_message_with_added_product(product_name)
        self.check_basket_value(product_cost)
