import time

import pytest

from section4.lesson2.pages.product_page import ProductPage
from section4.lesson2.pages.locators import ProductPageLocators
from section4.lesson2.tests.links import Links


@pytest.mark.parametrize('link', [Links.NEW_YEAR_LINK, Links.NEW_YEAR_2019_LINK])
def test_add_product_to_basket(browser, link):
    print(f'Go to {link}')
    product_page = ProductPage(browser, link)
    product_page.open()

    product_name = product_page.get_product_name()
    product_cost = product_page.get_product_cost()

    product_page.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON_LOCATOR)
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_added_product(product_name, product_cost)
