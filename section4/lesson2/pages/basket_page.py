from section4.lesson2.pages.base_page import BasePage
from section4.lesson2.pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_LOCATOR), 'Expected empty basket'

    def should_be_message_for_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_LOCATOR), 'Expected empty basket message'
