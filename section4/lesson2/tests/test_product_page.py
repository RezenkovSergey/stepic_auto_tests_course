import time

from section4.lesson2.pages.product_page import ProductPage
from section4.lesson2.pages.locators import ProductPageLocators
from section4.lesson2.tests.links import Links


def test_add_product_to_basket(browser):
    product_page = ProductPage(browser, Links.NEW_YEAR_LINK)
    product_page.open()
    product_page.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON_LOCATOR)
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_with_added_product()
    product_page.check_basket_value()
